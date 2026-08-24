# Casos de uso

Formato: **Ator · Objetivo · Pré · Fluxo · Alternativas · Pós · Regras · Plano/receita**

Legenda planos: **F** Free · **P** Pro · **B** Business · **A** Agency · **—** visitante/sistema

---

## A. Marketing e descoberta

### UC-01 — Ver landing e planos
| | |
|---|---|
| **Ator** | Visitante |
| **Objetivo** | Entender produto e preços |
| **Pré** | Nenhuma |
| **Fluxo** | 1. Acessa `www.` 2. Vê hero, exemplos, comparativo planos 3. Clica CTA (Free ou Pro/Business) |
| **Alt** | 3a. Clica demo/exemplo de bio pública |
| **Pós** | Redireciona signup ou checkout |
| **Regras** | Sem cookie de app; página cacheável |
| **Receita** | Topo do funil |

### UC-02 — Ver bio demo pública
| | |
|---|---|
| **Ator** | Visitante |
| **Objetivo** | Ver qualidade da página publicada |
| **Pré** | URL demo existe |
| **Fluxo** | 1. Abre `{demo}.sites…` ou domínio demo 2. Navega links/WhatsApp 3. (F) vê selo rodapé |
| **Alt** | 2a. Clica selo → landing (UC-01) |
| **Pós** | Analytics demo opcional |
| **Receita** | Prova social |

### UC-03 — Comparar planos na pricing
| | |
|---|---|
| **Ator** | Visitante |
| **Objetivo** | Escolher tier |
| **Fluxo** | 1. Abre `/pricing` 2. Compara limites (links, domínio, páginas, form) 3. Escolhe tier |
| **Regras** | Destaque Pro “recomendado”; Business para institucional |
| **Receita** | ARPU |

### UC-04 — Entrar via selo de bio free alheia
| | |
|---|---|
| **Ator** | Visitante de bio F |
| **Objetivo** | Descobrir a plataforma |
| **Fluxo** | 1. Clica “Feito com X” 2. Landing com UTM/ref 3. UC-01 ou UC-76 |
| **Receita** | Viral loop free |

### UC-05 — SEO landing indexada
| | |
|---|---|
| **Ator** | Busca Google |
| **Objetivo** | Achar produto |
| **Fluxo** | 1. Indexa `www` 2. Snippet com proposta clara |
| **Regras** | Canonical em `www`; sites de cliente indexam URL canônica deles (UC-37) |

---

## B. Conta e autenticação

### UC-06 — Login magic link (conta existente)
| | |
|---|---|
| **Ator** | Usuário |
| **Objetivo** | Acessar dashboard |
| **Pré** | `users.email` existe |
| **Fluxo** | 1. Informa e-mail em `app` 2. Recebe link 3. Clica → sessão em `app` 4. Redireciona dashboard/onboard pendente |
| **Alt** | 2a. E-mail inválido → mensagem genérica (anti-enum) |
| **Pós** | Cookie `Domain=app.` |
| **Regras** | Link expira (ex. 15 min); one-time |
| **Plano** | Todos |

### UC-07 — Sessão expirada
| | |
|---|---|
| **Ator** | Usuário |
| **Fluxo** | 1. Request sem sessão 2. Redirect login 3. Após login volta à rota |
| **Regras** | API autenticada só em `app` |

### UC-08 — Logout
| | |
|---|---|
| **Fluxo** | 1. Logout 2. Invalida sessão 3. Redirect `www` |

### UC-09 — Conta com múltiplos tenants (futuro A)
| | |
|---|---|
| **Ator** | Usuário Agency |
| **Pré** | Plano A; N tenants |
| **Fluxo** | 1. Dashboard lista sites 2. Seleciona tenant ativo 3. Edita contexto daquele site |
| **Receita** | MRR Agency |

### UC-10 — Convite membro time (futuro A)
| | |
|---|---|
| **Fluxo** | 1. Owner convida e-mail 2. Membro aceita magic link 3. Permissão editor/admin no tenant |
| **Plano** | A |

