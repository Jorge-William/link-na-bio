# Landing Page — Pixel Art Bio Link

> Documentação de conhecimento acumulado durante o design e implementação da landing page demo do link-na-bio.

## Visão geral

A landing page demonstra o produto "link na bio" com identidade visual em **pixel art** e **cores modernas**. Ela vive em `apps/www/public/` e é servida pelo Cloudflare Worker definido em `apps/www/`.

**Domínio da plataforma:** `linkk.ae` — marketing em `www.linkk.ae`, app em `app.linkk.ae`, bios free em `{slug}.sites.linkk.ae`.

Existem **duas versões** preservadas para comparação:

| Versão | Arquivo | Descrição |
|--------|---------|-----------|
| **v1** | `apps/www/public/v1/index.html` | Design original "Pixelink" — autocontido (Tailwind via CDN + Press Start 2P). Hero com "Seu universo inteiro em um pixel", tribos em grid, social proof com depoimentos. |
| **v2** | `apps/www/public/index.html` + `styles.css` | Redesign com CSS custom, botões empilhados como em apps reais, fontes por tribo, rabiscos SVG, hero animado com celular rotativo. |

Cada versão tem um botão fixo no canto inferior direito para navegar para a outra.

---

## Decisões de design

### Botões empilhados (v2)
Em apps de link na bio reais (Linktree, Beacons, Taplink, Appsha), os botões ficam **empilhados em coluna** — um por linha, largura total, fáceis de tocar no celular. A v1 usava chips lado a lado (flex-wrap); a v2 corrigiu para `display: grid` em coluna (classe `.phone-links`).

### Diferenciação por tribo
Cada tribo muda **fonte, cor, raio de borda, contorno e sombra**:

| Tribo | Fonte | Estilo de botão | Paleta |
|-------|-------|-----------------|--------|
| **Gamer** | VT323 (monospace pixel) | Canto reto (2px), borda neon | Roxo escuro + lime neon |
| **Negócios** | Lexend | Pill (12px radius), borda-left azul | Azul corporativo + branco |
| **Reggae** | Baloo 2 | Pill total (999px), sombra dura | Verde, ouro, vermelho |
| **Rock** | Bebas Neue | Bloco reto (0 radius), sombra vermelha | Preto + vermelho |
| **Gótico** | UnifrakturCook | Arco ornamental (top-round), glow | Violeta + preto profundo |
| **Creator** | Syne | Assimétrico (14px 24px 14px 24px) | Cyan, pink, yellow, lime |

### Rabiscos (doodles)
SVGs inline em `data:` URIs posicionados com `position: absolute` dentro de cada `.scene`. Tipos: estrela (lime e pink), zigzag (coral e cyan), espiral (violet), pontos (pink), burst (cyan), seta curva (orange). Animações sutis: `twinkle` (escala + rotação), `spin-slow` (espiral).

### Hero animado (v2)
- Celular flutuando com `@keyframes float` (7s ease-in-out)
- Troca automática de tribo a cada 3.6s via JS (`setInterval`)
- Dots clicáveis abaixo do celular
- Pausa ao hover, reinicia ao sair
- Entrada em cascata com delays (.d1–.d4)
- Cursor piscando (`.caret`) no eyebrow
- Risco vermelho ondulado sob o título (SVG `::after` no `.hero-accent`)
- Tudo desligado sob `prefers-reduced-motion: reduce`

### Scroll reveal
`IntersectionObserver` com `threshold: 0.12` adiciona `.is-visible` em cards, boxes, planos e FAQs. Classe `.on-scroll` dá `opacity: 0` + `translateY(20px)` inicial, transicionando em 520ms.

---

## Estrutura CSS (v2)

O CSS usa **custom properties** (`:root`) e **zero frameworks**:

```
:root vars → reset → skip-link → header (.top) → botões (.btn) →
rabiscos (.dd) → layout (main, .section-copy) → hero →
celular (.phone, .phone-overlay, .phone-links, .pl) →
temas por tribo (.theme-*) → hero dots → marquee →
tribos (toolbar, carousel, filters) → features → showcase →
planos → faq → cta final → rodapé → alternador de versão →
animações (@keyframes) → responsivo (@media)
```

### Fontes carregadas
Inter (base), Space Mono (monospace labels), Syne (headings), VT323, Lexend, Baloo 2, Bebas Neue, UnifrakturCook, Source Sans 3 — via Google Fonts com `preconnect`.

---

## Pesquisa de concorrentes

Concorrentes analisados para features e inspiração visual:

- **Linktree** — referência de mercado, design genérico, gap de branding
- **Beacons** — bio como página/loja/agenda/funil
- **Taplink** — bom quando vira página, loja e funil
- **Cuttly** — foco em encurtador + bio
- **Appsha** (appsha.com) — smart profile para profissionais, booking + CRM + reviews. Inspirou o CTA lime no topo e o estilo de pílulas com contorno.

Referências visuais usadas:
- [Lynku.id SaaS Bio Link Dashboard](https://dribbble.com/shots/23355011)
- [Leadrr AI Bio Link website](https://dribbble.com/shots/26438548)
- [Easy Bio AI Bio Link Landing Page](https://dribbble.com/shots/25291307)
- [Web design style with pixels (Medium)](https://medium.com/design-bootcamp/web-design-style-website-with-pixels-757e41ac447e)
- Velvetyne Terminal Grotesque (referência tipográfica)

---

## Acessibilidade

- Skip link (`a.skip-link`) para pular ao conteúdo
- `aria-label` em navs, listas e botões
- `aria-live="polite"` no status do carrossel
- `role="tablist"` + `role="tab"` + `aria-selected` nos filtros e dots
- `prefers-reduced-motion: reduce` desabilita todas as animações
- `aria-hidden="true"` em SVGs decorativos
- Foco visível com `outline` em `:focus-visible`
- Contraste testado entre texto e fundos

---

## Cópia local standalone

Uma cópia existe em `C:\Users\XPS001\Desktop\biolinkpixel\` para testes locais via `file://`. A diferença é que o `<link>` de CSS usa `href="./styles.css"` (relativo) em vez de `/styles.css` (absoluto). Essa pasta **não é versionada** — é apenas conveniência local.

Para servir ambas as versões com URLs reais:
```bash
cd apps/www/public
python -m http.server 8080 --bind 127.0.0.1
# v2: http://localhost:8080/
# v1: http://localhost:8080/v1/
```

---

## Próximos passos sugeridos

1. **Mesclar o melhor da v1 na v2** — o usuário gostou de elementos da v1 (peso do lettering, pílulas de prova social, nome "Pixelink"). Comparar lado a lado e decidir o que migrar.
2. **Animação do hero** — avaliar se a rotação automática de tribos é suficiente ou se precisa de mais "vida" (parallax, partículas, transições mais elaboradas).
3. **Mobile polish** — testar em dispositivos reais, ajustar carousel touch e navbar colapsável.
4. **Instalar dependências do monorepo** — `npm install` na raiz para habilitar `tsc`, `wrangler dev` e deploy.
5. **Deploy no Cloudflare** — `npm run deploy -w @linknabio/www` para publicar a landing em produção.

---

*Última atualização: 2026-09-03*
