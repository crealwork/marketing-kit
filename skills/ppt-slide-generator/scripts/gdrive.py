"""Google Drive helpers using the clasp OAuth token (drive.file scope).

Reused by the Google Slides delivery pipeline (see ../google-slides-export.md).
Battle-tested 2026-07-03 (Sundayable AI webinar deck, 33 slides).
"""
import json
import os
import sys
import time
import urllib.request
import urllib.parse
import uuid

sys.stdout.reconfigure(encoding="utf-8")

CLASPRC = os.path.expanduser("~/.clasprc.json")

PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
GSLIDES_MIME = "application/vnd.google-apps.presentation"


def access_token() -> str:
    d = json.load(open(CLASPRC))
    tok = d["tokens"]["default"]
    data = urllib.parse.urlencode({
        "client_id": tok["client_id"],
        "client_secret": tok["client_secret"],
        "refresh_token": tok["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    return json.load(urllib.request.urlopen(req, timeout=30))["access_token"]


def upload_pptx_as_slides(pptx_path: str, name: str, file_id: str | None = None) -> dict:
    """Upload pptx converted to Google Slides. If file_id given, update in place
    (PATCH keeps the URL stable across design iterations)."""
    token = access_token()
    boundary = uuid.uuid4().hex
    meta = {"name": name}
    if not file_id:
        meta["mimeType"] = GSLIDES_MIME
    body = (
        f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
        f"{json.dumps(meta)}\r\n"
        f"--{boundary}\r\nContent-Type: {PPTX_MIME}\r\n\r\n"
    ).encode() + open(pptx_path, "rb").read() + f"\r\n--{boundary}--".encode()
    if file_id:
        url = f"https://www.googleapis.com/upload/drive/v3/files/{file_id}?uploadType=multipart"
        method = "PATCH"
    else:
        url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
        method = "POST"
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": f"multipart/related; boundary={boundary}",
    })
    return json.load(urllib.request.urlopen(req, timeout=180))


def export_pdf(file_id: str, out_path: str) -> str:
    """Export a Google Slides file as PDF (works for files created via drive.file)."""
    token = access_token()
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}/export?mimeType=application/pdf"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
            data = urllib.request.urlopen(req, timeout=300).read()
            open(out_path, "wb").write(data)
            return out_path
        except Exception as e:  # export can 500 right after conversion
            if attempt == 3:
                raise
            print(f"export retry {attempt + 1}: {e}", flush=True)
            time.sleep(5 * (attempt + 1))


def delete_file(file_id: str) -> None:
    token = access_token()
    req = urllib.request.Request(
        f"https://www.googleapis.com/drive/v3/files/{file_id}",
        method="DELETE", headers={"Authorization": f"Bearer {token}"})
    urllib.request.urlopen(req, timeout=30)