### UC-11 — Turnstile no login/signup
| | |
|---|---|
| **Ator** | Sistema |
| **Fluxo** | 1. Form protegido Turnstile 2. Falha → bloqueia envio |
| **Regras** | Anti-abuse free |

### UC-12 — Excluir conta (LGPD)
| | |
|---|---|
| **Ator** | Usuário |
| **Pré** | Assinatura cancelada ou nunca paga |
| **Fluxo** | 1. Solicita exclusão 2. Confirma e-mail 3. Anonimiza/apaga user; agenda drop R2 em 30d |
| **Regras** | Export oferecido antes (UC-45) |

---

## C. Assinatura e PSP

### UC-13 — Escolher plano e ir ao checkout
| | |
|---|---|
| **Ator** | Visitante |
| **Objetivo** | Assinar Pro ou Business |
| **Fluxo** | 1. Escolhe plano 2. PSP Checkout (cartão/PIX conforme PSP) 3. Paga |
| **Pós** | `success_url` UX only; conta vem no webhook |
| **Receita** | **MRR nasce aqui** |

### UC-14 — Webhook pagamento confirmado
| | |
|---|---|
| **Ator** | PSP → Worker app |
| **Pré** | Checkout completado |
| **Fluxo** | 1. Valida assinatura webhook 2. Upsert `users` por e-mail checkout 3. Cria `tenant` vazio + `subscription(active, plan)` 4. Enfileira magic link |
| **Alt** | 1a. Assinatura inválida → 401 log 2a. Idempotência por `event_id` |
| **Pós** | Tenant sem slug ainda |
| **Regras** | **Única fonte de criação de conta paga** |

### UC-15 — Webhook pagamento falhou / abandonado
| | |
|---|---|
| **Fluxo** | 1. Evento failed/expired 2. Não cria tenant 3. Log + e-mail recuperação opcional |
| **Pós** | Sem conta órfã |

### UC-16 — PIX atrasado (async)
| | |
|---|---|
| **Fluxo** | 1. Checkout PIX pending 2. success_url “aguardando” 3. Webhook paid → UC-14 |
| **Regras** | Conta só após paid |

### UC-17 — Primeiro acesso pós-pagamento
| | |
|---|---|
| **Ator** | Cliente novo pago |
| **Fluxo** | 1. Abre magic link 2. Sessão 3. Redirect onboard (UC-23) |
| **Regras** | Nunca publicar site no webhook |

### UC-18 — Renovação mensal OK
| | |
|---|---|
| **Ator** | PSP |
| **Fluxo** | 1. `invoice.paid` 2. `subscription.status=active` 3. Mantém acesso |
| **Receita** | Retenção MRR |

### UC-19 — Cobrança falhou (inadimplente)
| | |
|---|---|
| **Fluxo** | 1. `invoice.failed` 2. `subscription.status=past_due` 3. Dashboard trava edição/publish 4. Site público **continua** |
| **Regras** | Grace 3–7d antes pausa pública |

### UC-20 — Pausar site público por inadimplência
| | |
|---|---|
| **Pré** | past_due &gt; N dias |
| **Fluxo** | 1. Cron/worker marca tenant `paused_billing` 2. KV atualizado 3. Worker sites serve página “assinatura pausada” **mesmo host** |
| **Regras** | Não apagar R2 no dia 1 |

### UC-21 — Regularizar pagamento
| | |
|---|---|
| **Fluxo** | 1. Cliente atualiza pagamento 2. Webhook paid 3. Restaura active 4. Site volta HTML normal |
| **Receita** | Recuperação MRR |

### UC-22 — Cancelar assinatura
| | |
|---|---|
| **Fluxo** | 1. Cancel no portal PSP ou app 2. `cancel_at_period_end` ou imediato 3. Fim período → UC-73 |
| **Regras** | Oferecer export (UC-45) |

---

## D. Onboarding

### UC-23 — Escolher slug
| | |
|---|---|
| **Ator** | Usuário pago/free pós-conta |
| **Objetivo** | Definir URL pública |
| **Fluxo** | 1. Digita slug 2. Valida disponível 3. Salva `tenants.slug` |
| **Alt** | 2a. Reservado/ofensivo → erro 2b. Já usado → erro |
| **Pós** | `{slug}.sites…` reservado logicamente |
| **Regras** | Reservados: www, app, sites, api, … |
| **Plano** | F/P/B |

