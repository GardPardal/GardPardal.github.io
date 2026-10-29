#!/usr/bin/env python3
"""Portfólio de Alison Barbosa do Amaral. Gera index.html (EN) e pt/index.html (PT).  python3 build.py"""
import hashlib, html, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://gardpardal.github.io"
LINKS = {
    "linkedin": "https://www.linkedin.com/in/alisonamaral-ads",
    "github": "https://github.com/GardPardal",
    "orvan": "https://orvan.pro/",
    "page": "https://orvan.pro/alison-barbosa-do-amaral",
    "wa": "https://wa.me/5543999146088",
}
e = html.escape

PROJECTS = [
    {"id": "dallegrave", "name": "Dallegrave Gruber", "url": "https://dallegrave-gruber.alisonlz7.workers.dev", "year": "2026",
     "tags": ["Strategy", "Design", "Development", "Tracking", "Local SEO"],
     "en": ("Labor law firm · Foz do Iguaçu & Medianeira", "A full rebuild for a labor law firm: editorial design built on color-psychology research, 22 local SEO pages with legal citations, a 4-step qualifying funnel and server-side lead tracking on Cloudflare Workers + D1. Fully compliant with the Brazilian Bar's advertising rules."),
     "pt": ("Advocacia trabalhista · Foz do Iguaçu e Medianeira", "Reconstrução completa de um escritório trabalhista: design editorial baseado em pesquisa de psicologia das cores, 22 páginas de SEO local com citação de lei, funil de qualificação em 4 passos e rastreamento de leads pelo servidor em Cloudflare Workers + D1, dentro das regras da OAB.")},
    {"id": "lz7energia", "name": "LZ7 Energia", "url": "https://lz7energia.com.br", "year": "2026",
     "tags": ["Paid media", "Funnels", "Conversions API", "CRM", "AI"],
     "en": ("Solar energy · Paraná", "Rebuilt the whole acquisition system: campaigns by region and funnel stage, a lead-qualifying quiz, server-side Conversions API, lead attribution inside the CRM (Ploomes) and a 24/7 AI assistant on WhatsApp."),
     "pt": ("Energia solar · Paraná", "Reconstrução de toda a aquisição: campanhas por região e etapa do funil, quiz de qualificação, API de Conversões pelo servidor, atribuição de cada lead no CRM (Ploomes) e atendimento por IA no WhatsApp 24 horas.")},
    {"id": "orvan", "name": "Orvan", "url": "https://orvan.pro", "year": "2021 → now",
     "tags": ["Founder", "Brand", "SaaS", "Development"],
     "en": ("Performance marketing agency + SaaS", "My agency, serving 100+ businesses. I also built the Orvan Traffic Robot, a subscription software that reviews the client's ad accounts every day, pauses what spends without selling and explains results in plain language."),
     "pt": ("Agência de performance + SaaS", "Minha agência, com mais de 100 empresas atendidas. Também criei o Robô Gestor de Tráfego da Orvan, um software por assinatura que analisa as campanhas do cliente todo dia, pausa o que gasta sem vender e explica os resultados em português.")},
    {"id": "lz7store", "name": "LZ7 Store", "url": "https://lz7store.com", "year": "2026",
     "tags": ["E-commerce", "Design", "Cloudflare"],
     "en": ("Electric mobility store", "Catalog store for e-scooters, e-bikes and parts, running on Cloudflare Workers + D1, with ad-style animated scrolling and checkout through WhatsApp."),
     "pt": ("Loja de mobilidade elétrica", "Loja-catálogo de scooters, bikes elétricas e peças em Cloudflare Workers + D1, com visual de anúncio, scroll animado e compra pelo WhatsApp.")},
    {"id": "american", "name": "American Motors", "url": "https://americanmultimarcas.com", "year": "2026",
     "tags": ["Development", "Inventory", "Lead gen"],
     "en": ("Car dealership", "Dealership website with live inventory, trade-in and financing flows, built to turn ad traffic into WhatsApp conversations."),
     "pt": ("Loja de veículos", "Site de revenda com estoque, troca e financiamento, feito para transformar o tráfego dos anúncios em conversa no WhatsApp.")},
    {"id": "japa", "name": "Japa Intermediações", "url": "https://japainter.site", "year": "2025",
     "tags": ["Development", "Admin panel", "Branding"],
     "en": ("Car dealership", "Brand and full inventory system for a used-car dealer: search, featured vehicles, sell-your-car form and an admin panel."),
     "pt": ("Loja de veículos", "Marca e sistema completo de estoque para uma revenda: busca, destaques, formulário para vender o carro e painel administrativo.")},
    {"id": "amaral", "name": "Amaral Escola de Música", "url": "https://amaralmusical.com", "year": "2026",
     "tags": ["Design", "Student area", "Web app"],
     "en": ("Music school", "Website and student area for a music school, including an online course and a microphone practice mode that listens to the student play."),
     "pt": ("Escola de música", "Site e área do aluno de uma escola de música, com curso online e modo de prática pelo microfone que ouve o aluno tocar.")},
]

