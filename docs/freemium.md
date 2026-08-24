# Freemium: canal de MRR, não produto principal

Free existe para **aquisição** e **prova**. Receita = Pro / Business / Agency. Ver **[produto-e-receita.md](produto-e-receita.md)**.

Nesta categoria o mecanismo que já converte é outro: **rodapé “Feito com X”** (clicável) + **URL no seu domínio** + **sem domínio próprio**. É o que Linktree e Carrd usam. Têm dois efeitos: o dono paga para parecer profissional; o visitante clica o selo e vira cadastro novo.

```mermaid
flowchart LR
  Visitante --> Pagina[bio free com selo]
  Pagina -->|"parece amador / quer domínio"| DonoPaga[dono faz upgrade]
  Pagina -->|clica o rodapé| Cadastro[visitante vira conta nova]
```

## O que sim e o que não

| Superfície | Free com selo? | Por quê |
|---|---|---|
| Bio | Sim — rodapé fino, ~12px, link para a landing | Job clássico da categoria; o próprio site é anúncio |
| Institucional / portfólio | Não | Selo numa página “empresa” humilha o cliente; você vira hosting grátis |
| Marca d’água diagonal por cima do conteúdo | Não | Visitante some; não diferencia de ferramenta tosca |

Institucional **só pago**. Selo lá só com permissão, como anúncio seu — não como paywall.

## O que de fato empurra o upgrade

Nesta ordem:

1. **Domínio próprio** (`bio.meunegocio.com`) — o paywall mais honesto da categoria.
2. Botão no editor **“remover rodapé”** → checkout. Não precisa cobrir a página.
3. **Analytics** de clique — dono de Instagram sente falta na 2ª semana.
4. O **9º link** (free para em 5–8).
5. **Export** zip do site — pago; reduz churn (“não prendo você”).
6. **QR + WhatsApp + embeds** — Pro; ver [concorrente-appsha.md](concorrente-appsha.md).
7. **Form/leads** — Business; upsell ARPU.

```mermaid
flowchart TB
  Free[Free: 5–8 links + selo + seu subdomínio]
  Free -->|quer bio.meunegocio.com| Pago
  Free -->|clica remover rodapé| Pago
  Free -->|quer saber o clique| Pago
  Free -->|9º link| Pago
  Pago[Pago: sem selo, CNAME, analytics, export, blocos Pro]
  Biz[Business: institucional, form, multi-página]
  Free --> Biz
```

## Desenho econômico

Free **fino** = margem preservada. Pausa 90d + zero suporte humano no free.

**Free:** bio · subdomínio · 5–8 links · 1 skin · selo · sem analytics/CNAME/export/form/institucional

**Pro:** sem selo · domínio · analytics · links ilimitados · embeds/galeria/QR · export

**Business:** institucional multi-página · SEO pack · form→lead · 2º site opcional

Preço pago não compete com Biofy R$ 12,90 — vende **profissionalismo + domínio + dados**.

## Conta honesta

Conversão típica de PLG sem marca grande: **2–5%** free → pago. A uns 3%, são ~**33 contas grátis para 1 de R$ 24,90**.

O free é canal, não receita. Infra de HTML estático aguenta milhares barato; atendimento e rebuild não. Por isso o free tem de ser auto-pausável e sem atendimento humano.

## O que não fazer

- Trial 14 dias full e depois pagar ou morrer — conversão ok, distribuição zero para quem ainda não te conhece.
- Free institucional de 4 páginas com selo.
- Forever-free com rebuild a cada save sem limite
- Cobrar para “tirar a marca” e ainda deixar o dono só no seu subdomínio — ele quer o domínio **dele**.
- Atender free no WhatsApp.

## Checklist

- [ ] Selo só no free da bio, uma linha no rodapé
- [ ] Sem marca d’água por cima do conteúdo
- [ ] Domínio próprio, analytics e export só no pago
- [ ] 5–8 links no free; o seguinte é paywall
- [ ] 90 dias inativo → HTML pausado
- [ ] Institucional só pago; selo opcional com permissão
- [ ] Preço pago não desce para a faixa Biofy R$ 12,90–16,90