### UC-24 — Escolher starter / tipo de site
| | |
|---|---|
| **Fluxo** | 1. Escolhe bio-lista / bio-oferta / inst-* / port-* 2. Preenche `page_model` template |
| **Regras** | Institucional bloqueado se plano F (UC-79) |
| **Plano** | P/B |

### UC-25 — Preencher conteúdo inicial
| | |
|---|---|
| **Fluxo** | 1. Nome, bio, foto 2. WhatsApp + links 3. Salva draft no SQL |
| **Regras** | Free: max links (UC-79) |

### UC-26 — Pular e publicar depois
| | |
|---|---|
| **Fluxo** | 1. Salva draft 2. Dashboard lembra onboard incompleto |
| **Pós** | Tenant existe; site pode 404 até UC-41 |

### UC-27 — Concluir onboard → publicar
| | |
|---|---|
| **Fluxo** | 1. Clica Publicar 2. UC-41 3. Redirect URL pública |
| **Pós** | Primeiro 200 = marco de ativação |

---

## E. Editor e conteúdo

### UC-28 — Abrir editor com preview
| | |
|---|---|
| **Ator** | Usuário autenticado |
| **Pré** | Sessão; tenant ativo; subscription permite editar |
| **Fluxo** | 1. Abre editor 2. Lista blocos 3. Preview mobile ao vivo (draft ou último publish) |
| **Regras** | Appsha-like: + Add Block |

### UC-29 — Adicionar bloco link
| | |
|---|---|
| **Fluxo** | 1. Add Block → Link 2. Título, URL, ícone/thumb opcional 3. Salva draft |
| **Alt** | Free excede limite → paywall UC-66 |
| **Plano** | F limitado / P ilimitado |

### UC-30 — Adicionar bloco WhatsApp
| | |
|---|---|
| **Fluxo** | 1. Add Block → WhatsApp 2. Telefone + mensagem pré-preenchida 3. Preview botão verde |
| **Receita** | Diferencial BR |

### UC-31 — Editar perfil (avatar, nome, bio)
| | |
|---|---|
| **Fluxo** | 1. Edita campos 2. Upload imagem → staging R2 3. Salva draft |

### UC-32 — Reordenar / remover blocos
| | |
|---|---|
| **Fluxo** | 1. Drag order 2. Delete bloco 3. Autosave draft |

### UC-33 — Trocar tema / skin
| | |
|---|---|
| **Fluxo** | 1. Galeria temas 2. Aplica preview 3. Salva |
| **Regras** | Premium skins → paywall P |
| **Plano** | F: 1 skin · P/B: catálogo |

### UC-34 — Criar site institucional multi-página
| | |
|---|---|
| **Pré** | Plano B+ |
| **Fluxo** | 1. Add página (Sobre, Serviços, Contato…) 2. Edita cada uma 3. Menu navegação |
| **Receita** | **Business MRR** |

### UC-35 — Starter portfólio (galeria projetos)
| | |
|---|---|
| **Plano** | B |
| **Fluxo** | 1. Starter port-studio 2. Projetos com imagens 3. Publish |

### UC-36 — Configurar menu e footer institucional
| | |
|---|---|
| **Plano** | B |

### UC-37 — Configurar SEO por página
| | |
|---|---|
| **Fluxo** | 1. Title, description, OG image 2. Salva 3. Publish inclui meta |
| **Plano** | B (básico P: só home) |

### UC-38 — Adicionar embed (YT, Maps, Spotify)
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Add embed URL 2. Valida allowlist 3. Preview iframe |

### UC-39 — Adicionar highlights (chips)
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Add highlight texto/ícone 2. Ordena abaixo nome |

### UC-40 — Adicionar galeria de imagens
| | |
|---|---|
| **Plano** | P+ (bio) / B (institucional) |
| **Fluxo** | 1. Upload N imagens 2. Layout grid/carrossel 3. Publish copia assets |

---

## F. Publicação