T = {
    "en": {
        "lang": "en", "html_lang": "en", "path": "/", "other": "/pt/", "other_label": "PT",
        "title": "Alison Amaral · Performance Marketing, Growth & Web",
        "desc": "Alison Barbosa do Amaral: performance marketer with 10+ years in paid acquisition, R$10M+ (~US$1.8M) managed on Meta and Google, founder of Orvan. Funnels, tracking and conversion websites.",
        "nav": ["Work", "Services", "Experience", "Contact"],
        "kicker": "Performance marketing · Growth · Web",
        "h1a": "I turn ad spend", "h1b": "into", "h1c": "measured revenue.",
        "lead": "Paid media, funnels, tracking and the websites that convert them. Founder of Orvan, 10+ years selling online, from offer to the last line of code.",
        "cta1": "Message me on LinkedIn", "cta2": "See selected work",
        "loc": "Paraná, Brazil · working remotely, US time zones",
        "stats": [("10", "+", "years selling online, since 2015"), ("10", "M+", "R$ managed in ads on Meta & Google (~US$1.8M)", "R$"), ("100", "+", "businesses served by Orvan"), ("30", "+", "people led")],
        "brands_t": "Brands I've run campaigns for",
        "work_k": "Selected work", "work_t": "Projects where strategy, design and code", "work_t2": "work as one",
        "visit": "Visit site",
        "svc_k": "Services", "svc_t": "One person for the whole", "svc_t2": "acquisition chain",
        "svc": [
            ("Paid media", "Meta Ads and Google Ads planned, launched and scaled for profit and ROAS, not vanity metrics. Account audits and rebuilds."),
            ("Funnels & offers", "Launches, evergreen and low-ticket: offer, pricing, bonuses, order bumps, sales pages and recovery flows."),
            ("Tracking & attribution", "Pixel + Conversions API, GTM, GA4, server-side events and CRM attribution, so every lead has a known source."),
            ("Conversion websites", "Fast, SEO-first websites and landing pages on Cloudflare, Hostinger or any stack, designed to sell."),
            ("AI & automation", "WhatsApp assistants, automated reporting and the Orvan Traffic Robot, an AI that manages ad accounts daily."),
            ("Local SEO", "Structured data, local pages and Google Business Profile, done with real local content, not doorway pages."),
        ],
        "exp_k": "Experience", "exp_t": "A career built", "exp_t2": "on results",
        "exp": [
            ("Jun 2026 – Present", "Senior Performance Marketing Analyst", "LZ7 Energia", "Rebuilt the acquisition system of a solar energy company and lead a team of 30+ people."),
            ("Mar 2021 – Present", "Founder & CEO", "Orvan", "Performance marketing agency. 100+ businesses taken from zero sales, or losing money on ads, to consistent profit."),
            ("2020 – 2021", "Paid Media Manager", "V4 Company", "Campaigns for major brands including C6 Bank, TIM Brasil, Spotify and Emagrecentro."),
            ("2018 – 2021", "Marketing Director", "LETTECH", "Built the brand, the expansion strategy and the online operation of a computer equipment manufacturer."),
            ("2015 – 2017", "Soldier", "Brazilian Air Force", "Discipline, hierarchy and responsibility under pressure."),
        ],
        "prod_k": "Own products", "prod": [("VTD · Venda Todo Dia", "Paid traffic course, Kiwify"), ("Biblioteca Claude", "4 course-ebooks with cross order bumps"), ("The 30-Day Money Reset", "English product for the US, UK and Canada")],
        "oss": "Open source", "oss_d": "Native Access 2 (Native Instruments / Kontakt) on Linux through Wine, with a login fix.",
        "contact_k": "Contact", "contact_t": "Have a project or a role", "contact_t2": "in mind?",
        "contact_p": "I'm open to remote roles and to new clients. The fastest way to reach me is LinkedIn or WhatsApp.",
        "langs": "Portuguese (native) · English (intermediate)",
        "foot": "Designed and built by Alison Barbosa do Amaral.",
    },
    "pt": {
        "lang": "pt", "html_lang": "pt-BR", "path": "/pt/", "other": "/", "other_label": "EN",
        "title": "Alison Barbosa do Amaral · Marketing de Performance, Growth e Web",
        "desc": "Alison Barbosa do Amaral: gestor de tráfego e marketing de performance há mais de 10 anos, R$ 10 mi+ investidos em Meta e Google, fundador da Orvan. Funis, rastreamento e sites que convertem.",
        "nav": ["Projetos", "Serviços", "Experiência", "Contato"],
        "kicker": "Marketing de performance · Growth · Web",
        "h1a": "Transformo investimento", "h1b": "em anúncio em", "h1c": "receita medida.",
        "lead": "Tráfego pago, funis, rastreamento e os sites que fazem tudo isso converter. Fundador da Orvan, vendendo pela internet desde 2015, da oferta à última linha de código.",
        "cta1": "Falar comigo no LinkedIn", "cta2": "Ver projetos",
        "loc": "Paraná, Brasil · trabalho remoto",
        "stats": [("10", "+", "anos vendendo pela internet, desde 2015"), ("10", " mi+", "investidos em anúncios no Meta e no Google", "R$ "), ("100", "+", "empresas atendidas pela Orvan"), ("30", "+", "pessoas lideradas")],
        "brands_t": "Marcas para as quais já rodei campanhas",
        "work_k": "Projetos", "work_t": "Projetos em que estratégia, design e código", "work_t2": "trabalham juntos",
        "visit": "Ver site",
        "svc_k": "Serviços", "svc_t": "Uma pessoa para toda a", "svc_t2": "cadeia de aquisição",
        "svc": [
            ("Tráfego pago", "Meta Ads e Google Ads planejados, lançados e escalados para lucro e ROAS, não para métrica de vaidade. Auditoria e reestruturação de contas."),
            ("Funis e ofertas", "Lançamento, perpétuo e low ticket: oferta, preço, bônus, order bump, página de vendas e recuperação."),
            ("Rastreamento e atribuição", "Pixel + API de Conversões, GTM, GA4, eventos pelo servidor e atribuição no CRM, para cada lead ter origem conhecida."),
            ("Sites que convertem", "Sites e landing pages rápidos, com SEO desde a base, em Cloudflare, Hostinger ou qualquer stack, feitos para vender."),
            ("IA e automação", "Atendimento por IA no WhatsApp, relatórios automáticos e o Robô Gestor da Orvan, uma IA que cuida das contas de anúncio todo dia."),
            ("SEO local", "Dados estruturados, páginas locais e Perfil da Empresa no Google, com conteúdo local de verdade."),
        ],
        "exp_k": "Experiência", "exp_t": "Uma carreira construída", "exp_t2": "em resultado",
        "exp": [
            ("jun/2026 – atual", "Analista de Marketing de Performance Sênior", "LZ7 Energia", "Reconstruí a aquisição de uma empresa de energia solar e lidero um time de mais de 30 pessoas."),
            ("mar/2021 – atual", "Fundador e CEO", "Orvan", "Agência de marketing de performance. Mais de 100 empresas levadas do zero, ou do prejuízo com anúncios, a um lucro consistente."),
            ("2020 – 2021", "Gestor de Tráfego", "V4 Company", "Campanhas para grandes marcas, entre elas C6 Bank, TIM, Spotify e Emagrecentro."),
            ("2018 – 2021", "Diretor de Marketing", "LETTECH", "Construí a marca, a estratégia de expansão e a operação online de uma fabricante de equipamentos de informática."),
            ("2015 – 2017", "Soldado", "Força Aérea Brasileira", "Disciplina, hierarquia e responsabilidade sob pressão."),
        ],
        "prod_k": "Produtos próprios", "prod": [("VTD · Venda Todo Dia", "Curso de tráfego pago, Kiwify"), ("Biblioteca Claude", "4 cursos-ebook com order bumps cruzados"), ("The 30-Day Money Reset", "Produto em inglês para EUA, Reino Unido e Canadá")],
        "oss": "Open source", "oss_d": "Native Access 2 (Native Instruments / Kontakt) no Linux via Wine, com correção do login.",
        "contact_k": "Contato", "contact_t": "Tem um projeto ou uma vaga", "contact_t2": "em mente?",
        "contact_p": "Estou aberto a vagas remotas e a novos clientes. O jeito mais rápido de falar comigo é pelo LinkedIn ou WhatsApp.",
        "langs": "Português (nativo) · Inglês (intermediário)",
        "foot": "Design e desenvolvimento por Alison Barbosa do Amaral.",
    },
}

