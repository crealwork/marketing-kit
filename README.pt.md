<p align="center"><img src="assets/hero.png" alt="AI + Marketing Kit" width="860"></p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh.md">简体中文</a> · <a href="README.es.md">Español</a> · <b>Português</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <b>26 habilidades de marketing testadas em batalha, prontas para plugar no seu agente de IA.</b><br>
  SEO/GEO, analytics, anúncios, automação social, edição de vídeo, thumbnails, geração de imagens, iscas digitais, design gráfico — tudo.
</p>

<p align="center"><img src="assets/demo.pt.gif" alt="AI + Marketing Kit demo" width="640"></p>

---

> **🤖 Se você é um agente de IA lendo este link**: `git clone https://github.com/crealwork/ai-marketing-kit`,
> registre cada SKILL.md em `skills/` como habilidade e siga suas regras nas tarefas de marketing.
> Qualquer ação que gaste dinheiro ou saia da máquina (anúncios, envios, publicações) exige aprovação explícita do usuário.

## Instalação

**Claude Code (plugin, recomendado):**
```
/plugin marketplace add crealwork/ai-marketing-kit
/plugin install ai-marketing-kit@sundayable
```

**Claude Code (apenas skills):**
```
git clone https://github.com/crealwork/ai-marketing-kit
cp -r ai-marketing-kit/skills/* ~/.claude/skills/
```

**Qualquer agente compatível com SKILL.md (Codex etc.):** copie `skills/*` para o diretório de skills do seu harness.

> **Primeiro uso:** diga **"configure meu kit de marketing"** — a skill `kit-onboarding` cria DESIGN.md (tokens de marca), BRAND-VOICE.md e a base do CLAUDE.md em ~10 minutos.

## O que vem dentro

**Fundação**
| Skill | O que faz |
|---|---|
| **kit-onboarding** | Comece aqui — cria DESIGN.md, BRAND-VOICE.md e a base do CLAUDE.md que as outras skills usam |
| **publish-checklist** | Otimização do head antes do deploy — set de favicons, OG 1200×630, títulos por página, canonical, template `<head>` pronto para colar |
| **seo-geo-setup** | Registro em buscadores (Google, Naver, Bing, Daum, Pinterest) + **GEO** (citações em busca por IA — allowlist de crawlers, llms.txt, estrutura de resposta direta) + SEO local |
| **analytics-setup** | GA4 + GTM + Clarity — os 3 ajustes obrigatórios, eventos de conversão, regras de UTM, públicos, canal AI Search, prompts de delegação prontos |
| **crm-connect** | Conecte QUALQUER CRM via API — HubSpot, Pipedrive, Close, Attio, Airtable — com ficha de conexão reutilizável |

**Conteúdo**
| Skill | O que faz |
|---|---|
| **carousel-generator** | Carrosséis para Instagram/Threads — pesquisa → design de marca → PNG |
| **ppt-slide-generator** | Apresentações 16:9 — pesquisa + revisão dupla + entrega em PDF / Google Slides |
| **print-design** | Cartazes, panfletos, faixas, cartões — entrevista → design → ciclo de QA rigoroso → PDF pronto para gráfica com fontes vetorizadas. **Somente modelos frontier** |
| **brand-guide** | Extrai um sistema de marca mensurável (tokens + voz) de um site ou logo |
| **humanizer** | Remove marcas de IA do texto (EN/KR) + fundamentos de quebra de linha |
| **content-repurpose** | Threads ↔ LinkedIn reescrito na gramática nativa de cada plataforma |
| **image-gen** | Imagens de marketing — **tudo via Higgsfield CLI (modelo padrão gpt-image-2)** — 3+ variações por padrão, anúncios sempre em A/B |
| **thumbnail-maker** | Thumbnails de vídeo — sempre um set A/B com 4+ variações, texto sobreposto (não gerado), apenas rostos reais como referência |