### UC-41 — Publicar site (assíncrono)
| | |
|---|---|
| **Ator** | Usuário |
| **Pré** | Draft válido; assinatura active (ou F dentro limite); slug definido |
| **Fluxo** | 1. Clica Publicar 2. API valida plano/limites 3. Enfileira job `{tenant_id, rev}` 4. Responde **202** + job id 5. Worker publish renderiza 6. Grava `sites/{id}/builds/{rev}/` 7. Promove `current/` 8. Invalida KV host 9. Notifica “no ar” (poll/UI) |
| **Alt** | 5a. Falha render → `current` intacto; erro no dashboard |
| **Regras** | Botão **nunca** espera render sync |
| **Plano** | Todos (limites variam) |

### UC-42 — Republicar após edição
| | |
|---|---|
| **Fluxo** | Igual UC-41; rev incrementa |

### UC-43 — Status publish em andamento
| | |
|---|---|
| **Fluxo** | 1. UI polling/SSE 2. Estados: queued, building, live, failed |

### UC-44 — Rollback para revisão anterior (futuro)
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Lista builds 2. Promove rev anterior → current |

### UC-45 — Exportar site (zip)
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Solicita export 2. Job empacota `current/` 3. Link download temporário R2 |
| **Receita** | Retenção; reduz churn “medo de lock-in” |

### UC-46 — Preview draft sem publish (futuro)
| | |
|---|---|
| **Fluxo** | 1. URL draft tokenizada 2. Não indexável |

---

## G. Site público (visitante)

### UC-47 — Abrir bio por subdomínio
| | |
|---|---|
| **Ator** | Visitante |
| **Fluxo** | 1. GET `{slug}.sites…` 2. Worker resolve Host→tenant (KV/SQL) 3. Serve `current/index.html` + assets |
| **Regras** | Sem cookie app |

### UC-48 — Abrir bio por domínio custom
| | |
|---|---|
| **Pré** | Custom Hostname active; plano P+ |
| **Fluxo** | 1. GET `bio.cliente.com` 2. Lookup custom_domains 3. Mesmo prefixo R2 |
| **Receita** | Pro |

### UC-49 — Clicar link / WhatsApp na bio
| | |
|---|---|
| **Fluxo** | 1. Click 2. (P) registra Analytics Engine 3. Redirect wa.me ou URL |
| **Plano** | Analytics P only |

### UC-50 — Ver selo rodapé (free)
| | |
|---|---|
| **Plano** | F |
| **Fluxo** | 1. Worker injeta selo HTML no response **ou** template flag 2. Link landing |
| **Receita** | Upgrade + viral |

### UC-51 — Site pausado (billing ou inatividade)
| | |
|---|---|
| **Pré** | `paused_billing` ou `paused_inactivity` |
| **Fluxo** | 1. Mesmo Host 2. Página estática explicativa 3. CTA dono login |
| **Regras** | Não 404; SEO menos pior |

### UC-52 — Site inexistente / slug inválido
| | |
|---|---|
| **Fluxo** | 404 genérico plataforma |

### UC-53 — Asset estático (CSS, JS, imagem)
| | |
|---|---|
| **Fluxo** | 1. GET path 2. R2 `sites/{id}/current/{path}` 3. Cache headers |

### UC-54 — Canonical e OG corretos
| | |
|---|---|
| **Regras** | Canonical = domínio custom se active; senão subdomínio; nunca `app.` |

### UC-55 — Página institucional multi-URL
| | |
|---|---|
| **Plano** | B |
| **Fluxo** | 1. `/`, `/sobre`, … 2. Mesmo tenant; paths no R2 |

---

## H. Domínio custom

### UC-56 — Iniciar conexão domínio próprio
| | |
|---|---|
| **Ator** | Usuário P+ |
| **Fluxo** | 1. Config → Domínio 2. Informa hostname 3. API cria Custom Hostname CF 4. Mostra instrução CNAME |

### UC-57 — Verificar propagação DNS
| | |
|---|---|
| **Fluxo** | 1. Poll status CF 2. UI: pending / active / failed 3. Active → UC-58 |