BRANDS = ["C6 Bank", "TIM", "Spotify", "Emagrecentro", "LZ7 Energia", "LETTECH", "Orvan", "American Motors", "Amaral"]

ARROW = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'


def v(name):
    return hashlib.md5((ROOT / "assets" / name).read_bytes()).hexdigest()[:8]


def schema(t):
    person = {"@type": "Person", "@id": f"{SITE}/#me", "name": "Alison Barbosa do Amaral", "alternateName": "Alison Amaral",
              "jobTitle": "Performance Marketing Specialist" if t["lang"] == "en" else "Especialista em Marketing de Performance",
              "url": SITE + "/", "image": f"{SITE}/img/avatar.jpg",
              "sameAs": [LINKS["linkedin"], LINKS["github"], LINKS["page"]],
              "worksFor": [{"@type": "Organization", "name": "Orvan", "url": LINKS["orvan"]}, {"@type": "Organization", "name": "LZ7 Energia", "url": "https://lz7energia.com.br"}],
              "alumniOf": {"@type": "Organization", "name": "Força Aérea Brasileira"},
              "address": {"@type": "PostalAddress", "addressRegion": "PR", "addressCountry": "BR"},
              "knowsAbout": ["Meta Ads", "Google Ads", "Conversions API", "Google Tag Manager", "GA4", "Sales funnels", "Local SEO", "Cloudflare Workers", "Marketing automation"],
              "knowsLanguage": ["pt-BR", "en"]}
    page = {"@type": "ProfilePage", "@id": SITE + t["path"] + "#page", "url": SITE + t["path"], "name": t["title"], "description": t["desc"],
            "inLanguage": t["html_lang"], "mainEntity": {"@id": f"{SITE}/#me"}, "dateModified": date.today().isoformat()}
    works = {"@type": "ItemList", "name": "Portfolio", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": {"@type": "CreativeWork", "name": p["name"], "url": p["url"], "creator": {"@id": f"{SITE}/#me"}}}
        for i, p in enumerate(PROJECTS)]}
    return json.dumps({"@context": "https://schema.org", "@graph": [person, page, works]}, ensure_ascii=False, separators=(",", ":"))


