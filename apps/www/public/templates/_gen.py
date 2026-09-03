# Generates one HTML file per official Linktree gallery template
# (names collected from linktr.ee/s/templates and category pages).
from pathlib import Path

OUT = Path(__file__).resolve().parent

ICONS = {
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14.2 3h3.1c.2 1.6 1.1 3 2.4 3.9 1 .7 2.2 1 3.3 1.1v3.2c-1.5 0-3-.4-4.3-1.2v6.8c0 3.7-3 6.7-6.7 6.7S5.3 20.5 5.3 16.8 8.3 10 12 10c.4 0 .8 0 1.2.1V13c-.4-.1-.8-.2-1.2-.2-2 0-3.6 1.6-3.6 3.6S10 20 12 20s3.6-1.6 3.6-3.6V3z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10.5 9l5 3-5 3V9z" fill="currentColor"/></svg>',
    "x": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h4.2l4.1 5.6L16.8 4H20l-6.3 8.2L20.4 20h-4.2l-4.5-6.1L7.2 20H4l6.7-8.7L4 4z"/></svg>',
    "spotify": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7.2 10.2c3.2-1.2 6.6-.9 9.6.6M7.6 13c2.6-1 5.4-.8 7.8.5M8 15.8c1.9-.7 4-.6 5.8.4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "twitch": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M5 4h14v10l-4 4H11l-3 3v-3H5V4z"/><path d="M11 8v5M15 8v5" stroke="currentColor" stroke-width="1.8"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="8" cy="10" r="1.3" fill="currentColor"/><path d="M8 12.2V18M11.2 18v-3.6c0-1.5 2.6-1.6 2.6 0V18M16.4 18v-4.2c0-2.6-3.2-2.5-4 0" stroke="currentColor" stroke-width="1.6"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 8h3V4.8h-3C11.6 4.8 10 6.5 10 8.8V11H7.5v3.2H10V20h3.4v-5.8h2.8L16.8 11H13.4V8.8c0-.5.4-.8.6-.8z"/></svg>',
    "pinterest": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10.4 19.2c.4-1.8.7-3.5 1-5.2-.5-.1-1.2.6-1.4 1.3-.8-1.4-.2-4 1.6-4.2 2.2-.3 3.3 2 2.7 4-.4 1.5-1.2 2.9-.4 3.8 1.8-1.5 2.8-4.3 2.4-6.7-.4-2.8-3.2-4.1-5.8-3.2-2.8 1-3.5 4.2-2.2 6.1" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>',
    "discord": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M7 18c-2-.8-3.2-2.4-3.8-4.6C4 9 6 6.4 8.4 5.6l.8 1.6c1.6-.5 3.2-.5 4.8 0l.8-1.6c2.4.8 4.4 3.4 5.2 7.8-.6 2.2-1.8 3.8-3.8 4.6l-1.2-1.6c.8-.2 1.5-.6 2.1-1.1-2 .9-4.2 1.3-6.5 1.3s-4.5-.4-6.5-1.3c.6.5 1.3.9 2.1 1.1L7 18z"/><circle cx="9.2" cy="12.2" r="1.2" fill="currentColor"/><circle cx="14.8" cy="12.2" r="1.2" fill="currentColor"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M6.4 18.2 5 21l3-1.2A9 9 0 1 0 6.4 18.2z"/><path d="M8.6 9.6c.2 2 2.4 4.4 4.4 5.2l1.4-.6 1.4 1.4-.5.8c-2.3 0-5.6-2.2-6.7-5.2z" fill="currentColor"/></svg>',
    "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 8l8 6 8-6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>',
    "web": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>',
    "snapchat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4c3.4 0 5.4 2.4 5.4 5.6 0 1.4.6 2.1 1.6 2.6-.8.4-1.2 1.1-.6 2 .8.2 1.4.6 2 1.3-1.6.4-2.3 1.3-2.3 2.2 0 .8.8 1.3 1.5 1.6-.8.6-2.4 1-4.1.6-.5.6-1.6 1.1-3.5 1.1s-3-.5-3.5-1.1c-1.7.4-3.3 0-4.1-.6.7-.3 1.5-.8 1.5-1.6 0-.9-.7-1.8-2.3-2.2.6-.7 1.2-1.1 2-1.3.6-.9.2-1.6-.6-2 1-.5 1.6-1.2 1.6-2.6C6.6 6.4 8.6 4 12 4z" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>',
}

FONTS_HREF = (
    "https://fonts.googleapis.com/css2?"
    "family=Anton&family=Archivo+Black&family=Bebas+Neue&family=Bodoni+Moda:opsz,wght@6..96,600;6..96,800"
    "&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800"
    "&family=Caveat:wght@700&family=Cormorant+Garamond:ital,wght@0,600;1,600;1,700"
    "&family=DM+Serif+Display:ital@0;1&family=Fjalla+One"
    "&family=Fraunces:ital,opsz,wght@0,9..144,700;1,9..144,700"
    "&family=IBM+Plex+Mono:wght@500;700&family=Instrument+Serif:ital@0;1"
    "&family=Inter:wght@400;500;600;700;800&family=Lexend:wght@500;700"
    "&family=Libre+Baskerville:ital,wght@0,700;1,400"
    "&family=Oswald:wght@500;700&family=Outfit:wght@500;700;800"
    "&family=Pacifico&family=Playfair+Display:ital,wght@0,700;1,700"
    "&family=Press+Start+2P&family=Space+Grotesk:wght@500;700"
    "&family=Syne:wght@700;800&family=UnifrakturCook:wght@700"
    "&family=VT323&display=swap"
)