### UC-58 — Servir site no domínio custom
| | |
|---|---|
| **Pós** | KV mapeia hostname→tenant; canonical atualizado no próximo publish |

### UC-59 — Remover domínio custom
| | |
|---|---|
| **Fluxo** | 1. Remove hostname 2. CF delete 3. Volta só subdomínio |

### UC-60 — Falha certificado / DCV
| | |
|---|---|
| **Fluxo** | 1. Status failed 2. Instruções TXT/CNAME 3. Retry |

---

## I. Analytics e ferramentas

### UC-61 — Ver cliques por link (dashboard)
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Abre Analytics 2. Agrega Analytics Engine por link/período |

### UC-62 — Ver visitas página (agregado)
| | |
|---|---|
| **Plano** | P básico / B avançado |

### UC-63 — Registrar evento clique (edge)
| | |
|---|---|
| **Ator** | Worker sites |
| **Fluxo** | 1. Redirect endpoint `/r/{link_id}` 2. Write AE 3. 302 destino |
| **Regras** | Free não grava |

### UC-64 — Gerar QR code da URL canônica
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Dashboard gera PNG/SVG 2. Download |
| **Receita** | Valor percebido Pro |

### UC-65 — Export CSV analytics (futuro B)
| | |
|---|---|
| **Plano** | B |

---

## J. Upgrade, downgrade, limites

### UC-66 — Hit paywall limite links (free)
| | |
|---|---|
| **Fluxo** | 1. Tenta add link 9 2. Modal upgrade 3. Checkout Pro |

### UC-67 — Hit paywall remover selo
| | |
|---|---|
| **Fluxo** | 1. Clica “Remover selo” 2. Checkout Pro |

### UC-68 — Upgrade Free → Pro
| | |
|---|---|
| **Fluxo** | 1. Checkout 2. UC-14 atualiza plan 3. Próximo publish sem selo; unlock domínio/analytics |

### UC-69 — Upgrade Pro → Business
| | |
|---|---|
| **Fluxo** | 1. Checkout delta ou full 2. Unlock multi-página, form, 2º site |

### UC-70 — Downgrade Business → Pro
| | |
|---|---|
| **Fluxo** | 1. Agendado fim período 2. Excesso páginas → read-only ou escolher 1 página |
| **Regras** | Não apagar conteúdo dia 1 |

### UC-71 — Downgrade Pro → Free (raro)
| | |
|---|---|
| **Fluxo** | 1. Cancel Pro 2. vira F com selo + limites 3. Custom domain desvincula |

### UC-72 — Tentativa usar feature sem plano
| | |
|---|---|
| **Fluxo** | 1. API 403 `PLAN_REQUIRED` 2. UI paywall |

### UC-73 — Pós-cancelamento período encerrado
| | |
|---|---|
| **Fluxo** | 1. status canceled 2. Dashboard read-only 3. Site pausado ou selo+free policy 4. Export disponível 30d |

### UC-74 — Cupom / trial Pro 14d (opcional)
| | |
|---|---|
| **Fluxo** | 1. Checkout trial 2. Webhook trialing 3. Lembrete D-3 cartão |
| **Receita** | Conversão; cuidado zumbi |

### UC-75 — Add-on 2º site (Pro ou B)
| | |
|---|---|
| **Receita** | MRR add-on |

---

## K. Plano Free

### UC-76 — Signup free sem cartão
| | |
|---|---|
| **Fluxo** | 1. Landing “Começar grátis” 2. E-mail 3. Magic link 4. Cria user + tenant `plan=free` |
| **Regras** | Sem PSP na porta |

### UC-77 — Publicar bio free
| | |
|---|---|
| **Pré** | UC-76; limites UC-79 |
| **Fluxo** | UC-41 com flag selo |

### UC-78 — Free trial Pro embarcado (opcional)
| | |
|---|---|
| **Nota** | Appsha faz 14d; nosso default é **não** — ver [freemium.md](freemium.md) |

### UC-79 — Enforcement limites free
| | |
|---|---|
| **Regras** | Bio only; 5–8 links; 1 skin; sem analytics/export/CNAME/form/institucional |