def render(t):
    L = t["lang"]
    stats = "".join(
        f'<li class="rv"><b><span class="pre">{s[3] if len(s) > 3 else ""}</span><span data-count="{s[0]}">{s[0]}</span><span class="suf">{s[1]}</span></b><span>{s[2]}</span></li>'
        for s in t["stats"])
    brands = "".join(f"<span>{b}</span>" for b in BRANDS * 2)
    work = ""
    for i, p in enumerate(PROJECTS):
        sub, desc = p[L]
        tags = "".join(f"<li>{x}</li>" for x in p["tags"])
        work += f"""<article class="work rv">
<a class="shot" href="{p['url']}" target="_blank" rel="noopener" aria-label="{e(p['name'])} — {t['visit']}">
<span class="bar"><i></i><i></i><i></i><em>{e(p['url'].split('//')[1])}</em></span>
<img src="/img/work/{p["id"]}.webp" width="1200" height="750" style="aspect-ratio:16/10;object-fit:cover" loading="{'eager' if i == 0 else 'lazy'}" alt="{e(p['name'])}: {e(sub)}"></a>
<div class="meta"><span class="num">{i + 1:02d}</span><div><h3>{e(p['name'])}</h3><p class="sub">{e(sub)} · {p['year']}</p></div></div>
<p class="desc">{e(desc)}</p><ul class="tags">{tags}</ul>
<a class="go" href="{p['url']}" target="_blank" rel="noopener">{t['visit']} {ARROW}</a></article>"""
    svc = "".join(f'<li class="rv"><span class="i">{i + 1:02d}</span><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(t["svc"]))
    exp = "".join(f'<li class="rv"><span class="when">{w}</span><div><h3>{r}</h3><p class="org">{o}</p><p>{d}</p></div></li>' for w, r, o, d in t["exp"])
    prod = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in t["prod"])
    alt = "/pt/" if L == "en" else "/"
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{SITE}{t['path']}">
<link rel="alternate" hreflang="en" href="{SITE}/"><link rel="alternate" hreflang="pt-BR" href="{SITE}/pt/"><link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0e1013">
<meta property="og:type" content="profile"><meta property="profile:first_name" content="Alison"><meta property="profile:last_name" content="Amaral">
<meta property="og:title" content="{e(t['title'])}"><meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{SITE}{t['path']}"><meta property="og:image" content="{SITE}/img/og.jpg">
<meta property="og:locale" content="{'en_US' if L == 'en' else 'pt_BR'}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/style.css?v={v('style.css')}">
<link rel="preload" as="image" href="/img/alison.webp" fetchpriority="high">
<script type="application/ld+json">{schema(t)}</script>
</head>
<body>
<div class="grain" aria-hidden="true"></div>
<header class="top"><div class="wrap">
<a class="mark" href="{t['path']}"><span>AA</span>Alison Amaral</a>
<nav aria-label="Main"><a href="#work">{t['nav'][0]}</a><a href="#services">{t['nav'][1]}</a><a href="#experience">{t['nav'][2]}</a><a href="#contact">{t['nav'][3]}</a></nav>
<a class="lang" href="{alt}" hreflang="{'pt-BR' if L == 'en' else 'en'}" lang="{'pt-BR' if L == 'en' else 'en'}">{t['other_label']}</a>
</div></header>
<main>
<section class="hero"><div class="wrap">
<div class="copy">
<p class="kicker">{t['kicker']}</p>
<h1><span class="ln"><span>{t['h1a']}</span></span> <span class="ln"><span>{t['h1b']} <em>{t['h1c']}</em></span></span></h1>
<p class="lead">{t['lead']}</p>
<div class="ctas"><a class="btn primary magnet" href="{LINKS['linkedin']}" target="_blank" rel="noopener">{t['cta1']} {ARROW}</a><a class="btn ghost" href="#work">{t['cta2']}</a></div>
<p class="loc"><i></i>{t['loc']}</p>
</div>
<figure class="portrait"><div class="ring" aria-hidden="true"></div><img src="/img/alison.webp" width="760" height="1005" alt="Alison Barbosa do Amaral"></figure>
</div></section>
<section class="stats"><div class="wrap"><ul>{stats}</ul></div></section>
<section class="brands" aria-label="{t['brands_t']}"><p class="wrap">{t['brands_t']}</p><div class="marquee"><div class="track">{brands}</div></div></section>
<section class="sec" id="work"><div class="wrap">
<header class="head rv"><p class="k">{t['work_k']}</p><h2>{t['work_t']} <em>{t['work_t2']}</em></h2></header>
<div class="works">{work}</div></div></section>
<section class="sec dark" id="services"><div class="wrap">
<header class="head rv"><p class="k">{t['svc_k']}</p><h2>{t['svc_t']} <em>{t['svc_t2']}</em></h2></header>
<ol class="svc">{svc}</ol></div></section>
<section class="sec" id="experience"><div class="wrap exp-grid">
<div class="exp-side"><header class="head rv"><p class="k">{t['exp_k']}</p><h2>{t['exp_t']} <em>{t['exp_t2']}</em></h2></header>
<img class="rv" src="/img/alison-notebook.webp" width="640" height="684" loading="lazy" alt="Alison Amaral">
<div class="side-box rv"><p class="k">{t['prod_k']}</p><ul class="prod">{prod}</ul>
<p class="k" style="margin-top:22px">{t['oss']}</p><p><a href="https://github.com/GardPardal/native-access-linux" target="_blank" rel="noopener">native-access-linux</a> · {t['oss_d']}</p></div></div>
<ol class="timeline">{exp}</ol></div></section>
<section class="sec contact" id="contact"><div class="wrap">
<p class="k rv">{t['contact_k']}</p><h2 class="rv">{t['contact_t']} <em>{t['contact_t2']}</em></h2>
<p class="lead rv">{t['contact_p']}</p>
<div class="ctas rv"><a class="btn primary magnet" href="{LINKS['linkedin']}" target="_blank" rel="noopener">LinkedIn {ARROW}</a><a class="btn ghost" href="{LINKS['wa']}" target="_blank" rel="noopener">WhatsApp {ARROW}</a><a class="btn ghost" href="{LINKS['orvan']}" target="_blank" rel="noopener">Orvan {ARROW}</a><a class="btn ghost" href="{LINKS['github']}" target="_blank" rel="noopener">GitHub {ARROW}</a></div>
<p class="langs rv">{t['langs']}</p>
</div></section>
</main>
<footer class="foot"><div class="wrap"><span>© {date.today().year} · {t['foot']}</span><a href="{alt}">{t['other_label']}</a></div></footer>
<script src="/assets/main.js?v={v('main.js')}" defer></script>
</body></html>"""


def main():
    for k, t in T.items():
        out = ROOT / ("index.html" if k == "en" else "pt/index.html")
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(t), encoding="utf-8")
    (ROOT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0e1013"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="30" fill="#ecebe7">AA</text><circle cx="50" cy="16" r="5" fill="#4fb3d9"/></svg>', encoding="utf-8")
    today = date.today().isoformat()
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + "".join(f'<url><loc>{SITE}{p}</loc><lastmod>{today}</lastmod><xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/><xhtml:link rel="alternate" hreflang="pt-BR" href="{SITE}/pt/"/></url>' for p in ("/", "/pt/"))
        + "</urlset>", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("")
    print("ok")


if __name__ == "__main__":
    main()