# Official names from linktr.ee/s/templates + category pages.
# Each profile changes name type, handle placement, avatar treatment and social row.
TEMPLATES = [
    dict(slug="artemis", official="Artemis", cat="small-business", display="Sunrise Juice", handle="@sunrise.juice", role="bar de sucos · receitas · lojas",
         avatar="https://images.unsplash.com/photo-1623065428148-80a3c6ea0a8d?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=800&q=80",
         name_font="'Bricolage Grotesque',sans-serif", handle_pos="under-name", header="cover-overlap",
         bg="linear-gradient(180deg,#fff4c8,#ff8a3d)", ink="#3a1408", btn_bg="#fff", btn_ink="#3a1408", btn_r="28px",
         socials=["instagram","tiktok","whatsapp","web"], links=["Cardápio de sucos","Receitas da semana","Encontre uma loja","Peça pelo app"],
         note="Sucos e smoothie bar — capa laranja, nome sobre a foto."),
    dict(slug="balcombe", official="Balcombe", cat="influencer-and-creator", display="Maya Costa", handle="@maya.wanders", role="travel diary · 42 países",
         avatar="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
         name_font="'Pacifico',cursive", handle_pos="above-name", header="name-first-no-avatar-top",
         bg="linear-gradient(180deg,#c8f4ff,#fff8dc)", ink="#0b3a4a", btn_bg="#0b3a4a", btn_ink="#fff8dc", btn_r="999px",
         socials=["instagram","youtube","tiktok","pinterest"], links=["Guia Bali 2026","Mapa dos 42 países","Newsletter de rotas","Loja de prints"],
         note="Travel — handle acima, nome em script, avatar pequeno no rodapé do header."),
    dict(slug="boultont", official="Boultont", cat="social-media", display="BOULTONT", handle="@studio.boultont", role="conteúdo · campanhas · reels",
         avatar="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Anton',sans-serif", handle_pos="right-of-name", header="wordmark-left",
         bg="#111", ink="#f4f1ea", btn_bg="#f4f1ea", btn_ink="#111", btn_r="4px",
         socials=["instagram","tiktok","x","email"], links=["Media kit","Último reel","Briefing de marca","Contato comercial"],
         note="Social studio — wordmark enorme à esquerda, handle ao lado."),
    dict(slug="bourke", official="Bourke", cat="health-and-fitness", display="ALEX BOURKE", handle="@bourke.moves", role="coach · HIIT · run club",
         avatar="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=800&q=80",
         name_font="'Oswald',sans-serif", handle_pos="badge-on-avatar", header="jersey",
         bg="#0e1a14", ink="#e8ff6b", btn_bg="#e8ff6b", btn_ink="#0e1a14", btn_r="8px",
         socials=["instagram","youtube","tiktok","spotify"], links=["Plano 6 semanas","Run club SP","App de treino","Marca de suplemento"],
         note="Fitness — nome tipo camisa, handle em badge no avatar."),
    dict(slug="constance", official="Constance", cat="sports", display="CONSTANCE", handle="@constance.sk8", role="pro skater · parks · playlist",
         avatar="https://images.unsplash.com/photo-1564982752979-3f7bc97460bb?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1564419320461-6870880221ad?auto=format&fit=crop&w=800&q=80",
         name_font="'Archivo Black',sans-serif", handle_pos="footer-of-hero", header="poster-stack",
         bg="#1a1a1a", ink="#fff", btn_bg="transparent", btn_ink="#fff", btn_r="0",
         socials=["instagram","tiktok","youtube","spotify"], links=["Melhores pistas do mundo","Playlist pra andar","Video part 2026","Patrocinadores"],
         note="Skate — nome em stack de cartaz, handle no rodapé do hero."),
    dict(slug="coromandel", official="Coromandel", cat="marketing", display="Coromandel", handle="@coro.studio", role="brand studio · growth",
         avatar="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Instrument Serif',serif", handle_pos="tiny-top", header="editorial-serif",
         bg="#f3efe6", ink="#1c1914", btn_bg="#1c1914", btn_ink="#f3efe6", btn_r="2px",
         socials=["linkedin","instagram","web","email"], links=["Cases 2026","Deck comercial","Newsletter de growth","Agendar briefing"],
         note="Marketing — serif editorial, handle minúsculo no topo."),
    dict(slug="crombie", official="Crombie", cat="influencer-and-creator", display="Nia Crombie", handle="@nia.crombie", role="justiça social · essays",
         avatar="https://images.unsplash.com/photo-1531123897727-8f129e1688ce?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Libre Baskerville',serif", handle_pos="italic-under", header="split-card",
         bg="#f7f1e6", ink="#2b2118", btn_bg="#c45c26", btn_ink="#fff", btn_r="14px",
         socials=["instagram","x","youtube","email"], links=["Último ensaio","Petição da semana","Livros que indico","Apoie o trabalho"],
         note="Ativismo — avatar à esquerda, nome serif à direita."),
    dict(slug="gordon", official="Gordon", cat="small-business", display="Gordon Shop", handle="@gordon.earth", role="clima · loja · blog",
         avatar="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=800&q=80",
         name_font="'Fraunces',serif", handle_pos="center-under-avatar", header="sunny-classic",
         bg="linear-gradient(180deg,#fff3a1,#7ec8a3)", ink="#16331f", btn_bg="#16331f", btn_ink="#fff3a1", btn_r="18px",
         socials=["instagram","pinterest","web","email"], links=["Loja sustentável","Blog climático","Formulário de contato","Coleção primavera"],
         note="Ecom clima — layout clássico mas nome em Fraunces grande."),
    dict(slug="guildford-sport", official="Guildford Sport", cat="sports", display="GUILDFORD", handle="@guildford.sc", role="clube · ingressos · tv",
         avatar="https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=800&q=80",
         name_font="'Fjalla One',sans-serif", handle_pos="below-crest", header="crest-center",
         bg="#0b1f4d", ink="#fff", btn_bg="#e10600", btn_ink="#fff", btn_r="6px",
         socials=["instagram","youtube","x","tiktok"], links=["Comprar ingresso","Tabela do campeonato","Loja oficial","Guildford TV"],
         note="Clube — brasão/avatar no centro, nome tipo escudo."),
    dict(slug="hanna", official="Hanna", cat="music", display="hanna.", handle="@hanna.songs", role="indie folk · singles",
         avatar="https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'DM Serif Display',serif", handle_pos="side-caption", header="lowercase-serif",
         bg="#f8e8ef", ink="#3b1020", btn_bg="#3b1020", btn_ink="#f8e8ef", btn_r="999px",
         socials=["spotify","instagram","youtube","tiktok"], links=["Novo single","Clipe no YouTube","Datas da turnê","Vinyl pré-venda"],
         note="Música indie — nome em caixa baixa com ponto, handle na lateral."),
    dict(slug="hay", official="Hay", cat="fashion", display="HAY", handle="@hay.atelier", role="lookbook · drop mensal",
         avatar="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=800&q=80",
         name_font="'Bodoni Moda',serif", handle_pos="vertical-left", header="fashion-masthead",
         bg="#efe6d9", ink="#111", btn_bg="#111", btn_ink="#efe6d9", btn_r="0",
         socials=["instagram","pinterest","tiktok","web"], links=["Lookbook SS26","Lista de espera","Atelier visits","Editorial"],
         note="Fashion — nome Bodoni enorme, handle vertical na esquerda."),
    dict(slug="healeys", official="Healeys", cat="music", display="The Healeys", handle="@thehealeys", role="banda · merch · setlist",
         avatar="https://images.unsplash.com/photo-1501386761578-eac5c94b800a?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=800&q=80",
         name_font="'Bebas Neue',sans-serif", handle_pos="stamp", header="band-stamp",
         bg="#120c0c", ink="#f3d27a", btn_bg="#f3d27a", btn_ink="#120c0c", btn_r="0",
         socials=["spotify","youtube","instagram","tiktok"], links=["Tickets","Merch store","Setlist oficial","Clipe novo"],
         note="Banda — nome condensed, handle como carimbo."),
    dict(slug="heape", official="Heape", cat="small-business", display="Heape Studio", handle="@heape.plants", role="horticultura · design",
         avatar="https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Outfit',sans-serif", handle_pos="chip-row", header="color-blocks",
         bg="#d8f27d", ink="#16300a", btn_bg="#16300a", btn_ink="#d8f27d", btn_r="12px",
         socials=["instagram","pinterest","whatsapp","web"], links=["Loja de plantas","Ferramentas favoritas","Como entrar em contato","Workshop"],
         note="Horticultura — blocos de cor, handle em chip."),
    dict(slug="heffernan", official="Heffernan", cat="influencer-and-creator", display="Leo Heffernan", handle="@leo.heff", role="daily vlogs · collabs",
         avatar="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Space Grotesk',sans-serif", handle_pos="between-avatar-name", header="creator-stack",
         bg="#101014", ink="#fff", btn_bg="#7c5cff", btn_ink="#fff", btn_r="16px",
         socials=["tiktok","instagram","youtube","snapchat"], links=["Vlog de hoje","Collab form","Amazon storefront","Discord"],
         note="Creator — avatar, handle, depois o nome em caixa alta."),
    dict(slug="iris", official="Iris", cat="influencer-and-creator", display="Iris Vale", handle="@iris.vale", role="filosofia · palestras · blog",
         avatar="https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Cormorant Garamond',serif", handle_pos="ornament-line", header="thinker",
         bg="#1b1530", ink="#f0e6ff", btn_bg="transparent", btn_ink="#f0e6ff", btn_r="999px",
         socials=["youtube","instagram","x","email"], links=["Próxima palestra","Blog","Site principal","Lista de leitura"],
         note="Pensadora — nome itálico grande, handle entre filetes."),
    dict(slug="knox", official="Knox", cat="influencer-and-creator", display="Knox Solar", handle="@knox.solar", role="design solar · talks",
         avatar="https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Syne',sans-serif", handle_pos="mono-top-right", header="tech-split",
         bg="#f6f3ea", ink="#1a1408", btn_bg="#f4b400", btn_ink="#1a1408", btn_r="10px",
         socials=["linkedin","instagram","youtube","web"], links=["Afiliados solares","Talk VidCon","Portfólio de telhados","Contato"],
         note="Solar — nome Syne à esquerda, handle mono no canto."),
    dict(slug="lane", official="Lane", cat="influencer-and-creator", display="LANE", handle="@lane.live", role="streamer · merch · twitch",
         avatar="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=800&q=80",
         name_font="'Press Start 2P',monospace", handle_pos="neon-under", header="gamer-neon",
         bg="#0a0618", ink="#d7ff3f", btn_bg="#1b1140", btn_ink="#d7ff3f", btn_r="2px",
         socials=["twitch","youtube","discord","tiktok"], links=["Watch live","Loja de merch","Setup tour","Discord do clan"],
         note="Gamer — nome pixel, handle neon abaixo."),
    dict(slug="lingham", official="Lingham", cat="sports", display="Lingham", handle="@lingham.fit", role="performance · recovery",
         avatar="https://images.unsplash.com/photo-1571019614242-c162c256452d?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Outfit',sans-serif", handle_pos="overline", header="sport-minimal",
         bg="#eef2f5", ink="#0d1b2a", btn_bg="#0d1b2a", btn_ink="#fff", btn_r="22px",
         socials=["instagram","youtube","tiktok","web"], links=["Programa de recovery","Loja de kits","Agenda de aulas","App"],
         note="Esporte clean — handle com overline, nome médio-grande."),
    dict(slug="merlin-biz", official="Merlin Biz", cat="small-business", display="Merlin & Co.", handle="@merlin.biz", role="consultoria · board",
         avatar="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Lexend',sans-serif", handle_pos="business-card", header="biz-card",
         bg="#f4f6f8", ink="#12233d", btn_bg="#fff", btn_ink="#12233d", btn_r="12px",
         socials=["linkedin","email","web","whatsapp"], links=["Agendar call","Pitch deck","LinkedIn","Newsletter"],
         note="Negócios — cartão: cargo, nome, handle no rodapé do header."),
    dict(slug="merriman", official="Merriman", cat="health-and-fitness", display="Merriman Lab", handle="@merriman.lab", role="lab de movimento",
         avatar="https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'IBM Plex Mono',monospace", handle_pos="index-left", header="lab-index",
         bg="#f2efe6", ink="#222", btn_bg="#222", btn_ink="#f2efe6", btn_r="0",
         socials=["instagram","youtube","web","email"], links=["Método","Turmas abertas","Pesquisa","Contato"],
         note="Lab — nome mono indexado, handle como 01 / @."),
    dict(slug="meyers", official="Meyers", cat="small-business", display="Meyers", handle="@meyers.home", role="home goods · loja",
         avatar="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Playfair Display',serif", handle_pos="small-center", header="boutique",
         bg="#f8f1e7", ink="#4a3424", btn_bg="#4a3424", btn_ink="#f8f1e7", btn_r="8px",
         socials=["instagram","pinterest","web","whatsapp"], links=["Coleção casa","Loja online","Showroom","WhatsApp"],
         note="Casa — nome serif central, handle discreto."),
    dict(slug="pender", official="Pender", cat="small-business", display="PENDER", handle="@pender.co", role="studio criativo",
         avatar="https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Archivo Black',sans-serif", handle_pos="slash", header="slash-name",
         bg="#fff", ink="#111", btn_bg="#111", btn_ink="#fff", btn_r="0",
         socials=["instagram","linkedin","web","email"], links=["Work","About","Careers","Contact"],
         note="Studio — PENDER / @pender.co na mesma linha."),
    dict(slug="presgrave", official="Presgrave", cat="marketing", display="Presgrave", handle="@presgrave", role="growth partner",
         avatar="https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Space Grotesk',sans-serif", handle_pos="dot-separator", header="logo-lockup",
         bg="#0f1720", ink="#d6ffe6", btn_bg="#d6ffe6", btn_ink="#0f1720", btn_r="6px",
         socials=["linkedin","x","web","email"], links=["Oferta de growth","Calendário","Cases","Contratar"],
         note="Marketing dark — lockup com ponto entre nome e handle."),
    dict(slug="stubbs", official="Stubbs", cat="small-business", display="Stubbs Coffee", handle="@stubbs.coffee", role="torrefação · assinatura",
         avatar="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Fraunces',serif", handle_pos="under-circle", header="circle-badge",
         bg="#3b2416", ink="#f3e2c8", btn_bg="#f3e2c8", btn_ink="#3b2416", btn_r="999px",
         socials=["instagram","whatsapp","web","tiktok"], links=["Assinar café","Cardápio da semana","Nossa história","Onde encontrar"],
         note="Café — nome dentro/abaixo de selo circular."),
    dict(slug="sugden", official="Sugden", cat="small-business", display="Sugden", handle="@sugden.works", role="oficina · encomendas",
         avatar="https://images.unsplash.com/photo-1504148455328-c376907d081c?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Oswald',sans-serif", handle_pos="workshop-tag", header="industrial",
         bg="#d9d3c5", ink="#1c1c1c", btn_bg="#1c1c1c", btn_ink="#d9d3c5", btn_r="2px",
         socials=["instagram","facebook","whatsapp","web"], links=["Encomendar","Catálogo","Oficina aberta","WhatsApp"],
         note="Oficina — nome industrial, handle em tag."),
    dict(slug="warburton", official="Warburton", cat="small-business", display="Warburton", handle="@warburton.bakery", role="padaria · encomendas",
         avatar="https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1486427944299-d1955d23e34d?auto=format&fit=crop&w=800&q=80",
         name_font="'Caveat',cursive", handle_pos="printed-small", header="bakery-ticket",
         bg="#f7efe4", ink="#4a2c14", btn_bg="#fff", btn_ink="#4a2c14", btn_r="20px",
         socials=["instagram","whatsapp","facebook","web"], links=["Cardápio do dia","Encomendas","Endereços","Nossa história"],
         note="Padaria — nome manuscrito, handle tipo impresso de ticket."),
    dict(slug="louden", official="Louden", cat="marketing", display="Louden", handle="@louden.media", role="media house",
         avatar="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Anton',sans-serif", handle_pos="bottom-right", header="billboard",
         bg="#ff3d00", ink="#fff", btn_bg="#111", btn_ink="#fff", btn_r="0",
         socials=["instagram","tiktok","youtube","linkedin"], links=["Reel pack","Media kit","Briefing","Reel awards"],
         note="Media — nome outdoor, handle canto inferior direito."),
    dict(slug="merlin", official="Merlin", cat="health-and-fitness", display="Merlin", handle="@merlin.fit", role="treino · youtube · looks",
         avatar="https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Anton',sans-serif", handle_pos="center-caps", header="fit-hero-name",
         bg="linear-gradient(180deg,#1b1b1b,#3d3d3d)", ink="#fff", btn_bg="#fff", btn_ink="#111", btn_r="999px",
         socials=["youtube","instagram","pinterest","tiktok"], links=["Canal YouTube","Pinterest de looks","Programa 12 semanas","Marca"],
         note="Fitness influencer — NOME gigante no meio, handle em caps no centro."),
    dict(slug="oliver", official="Oliver", cat="influencer-and-creator", display="oliver chen", handle="@oliver", role="foto · zine · prints",
         avatar="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Instrument Serif',serif", handle_pos="only-at", header="quiet-photo",
         bg="#ece7df", ink="#2a241c", btn_bg="#2a241c", btn_ink="#ece7df", btn_r="4px",
         socials=["instagram","web","email","pinterest"], links=["Zine 04","Print shop","Comissões","Sobre"],
         note="Fotógrafo — nome itálico pequeno-grande, handle só @oliver."),
    dict(slug="paynes", official="Paynes", cat="influencer-and-creator", display="PAYNES", handle="@paynes.tv", role="host · clips · live",
         avatar="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Bebas Neue',sans-serif", handle_pos="tv-bug", header="broadcast",
         bg="#0c0c12", ink="#f5f5f5", btn_bg="#ff2d55", btn_ink="#fff", btn_r="8px",
         socials=["youtube","twitch","instagram","x"], links=["Último episódio","Clips","Live schedule","Patreon"],
         note="Host — nome tipo TV, handle como bug de canal."),
    dict(slug="ridgway", official="Ridgway", cat="influencer-and-creator", display="Ridgway", handle="@ridgway", role="outdoor · trails",
         avatar="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
         name_font="'Bricolage Grotesque',sans-serif", handle_pos="on-cover", header="landscape-name",
         bg="#e8f0e6", ink="#1d2b1a", btn_bg="#1d2b1a", btn_ink="#e8f0e6", btn_r="14px",
         socials=["instagram","youtube","tiktok","web"], links=["Trilha da semana","Guia de equipamento","Patreon maps","Contato"],
         note="Outdoor — nome sobre a paisagem, handle na capa."),
    dict(slug="russell", official="Russell", cat="influencer-and-creator", display="RUSSELL", handle="@russell.notes", role="escrita · newsletter",
         avatar="https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'IBM Plex Mono',monospace", handle_pos="byline", header="byline-block",
         bg="#faf7f0", ink="#111", btn_bg="#111", btn_ink="#faf7f0", btn_r="2px",
         socials=["x","email","web","instagram"], links=["Newsletter","Último texto","Livro","Arquivo"],
         note="Escrita — byline 'notes by' + nome mono."),
    dict(slug="middleton", official="Middleton", cat="fashion", display="Middleton", handle="@middleton.arc", role="archive fashion",
         avatar="https://images.unsplash.com/photo-1529139574466-a303027c1d8b?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'UnifrakturCook',serif", handle_pos="modern-under-gothic", header="gothic-modern",
         bg="#140f16", ink="#e8d7ff", btn_bg="#2a2033", btn_ink="#e8d7ff", btn_r="999px 999px 8px 8px",
         socials=["instagram","pinterest","tiktok","web"], links=["Lookbook after dark","Atelier","Peças únicas","Editorial"],
         note="Fashion gótico — nome blackletter, handle sans moderno."),
    dict(slug="music-14", official="Music 14", cat="music", display="MUSIC14", handle="@music14.dj", role="dj · boiler room · booking",
         avatar="https://images.unsplash.com/photo-1571266028243-d220c6a68e4c?auto=format&fit=crop&w=400&q=80",
         cover="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=800&q=80",
         name_font="'Syne',sans-serif", handle_pos="mix-tag", header="dj-gradient",
         bg="linear-gradient(180deg,#1a0033,#4b006e,#0d0d16)", ink="#fff", btn_bg="rgba(255,255,255,.12)", btn_ink="#fff", btn_r="999px",
         socials=["spotify","instagram","youtube","email"], links=["Boiler Room set","Setup de DJ","Comprar o mesmo kit","Booking"],
         note="DJ — gradient escuro, nome tracking largo, handle tipo tag de mix."),
    dict(slug="platypus", official="Platypus", cat="music", display="platypus", handle="@platypus.fm", role="radio show · mixes",
         avatar="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'VT323',monospace", handle_pos="fm-freq", header="radio",
         bg="#11180f", ink="#9dff6a", btn_bg="#9dff6a", btn_ink="#11180f", btn_r="4px",
         socials=["spotify","instagram","youtube","web"], links=["Ouça o programa","Arquivo de mixes","Convidados","Ao vivo"],
         note="Rádio — nome terminal, handle como frequência FM."),
    dict(slug="rutledge", official="Rutledge", cat="music", display="Rutledge", handle="@rutledge.raw", role="alt rock",
         avatar="https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Oswald',sans-serif", handle_pos="boxed", header="raw-box",
         bg="#f2efe8", ink="#111", btn_bg="#111", btn_ink="#f2efe8", btn_r="0",
         socials=["spotify","youtube","instagram","tiktok"], links=["Álbum novo","Ingressos","Merch","Discord da cena"],
         note="Alt rock — nome em caixa, handle boxed."),
    dict(slug="sampson", official="Sampson", cat="music", display="SAMPSON", handle="@sampson.wav", role="producer · beats",
         avatar="https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Space Grotesk',sans-serif", handle_pos="wav-ext", header="producer",
         bg="#0e0e12", ink="#7ef0ff", btn_bg="#7ef0ff", btn_ink="#0e0e12", btn_r="10px",
         socials=["spotify","youtube","instagram","email"], links=["Beat tape","Licensing","Pack de samples","Contato"],
         note="Producer — nome + extensão .wav no handle."),
    dict(slug="singers", official="Singers", cat="music", display="the singers", handle="@the.singers", role="vocal group",
         avatar="https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Playfair Display',serif", handle_pos="centered-script-pair", header="choir",
         bg="#241820", ink="#f6e6c8", btn_bg="#f6e6c8", btn_ink="#241820", btn_r="999px",
         socials=["spotify","youtube","instagram","facebook"], links=["Álbum ao vivo","Ingressos","Ensaios abertos","Contato"],
         note="Vocal — nome itálico central, handle logo abaixo em tracking."),
    dict(slug="somerset", official="Somerset", cat="music", display="Somerset", handle="@somerset.am", role="americana · live",
         avatar="https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Libre Baskerville',serif", handle_pos="ampersand", header="americana",
         bg="#efe4cf", ink="#3a2614", btn_bg="#3a2614", btn_ink="#efe4cf", btn_r="6px",
         socials=["spotify","instagram","youtube","facebook"], links=["Live sessions","Tour","Vinyl","Patreon"],
         note="Americana — Somerset & @somerset.am."),
    dict(slug="turner", official="Turner", cat="music", display="TURNER", handle="@turner.tour", role="solo tour",
         avatar="https://images.unsplash.com/photo-1521335629791-ce4aec67dd47?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Bebas Neue',sans-serif", handle_pos="tour-line", header="tour-poster",
         bg="#111", ink="#f2c14e", btn_bg="#f2c14e", btn_ink="#111", btn_r="0",
         socials=["spotify","instagram","youtube","tiktok"], links=["Datas da tour","Ingressos","Merch","Setlist"],
         note="Tour poster — nome faixa, handle 'on tour'."),
    dict(slug="smythe-sports", official="Smythe Sports", cat="sports", display="SMYTHE", handle="@smythe.tricks", role="trickshots · time · merch",
         avatar="https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Anton',sans-serif", handle_pos="scoreboard", header="scoreboard",
         bg="#083318", ink="#f4ff54", btn_bg="#f4ff54", btn_ink="#083318", btn_r="4px",
         socials=["youtube","instagram","tiktok","web"], links=["Trickshots","Site do time","Loja de merch","Agenda"],
         note="Esportes — nome tipo placar, handle como marcador."),
    dict(slug="mitre", official="Mitre", cat="sports", display="MITRE", handle="@mitre.club", role="clube amador",
         avatar="https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Fjalla One',sans-serif", handle_pos="kit-number", header="kit",
         bg="#f4f4f4", ink="#0a1a4a", btn_bg="#0a1a4a", btn_ink="#fff", btn_r="8px",
         socials=["instagram","facebook","youtube","web"], links=["Tabela","Sócio torcedor","Loja","Ingressos"],
         note="Clube amador — número 07 + nome, handle como dorsal."),
    dict(slug="star", official="Star", cat="influencer-and-creator", display="STAR", handle="@star.xyz", role="web3 · portfolio · store",
         avatar="https://images.unsplash.com/photo-1639762681485-074b7f938ba0?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Syne',sans-serif", handle_pos="wallet-chip", header="web3",
         bg="#07070c", ink="#e8e8ff", btn_bg="#6d5efc", btn_ink="#fff", btn_r="12px",
         socials=["x","discord","youtube","web"], links=["Portfólio web3","Vídeos para iniciantes","Loja","Comunidade"],
         note="Web3 — nome geométrico, handle tipo chip de wallet."),
    dict(slug="smythe", official="Smythe", cat="sports", display="Smythe", handle="@smythe", role="athlete brand",
         avatar="https://images.unsplash.com/photo-1517649763962-0c623066027c?auto=format&fit=crop&w=400&q=80",
         cover="",
         name_font="'Oswald',sans-serif", handle_pos="underline-handle", header="athlete-brand",
         bg="#101010", ink="#fff", btn_bg="#fff", btn_ink="#101010", btn_r="999px",
         socials=["instagram","tiktok","youtube","web"], links=["Highlight reel","Contratos","Loja","Contato"],
         note="Athlete brand — nome underline, handle sublinhado."),
]