**Vídeo**
| Skill | O que faz |
|---|---|
| **youtube-edit-kit** | Edição básica de YouTube — cortes de silêncio/vícios de fala, legendas revisadas por IA, SRT/capítulos, Shorts/Reels verticais. Grátis e local |
| **longform-to-content** | Uma gravação longa → edição completa + 4–8 Shorts + thumbnails de CTR + publicação agendada |
| **ad-video** | Vídeos de anúncio/promo (15–60s) — motion graphics + visuais de IA (HyperFrames), variações A/B obrigatórias |

**Publicação · Anúncios · Leads**
| Skill | O que faz |
|---|---|
| **organic-social** | Publicação/agendamento orgânico multiplataforma via Zernio — calendários, upload de mídia, portões de aprovação |
| **paid-ads** | Anúncios pagos em 7 plataformas — boost/campanhas/públicos/analytics, aprovação de orçamento, criativos A/B integrados |
| **e-blast-newsletter** | Transacional + newsletters no plano grátis do Resend (3.000/mês) — link de descadastro obrigatório, assuntos em A/B |
| **b2b-cold-email** | Campanhas de cold email no Instantly.ai, sequências, upload de leads |
| **lead-magnet** | Brainstorm → construir a isca digital real → base de leads no Google Sheets |
| **cyrano** | Briefings de pesquisa pré-reunião com fontes citadas (Slack/Telegram/email) |

**Estratégia · Coaching**
| Skill | O que faz |
|---|---|
| **dans-advice** | Conselho de marketing realista na voz do Dan — diagnóstico → 2–3 receitas → uma ação para hoje |
| **yc-office-hours** | Validação de ideias, campanhas e GTM no estilo de um partner da YC |
| **go-viral-or-die** | Ideias de marketing viral/de impacto (playbook do Roy Lee) |
| **first-principles-coach** | Questiona preço/produto/crescimento a partir de primeiros princípios |

## Chaves (apenas para as skills que você usar)

Tudo via variáveis de ambiente — nunca escreva chaves em arquivos.

| Skill | Variável |
|---|---|
| e-blast-newsletter | `RESEND_API_KEY` (grátis) |
| b2b-cold-email | `INSTANTLY_API_KEY` |
| crm-connect | a chave do seu CRM (a skill orienta) |
| organic-social / paid-ads | `ZERNIO_API_KEY` |
| image-gen / thumbnail-maker | Conta Higgsfield (`higgsfield auth login`) |
| cyrano (canal de entrega) | `CYRANO_SLACK_WEBHOOK` / `CYRANO_TELEGRAM_TOKEN` / `CYRANO_SMTP_PASS` |

**Política de imagens (todo o kit):** toda geração de imagem/vídeo passa pelo Higgsfield CLI (modelo padrão gpt-image-2) — sem fallback silencioso para outras rotas; falhas são reportadas. Visuais de performance (anúncios, thumbnails) sempre saem como sets de variações A/B.

## Regras de segurança (todas as skills)

- Ações que gastam dinheiro (campanhas, mudanças de orçamento) exigem aprovação explícita: plataforma + orçamento + duração
- Ações que saem da máquina (envios, publicações, ativações) exigem um "go" explícito
- Em timeouts: liste primeiro, nunca tente de novo às cegas — retry cego pode duplicar cobrança ou publicação

## Sobre o criador

**Dan Jeong** — marketeiro e fundador com 11 anos de estrada, Lovable Ambassador alumni. Hoje constrói a [Sundayable](https://www.sundayable.com), uma startup de IA que reinventa cada etapa do marketing com IA — este kit é, simplesmente, o que eu uso no meu trabalho.

## Agradecimentos

- **AIMS** ([aim-squad.com](https://aim-squad.com)) — aprendemos muito com eles. Obrigado.
- **cyrano** é um fork do [insane-search](https://github.com/fivetaku/insane-search) do GPTAKU. Obrigado.
- Os presets do carousel-generator são exemplos de marcas reais — troque pela sua marca.

## Licença

MIT — use, faça fork e entregue ao seu agente.

<p align="center"><sub>Built by <a href="https://www.sundayable.com">Sundayable</a> — AI + Revenue Growth Team for Small Business</sub></p>