### UC-80 — Pausa inatividade 90 dias
| | |
|---|---|
| **Ator** | Cron |
| **Fluxo** | 1. Sem publish E sem visita 90d 2. `paused_inactivity` 3. UC-51 4. Dono pode reativar login + publish |
| **Receita** | Margem free |

---

## L. Captura de leads (Business)

### UC-81 — Adicionar bloco formulário
| | |
|---|---|
| **Plano** | B |
| **Fluxo** | 1. Add form (nome, email, msg campos) 2. Publish inclui form POST |

### UC-82 — Visitante envia formulário
| | |
|---|---|
| **Fluxo** | 1. POST Worker endpoint 2. Turnstile 3. Grava lead SQL 4. E-mail dono 5. Tela obrigado |
| **Regras** | Não CRM pesado v1 — lista + e-mail |

### UC-83 — Dono vê lista leads
| | |
|---|---|
| **Plano** | B |
| **Fluxo** | 1. Dashboard Leads 2. Filtro data 3. Export CSV opcional |

### UC-84 — Bloco com janela de exibição
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. `starts_at`/`ends_at` 2. Publish + Worker oculta fora janela |

### UC-85 — Card produto afiliado / loja externa
| | |
|---|---|
| **Plano** | P+ |
| **Fluxo** | 1. Imagem, título, preço, URL externa 2. Click UC-49 |

---

## M. Multi-site e agência

### UC-86 — Criar 2º tenant mesma conta
| | |
|---|---|
| **Plano** | B ou add-on |
| **Fluxo** | 1. “Novo site” 2. Novo slug 3. Onboard curto |

### UC-87 — Alternar entre sites no dashboard
| | |
|---|---|
| **Fluxo** | 1. Switcher 2. Contexto tenant muda |

### UC-88 — Plano Agency N sites
| | |
|---|---|
| **Receita** | MRR alto |

### UC-89 — Membro edita site cliente
| | |
|---|---|
| **Plano** | A · UC-10 |

### UC-90 — Remover selo white-label Agency
| | |
|---|---|
| **Plano** | A opcional |

---

## N. Operações e sistema

### UC-91 — Idempotência webhook PSP
| | |
|---|---|
| **Ator** | Sistema |
| **Fluxo** | 1. `event_id` dedup table 2. Replay safe |

### UC-92 — Retry fila publish
| | |
|---|---|
| **Fluxo** | 1. Falha job 2. Retry N 3. DLQ alerta ops |

### UC-93 — Monitoramento health
| | |
|---|---|
| **Fluxo** | 1. `/health` workers 2. Alerta fila atrasada |

### UC-94 — Backup SQL / snapshot R2 (ops)
| | |
|---|---|
| **Periodicidade** | SQL daily; R2 lifecycle |

### UC-95 — Feature flag por plano
| | |
|---|---|
| **Fluxo** | 1. `plan_features` map 2. API centraliza UC-72 |

---

## O. Mapa caso → fase

| Fase | Casos de uso |
|---|---|
| F0 | UC-91, UC-93, UC-95 |
| F1 | UC-01, 13–17, 23–27, 29–32, 41–43, 47, 49, 52–53 |
| F2 | UC-18–21, 48, 56–58, 61–64, 45, 33, 54 |
| F3 | UC-04, 50, 66–68, 76–77, 79–80 |
| F4 | UC-03, 34–37, 55, 69, 86–87 |
| F5 | UC-38–40, 81–85, 84 |
| F6 | UC-09–10, 44, 46, 65, 88–90 |

---

## P. Regras transversais

1. **Três origens:** `www` / `app` / `*.sites` — cookie só `app`.
2. **Host routing:** nunca tenant por path se houver custom domain.
3. **PSP cria conta paga;** free cria sem PSP.
4. **Publish assíncrono** sempre.
5. **Plano gates** na API, não só UI.
6. **Cloudflare** serve público; SQL é source of truth; KV cache.
7. **Lucro &gt; feature:** backlog se não ligar a Pro/Business/Agency.

Planejamento: **[plano-construcao.md](plano-construcao.md)** · receita: **[produto-e-receita.md](produto-e-receita.md)**.