def social_row(keys, cls="socials"):
    items = []
    for k in keys:
        items.append(
            f'<a class="soc" href="#" aria-label="{k}">{ICONS[k]}</a>'
        )
    return f'<nav class="{cls}" aria-label="redes sociais">{"".join(items)}</nav>'


def buttons(links, t):
    return "".join(f'<a class="link-btn" href="#">{label}</a>' for label in links)


def header_html(t):
    av = t["avatar"]
    cover = t.get("cover") or ""
    name = t["display"]
    handle = t["handle"]
    role = t["role"]
    socials = social_row(t["socials"])
    h = t["header"]

    if h == "cover-overlap":
        return f'''
        <div class="cover" style="background-image:url('{cover}')"></div>
        <header class="hdr overlap">
          <img class="av av-lg ring" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "name-first-no-avatar-top":
        return f'''
        <header class="hdr name-first">
          <p class="hd tiny">{handle}</p>
          <h1 class="nm script">{name}</h1>
          <p class="role">{role}</p>
          {socials}
          <img class="av av-sm" src="{av}" alt="{name}">
        </header>'''
    if h == "wordmark-left":
        return f'''
        <header class="hdr wordmark">
          <div>
            <h1 class="nm huge">{name}</h1>
            <p class="hd inline">{handle}</p>
          </div>
          <img class="av av-sq" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "jersey":
        return f'''
        <header class="hdr jersey">
          <div class="av-wrap">
            <img class="av av-md" src="{av}" alt="{name}">
            <span class="hd badge">{handle}</span>
          </div>
          <p class="role caps">nº 09</p>
          <h1 class="nm jersey-nm">{name}</h1>
          {socials}
        </header>'''
    if h == "poster-stack":
        return f'''
        <div class="cover tall" style="background-image:url('{cover}')">
          <p class="hd on-cover">{handle}</p>
        </div>
        <header class="hdr poster">
          <h1 class="nm stack">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "editorial-serif":
        return f'''
        <header class="hdr editorial">
          <p class="hd micro">{handle}</p>
          <h1 class="nm">{name}</h1>
          <p class="role">{role}</p>
          <img class="av av-wide" src="{av}" alt="{name}">
          {socials}
        </header>'''
    if h == "split-card":
        return f'''
        <header class="hdr split">
          <img class="av av-md" src="{av}" alt="{name}">
          <div>
            <h1 class="nm">{name}</h1>
            <p class="hd italic">{handle}</p>
            <p class="role">{role}</p>
          </div>
          {socials}
        </header>'''
    if h == "sunny-classic":
        return f'''
        <header class="hdr classic">
          <img class="av av-lg" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "crest-center":
        return f'''
        <header class="hdr crest">
          <img class="av av-crest" src="{av}" alt="{name}">
          <p class="hd">{handle}</p>
          <h1 class="nm">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "lowercase-serif":
        return f'''
        <header class="hdr side-cap">
          <img class="av av-md roundish" src="{av}" alt="{name}">
          <div class="pair">
            <h1 class="nm">{name}</h1>
            <p class="hd side">{handle}</p>
          </div>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "fashion-masthead":
        return f'''
        <header class="hdr masthead">
          <p class="hd vert">{handle}</p>
          <h1 class="nm fashion">{name}</h1>
          <img class="av av-rect" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "band-stamp":
        return f'''
        <header class="hdr stamp">
          <img class="av av-wide" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd stamp-hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "color-blocks":
        return f'''
        <header class="hdr blocks">
          <div class="block-row">
            <img class="av av-md" src="{av}" alt="{name}">
            <h1 class="nm">{name}</h1>
          </div>
          <p class="hd chip">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "creator-stack":
        return f'''
        <header class="hdr creator">
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="hd">{handle}</p>
          <h1 class="nm">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "thinker":
        return f'''
        <header class="hdr thinker">
          <img class="av av-lg" src="{av}" alt="{name}">
          <p class="hd ornament">{handle}</p>
          <h1 class="nm italic">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "tech-split":
        return f'''
        <header class="hdr tech">
          <p class="hd mono-tr">{handle}</p>
          <h1 class="nm">{name}</h1>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "gamer-neon":
        return f'''
        <header class="hdr gamer">
          <img class="av av-sq pixel-av" src="{av}" alt="{name}">
          <h1 class="nm pixel">{name}</h1>
          <p class="hd neon">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "sport-minimal":
        return f'''
        <header class="hdr sport-min">
          <p class="hd over">{handle}</p>
          <h1 class="nm">{name}</h1>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "biz-card":
        return f'''
        <header class="hdr biz">
          <p class="role caps">advisor</p>
          <h1 class="nm">{name}</h1>
          <img class="av av-sm" src="{av}" alt="{name}">
          <p class="hd">{handle}</p>
          {socials}
        </header>'''
    if h == "lab-index":
        return f'''
        <header class="hdr lab">
          <p class="hd index">01 / {handle}</p>
          <h1 class="nm">{name}</h1>
          <p class="role">{role}</p>
          <img class="av av-sq" src="{av}" alt="{name}">
          {socials}
        </header>'''
    if h == "boutique":
        return f'''
        <header class="hdr boutique">
          <img class="av av-lg" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd small">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "slash-name":
        return f'''
        <header class="hdr slash">
          <h1 class="nm">{name} <span class="hd slash-hd">/ {handle}</span></h1>
          <img class="av av-wide" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "logo-lockup":
        return f'''
        <header class="hdr lockup">
          <h1 class="nm">{name}<span class="hd dot"> · {handle}</span></h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "circle-badge":
        return f'''
        <header class="hdr badge-c">
          <img class="av av-lg ring" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "industrial":
        return f'''
        <header class="hdr industrial">
          <h1 class="nm">{name}</h1>
          <p class="hd tag">{handle}</p>
          <img class="av av-wide" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "bakery-ticket":
        return f'''
        <header class="hdr ticket">
          <p class="hd printed">{handle}</p>
          <h1 class="nm">{name}</h1>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "billboard":
        return f'''
        <header class="hdr billboard">
          <h1 class="nm huge">{name}</h1>
          <img class="av av-sm end" src="{av}" alt="{name}">
          <p class="hd br">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "fit-hero-name":
        return f'''
        <header class="hdr fit">
          <h1 class="nm mega">{name}</h1>
          <p class="hd caps">{handle}</p>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "quiet-photo":
        return f'''
        <header class="hdr quiet">
          <img class="av av-lg" src="{av}" alt="{name}">
          <h1 class="nm italic">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "broadcast":
        return f'''
        <header class="hdr tv">
          <span class="hd bug">LIVE {handle}</span>
          <h1 class="nm">{name}</h1>
          <img class="av av-sq" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "landscape-name":
        return f'''
        <div class="cover" style="background-image:url('{cover}')">
          <h1 class="nm on-cover">{name}</h1>
          <p class="hd on-cover">{handle}</p>
        </div>
        <header class="hdr after-cover">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "byline-block":
        return f'''
        <header class="hdr byline">
          <p class="role">notes by</p>
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          {socials}
        </header>'''
    if h == "gothic-modern":
        return f'''
        <header class="hdr gothic">
          <h1 class="nm">{name}</h1>
          <p class="hd modern">{handle}</p>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "dj-gradient":
        return f'''
        <header class="hdr dj">
          <p class="hd mix">A1 · {handle}</p>
          <h1 class="nm tracked">{name}</h1>
          <img class="av av-md ring" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "radio":
        return f'''
        <header class="hdr radio">
          <p class="hd freq">98.3 {handle}</p>
          <h1 class="nm">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "raw-box":
        return f'''
        <header class="hdr raw">
          <h1 class="nm boxed">{name}</h1>
          <p class="hd boxed">{handle}</p>
          <img class="av av-wide" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "producer":
        return f'''
        <header class="hdr prod">
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <img class="av av-sq" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "choir":
        return f'''
        <header class="hdr choir">
          <h1 class="nm italic">{name}</h1>
          <p class="hd tracked">{handle}</p>
          <img class="av av-lg" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "americana":
        return f'''
        <header class="hdr americana">
          <h1 class="nm">{name} <span class="hd">&amp; {handle}</span></h1>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "tour-poster":
        return f'''
        <header class="hdr tour">
          <p class="hd">on tour · {handle}</p>
          <h1 class="nm banner">{name}</h1>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "scoreboard":
        return f'''
        <header class="hdr score">
          <p class="hd score-hd">HOME {handle}</p>
          <h1 class="nm">{name}</h1>
          <img class="av av-sq" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "kit":
        return f'''
        <header class="hdr kit">
          <p class="num">07</p>
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "web3":
        return f'''
        <header class="hdr web3">
          <h1 class="nm">{name}</h1>
          <p class="hd chip">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''
    if h == "athlete-brand":
        return f'''
        <header class="hdr athlete">
          <h1 class="nm ul">{name}</h1>
          <p class="hd ul">{handle}</p>
          <img class="av av-md" src="{av}" alt="{name}">
          <p class="role">{role}</p>
          {socials}
        </header>'''
    return f'''
        <header class="hdr classic">
          <img class="av av-lg" src="{av}" alt="{name}">
          <h1 class="nm">{name}</h1>
          <p class="hd">{handle}</p>
          <p class="role">{role}</p>
          {socials}
        </header>'''


SHARED_CSS = r"""
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
html, body { margin: 0; min-height: 100%; }
body {
  font-family: Inter, system-ui, sans-serif;
  color: var(--ink);
  background: var(--bg);
}
a { color: inherit; text-decoration: none; }
.page {
  min-height: 100vh;
  max-width: 430px;
  margin: 0 auto;
  padding: 22px 16px 28px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.cover {
  margin: -22px -16px 0;
  height: 168px;
  background-size: cover;
  background-position: center;
  position: relative;
}
.cover.tall { height: 210px; }
.cover .nm, .cover .hd { position: absolute; left: 16px; color: #fff; text-shadow: 0 2px 12px #0008; }
.cover .nm { bottom: 36px; margin: 0; font-size: 2.4rem; }
.cover .hd { bottom: 14px; margin: 0; }
.hdr { display: grid; gap: 8px; justify-items: center; text-align: center; }
.hdr.split, .hdr.wordmark, .hdr.blocks, .hdr.tech { justify-items: start; text-align: left; width: 100%; }
.hdr.split { grid-template-columns: auto 1fr; align-items: center; }
.hdr.split .socials { grid-column: 1 / -1; }
.nm { margin: 0; line-height: .95; letter-spacing: -.03em; font-size: clamp(1.8rem, 8vw, 2.7rem); font-family: var(--name-font); }
.nm.huge, .nm.mega { font-size: clamp(2.6rem, 14vw, 4.2rem); }
.nm.script { font-size: 2.6rem; }
.nm.pixel { font-size: .95rem; line-height: 1.4; }
.nm.fashion { font-size: 4.2rem; letter-spacing: -.06em; }
.nm.tracked { letter-spacing: .22em; font-size: 1.8rem; }
.nm.banner { width: 100%; background: currentColor; color: var(--bg); padding: .15em 0; }
.nm.ul { border-bottom: 4px solid currentColor; }
.nm.boxed { border: 3px solid currentColor; padding: .15em .3em; }
.nm.italic { font-style: italic; }
.hd { margin: 0; font-size: .86rem; opacity: .8; }
.hd.tiny, .hd.micro, .hd.small, .hd.printed { font-size: .72rem; letter-spacing: .16em; text-transform: uppercase; }
.hd.inline, .hd.slash-hd, .hd.dot { font-size: .9rem; font-family: Inter, sans-serif; font-weight: 600; letter-spacing: 0; }
.hd.badge, .hd.chip, .hd.tag, .hd.bug { display: inline-flex; padding: .2rem .55rem; border: 1.5px solid currentColor; border-radius: 999px; font-size: .72rem; }
.hd.vert { writing-mode: vertical-rl; transform: rotate(180deg); position: absolute; left: 8px; top: 28px; letter-spacing: .2em; }
.hd.stamp-hd { border: 2px dashed currentColor; padding: .15rem .5rem; text-transform: uppercase; letter-spacing: .12em; }
.hd.neon { color: #d7ff3f; text-shadow: 0 0 12px #d7ff3f; font-family: 'Press Start 2P', monospace; font-size: .55rem; }
.hd.over { letter-spacing: .28em; text-transform: uppercase; font-size: .68rem; border-top: 2px solid currentColor; padding-top: .35rem; }
.hd.index, .hd.mono-tr, .hd.freq, .hd.mix, .hd.score-hd { font-family: 'IBM Plex Mono', monospace; font-size: .75rem; }
.hd.mono-tr { justify-self: end; }
.hd.br { justify-self: end; }
.hd.modern { font-family: Inter, sans-serif; letter-spacing: .18em; text-transform: lowercase; }
.hd.tracked { letter-spacing: .32em; text-transform: lowercase; }
.hd.boxed { border: 2px solid currentColor; padding: .1rem .4rem; }
.hd.ul { text-decoration: underline; text-underline-offset: 4px; }
.role { margin: 0; font-size: .78rem; opacity: .7; max-width: 22rem; }
.role.caps { letter-spacing: .2em; text-transform: uppercase; font-size: .68rem; }
.av { object-fit: cover; background: #ddd; }
.av-lg { width: 96px; height: 96px; border-radius: 50%; }
.av-md { width: 72px; height: 72px; border-radius: 50%; }
.av-sm { width: 48px; height: 48px; border-radius: 50%; }
.av-sq { width: 64px; height: 64px; border-radius: 8px; }
.av-wide { width: 100%; height: 120px; border-radius: 16px; }
.av-rect { width: 100%; height: 160px; border-radius: 0; }
.av-crest { width: 88px; height: 88px; border-radius: 20%; border: 3px solid currentColor; }
.av.ring { box-shadow: 0 0 0 4px var(--bg), 0 0 0 6px currentColor; }
.av-wrap { position: relative; }
.av-wrap .badge { position: absolute; bottom: -6px; left: 50%; transform: translateX(-50%); background: var(--bg); }
.hdr.masthead { position: relative; padding-left: 28px; }
.hdr.overlap { margin-top: -48px; }
.hdr.billboard, .hdr.fit, .hdr.wordmark { align-content: start; }
.num { font-family: 'Fjalla One', sans-serif; font-size: 3.4rem; line-height: 1; margin: 0; }
.socials { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 4px; }
.hdr.split .socials, .hdr.wordmark .socials, .hdr.blocks .socials, .hdr.tech .socials { justify-content: flex-start; }
.soc { width: 40px; height: 40px; display: grid; place-items: center; border: 1.5px solid color-mix(in srgb, currentColor 40%, transparent); border-radius: 50%; }
.soc svg { width: 18px; height: 18px; }
.links { display: grid; gap: 10px; margin-top: 6px; }
.link-btn {
  display: flex; align-items: center; justify-content: center;
  min-height: 52px; padding: .85rem 1rem;
  border-radius: var(--btn-r);
  background: var(--btn-bg); color: var(--btn-ink);
  border: 1.5px solid color-mix(in srgb, var(--ink) 25%, transparent);
  font-weight: 700; font-size: .95rem;
}
.brand-foot { margin-top: auto; text-align: center; font-size: .68rem; letter-spacing: .16em; text-transform: uppercase; opacity: .45; padding-top: 18px; }
.back { position: fixed; top: 10px; left: 10px; z-index: 4; font-size: .72rem; padding: .35rem .6rem; border: 1px solid color-mix(in srgb, currentColor 30%, transparent); border-radius: 999px; background: color-mix(in srgb, var(--bg) 80%, transparent); }
"""

PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{official} — template link na bio</title>
  <meta name="description" content="{note}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{fonts}" rel="stylesheet" />
  <link rel="stylesheet" href="template.css" />
  <style>
    body {{
      --bg: {bg};
      --ink: {ink};
      --btn-bg: {btn_bg};
      --btn-ink: {btn_ink};
      --btn-r: {btn_r};
      --name-font: {name_font};
    }}
  </style>
</head>
<body>
  <a class="back" href="./index.html">galeria</a>
  <div class="page">
    {header}
    <div class="links">{buttons}</div>
    <p class="brand-foot">link na bio · {official}</p>
  </div>
</body>
</html>
"""


def write_files():
    (OUT / "template.css").write_text(SHARED_CSS, encoding="utf-8")
    cards = []
    for t in TEMPLATES:
        html = PAGE.format(
            official=t["official"],
            note=t["note"],
            fonts=FONTS_HREF,
            bg=t["bg"],
            ink=t["ink"],
            btn_bg=t["btn_bg"],
            btn_ink=t["btn_ink"],
            btn_r=t["btn_r"],
            name_font=t["name_font"],
            header=header_html(t),
            buttons=buttons(t["links"], t),
        )
        (OUT / f"{t['slug']}.html").write_text(html, encoding="utf-8")
        cards.append(
            f'<a class="card" href="{t["slug"]}.html">'
            f'<iframe src="{t["slug"]}.html" title="{t["official"]}" loading="lazy" tabindex="-1"></iframe>'
            f'<span><strong>{t["official"]}</strong><em>{t["display"]}</em><small>{t["cat"]}</small></span>'
            f"</a>"
        )

    gallery = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Templates — inspirados no catálogo Linktree</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Syne:wght@800&display=swap" rel="stylesheet" />
  <style>
    body {{ margin:0; font-family:Inter,system-ui,sans-serif; background:#fcf6ea; color:#111; }}
    header {{ max-width:1180px; margin:0 auto; padding:28px 20px 12px; }}
    h1 {{ font-family:Syne,sans-serif; font-size:clamp(1.8rem,4vw,3rem); margin:0 0 .4rem; }}
    p.lead {{ max-width:46rem; color:#5f6475; }}
    .grid {{ max-width:1180px; margin:0 auto; padding:12px 20px 64px; display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:22px; }}
    .card {{ display:grid; gap:8px; color:inherit; text-decoration:none; }}
    iframe {{ width:190%; height:720px; transform:scale(.52); transform-origin:top left; border:3px solid #111; border-radius:28px; pointer-events:none; background:#fff; }}
    .card {{ height: 410px; overflow:hidden; }}
    .card span {{ display:grid; }}
    .card em {{ font-style:normal; font-weight:700; }}
    .card small {{ color:#5f6475; text-transform:uppercase; letter-spacing:.08em; }}
    a.home {{ display:inline-block; margin-bottom:12px; font-weight:700; }}
  </style>
</head>
<body>
  <header>
    <a class="home" href="/">← landing</a>
    <h1>{len(TEMPLATES)} templates, cada um com nome, handle e ícones próprios.</h1>
    <p class="lead">Catálogo mapeado em linktr.ee/s/templates e nas categorias Fashion, Health, Creator, Marketing, Music, Small Business, Social Media e Sports. Não é o mesmo bloco com cor trocada: o nome muda de fonte, escala e lugar; o @ muda de posição; os ícones de rede ficam na bio.</p>
  </header>
  <div class="grid">
    {''.join(cards)}
  </div>
</body>
</html>
"""
    (OUT / "index.html").write_text(gallery, encoding="utf-8")
    print(f"wrote {len(TEMPLATES)} templates + gallery")


if __name__ == "__main__":
    write_files()