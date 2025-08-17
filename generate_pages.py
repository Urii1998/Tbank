import re
import os

# Содержимое index.html (вставьте полный текст из <DOCUMENT>)
index_html = '''
<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=103741323', 'ym');

    ym(103741323, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", accurateTrackBounce:true, trackLinks:true});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/103741323" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
        </script><!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Финансовые продукты Т‑Банка — бонусы, кешбэк и выгодные условия</title>
  <meta name="description" content="Оформите карты, вклады, инвестиции и страхование Т‑Банка. Выгодные условия, бонусы и быстрые заявки. Партнёрский сайт." />
  <meta name="keywords" content="Т‑Банк, T‑Bank, партнерская программа, кредитные карты, дебетовые карты, вклады, инвестиции, страхование, рефералы" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <!-- Tailwind CSS -->
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
  <!-- AOS Animations -->
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet" />
  <!-- Feather Icons -->
  <script src="https://unpkg.com/feather-icons"></script>
  <!-- Open Graph / Twitter -->
  <meta property="og:title" content="Финансовые продукты Т‑Банка — выгодные предложения" />
  <meta property="og:description" content="Карты, вклады, инвестиции и страхование Т‑Банка. Подберите продукт и оформите онлайн." />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="T‑Bank Guide" />
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <meta property="og:locale" content="ru_RU" />
  <meta name="twitter:card" content="summary" />
  <!-- JSON‑LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "T‑Bank Guide",
    "url": "https://example.com/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://example.com/?q={search_term_string}",
      "query-input": "required name=search_term_string"
    }
  }
  </script>
  <style>
    :root { scroll-behavior: smooth; }
    body { font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Apple Color Emoji", "Segoe UI Emoji"; }
    .product-card { transition: transform .3s, box-shadow .3s; }
    .product-card:hover { transform: translateY(-6px); box-shadow: 0 12px 24px rgba(0,0,0,.12); }
    .product-card img { max-height: 96px; width: auto; object-fit: contain; }
    .hero-grad { background: radial-gradient(1200px 600px at 10% 20%, rgba(59,130,246,.25), transparent), linear-gradient(90deg, #1e3a8a, #2563eb, #3b82f6); }
    .badge { position:absolute; top:12px; left:12px; padding:4px 10px; border-radius:9999px; font-weight:700; font-size:12px; color:#fff; }
    .badge-hot { background:#ef4444; }
    .badge-new { background:#10b981; }
    .badge-top { background:#f59e0b; }
    .btn { display:inline-flex; align-items:center; justify-content:center; padding:.75rem 1rem; border-radius:.75rem; font-weight:700; transition:transform .15s ease, box-shadow .15s ease; }
    .btn:hover { transform: translateY(-1px); }
    .btn-primary { background:#2563eb; color:#fff; }
    .btn-primary:hover { background:#1d4ed8; }
    .btn-green { background:#059669; color:#fff; }
    .btn-green:hover { background:#047857; }
    .btn-amber { background:#f59e0b; color:#111827; }
    .btn-amber:hover { background:#d97706; color:#111827; }
    .safe-note { font-size: .85rem; }
    .shadow-soft { box-shadow: 0 8px 20px rgba(0,0,0,.08); }
    #mobileNav { transition: transform 0.3s ease, opacity 0.3s ease; transform: translateY(-10px); opacity: 0; }
    #mobileNav:not(.hidden) { transform: translateY(0); opacity: 1; }
    #mobileNav a { padding: 0.75rem 1rem; }
    @media (max-width: 640px) {
      h1 { font-size: 1.875rem; line-height: 2.25rem; }
      h2 { font-size: 1.5rem; }
      .product-card { padding: 1rem; }
    }
  </style>
  <!-- Yandex.Metrika counter -->
  <script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=103734789', 'ym');
    ym(103734789, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", accurateTrackBounce:true, trackLinks:true});
  </script>
  <noscript><div><img src="https://mc.yandex.ru/watch/103734789" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
</head>
<body class="bg-gray-50 text-gray-900">
  <!-- Header -->
  <header class="bg-white/90 backdrop-filter backdrop-blur shadow z-50 sticky top-0">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between py-4">
        <a href="#top" class="flex items-center space-x-3">
          <span class="inline-flex items-center justify-center h-9 w-9 rounded-xl bg-blue-600 text-white font-black">T</span>
          <span class="text-lg font-bold">T‑Bank Guide</span>
        </a>
        <nav class="hidden md:flex items-center space-x-6 text-sm font-medium">
          <a href="#products" class="hover:text-blue-700">Продукты</a>
          <a href="#benefits" class="hover:text-blue-700">Преимущества</a>
          <a href="#faq" class="hover:text-blue-700">FAQ</a>
          <a href="#contacts" class="hover:text-blue-700">Контакты</a>
          <a href="#products" class="btn btn-amber shadow-soft">Подобрать продукт</a>
        </nav>
        <button id="menuBtn" aria-label="Открыть меню" class="md:hidden inline-flex items-center justify-center h-10 w-10 rounded-lg border border-gray-200">
          <i data-feather="menu"></i>
        </button>
      </div>
      <div id="mobileNav" class="md:hidden hidden pb-4">
        <div class="grid gap-2 text-sm">
          <a href="#products" class="py-2">Продукты</a>
          <a href="#benefits" class="py-2">Преимущества</a>
          <a href="#faq" class="py-2">FAQ</a>
          <a href="#contacts" class="py-2">Контакты</a>
        </div>
      </div>
    </div>
  </header>
  <!-- Hero -->
  <section class="hero-grad text-white relative" id="top">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
      <div class="text-center" data-aos="fade-up">
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold leading-tight">Ваши финансы с Т‑Банком: карты, вклады, инвестиции и защита</h1>
        <p class="mt-5 text-base sm:text-lg md:text-xl text-blue-100 max-w-3xl mx-auto">Подбирайте продукты с выгодой — кешбэк до 30%, бонусы за оформление и прозрачные условия. Официальные партнёрские ссылки.</p>
        <div class="mt-8 flex items-center justify-center space-x-3">
          <a href="#products" class="btn btn-primary shadow-soft">Смотреть продукты</a>
          <a href="#benefits" class="btn btn-amber shadow-soft">Почему это выгодно</a>
        </div>
        <p class="mt-4 safe-note text-blue-100/90">Реклама. АО «Т‑Банк», ОГРН 1027739642281, универсальная лицензия ЦБ РФ № 2673.</p>
      </div>
    </div>
  </section>
  <!-- Benefits -->
  <section id="benefits" class="py-12 sm:py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl sm:text-3xl font-bold text-center mb-10" data-aos="fade-down">Почему оформлять через нас</h2>
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <div class="bg-gray-50 rounded-2xl p-6 shadow-sm" data-aos="zoom-in">
          <i data-feather="zap" class="mb-3" width="28" height="28"></i>
          <h3 class="font-semibold mb-1">Быстро и просто</h3>
          <p class="text-gray-600 text-sm">Короткие формы, официальные ссылки, моментальная отправка заявки.</p>
        </div>
        <div class="bg-gray-50 rounded-2xl p-6 shadow-sm" data-aos="zoom-in" data-aos-delay="50">
          <i data-feather="percent" class="mb-3" width="28" height="28"></i>
          <h3 class="font-semibold mb-1">Выгоды и кешбэк</h3>
          <p class="text-gray-600 text-sm">Кешбэк до 30% и акции по отдельным продуктам от банка.</p>
        </div>
        <div class="bg-gray-50 rounded-2xl p-6 shadow-sm" data-aos="zoom-in" data-aos-delay="100">
          <i data-feather="shield" class="mb-3" width="28" height="28"></i>
          <h3 class="font-semibold mb-1">Безопасно</h3>
          <p class="text-gray-600 text-sm">Переход сразу на сайт банка. Данные защищены. Мы ничего не храним.</p>
        </div>
        <div class="bg-gray-50 rounded-2xl p-6 shadow-sm" data-aos="zoom-in" data-aos-delay="150">
          <i data-feather="award" class="mb-3" width="28" height="28"></i>
          <h3 class="font-semibold mb-1">Прозрачно</h3>
          <p class="text-gray-600 text-sm">Все условия и тарифы — на стороне Т‑Банка. Никаких скрытых действий.</p>
        </div>
      </div>
    </div>
  </section>
  <!-- Products -->
  <section id="products" class="py-12 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl sm:text-3xl font-bold text-center mb-10" data-aos="fade-down">Продукты и услуги Т‑Банка</h2>
      <div class="mb-8 flex flex-wrap gap-3 justify-center" data-aos="fade-down">
        <button class="btn btn-primary" data-filter="all">Все продукты</button>
        <button class="btn btn-amber" data-filter="cards">Карты</button>
        <button class="btn btn-green" data-filter="invest">Инвестиции</button>
        <button class="btn btn-primary" data-filter="business">Бизнес</button>
        <button class="btn btn-amber" data-filter="insurance">Страхование</button>
        <button class="btn btn-green" data-filter="other">Другое</button>
      </div>
      <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <!-- Карта Т‑Банк Black -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-category="cards" itemscope itemtype="https://schema.org/Product">
          <span class="badge badge-top">🔥 Популярно</span>
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9hZmI2YTVmNS0xNzU3LTQ2OWQtOTdkNi01Zjk3YjlhZGUwNzAucG5n" alt="Карта Т-Банк Black" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Карта Т‑Банк Black</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Дебетовая карта с кешбэком до 30% и бесплатным обслуживанием для покупок и путешествий.</p>
          <a data-product="Карта Black" href="https://www.tbank.ru/baf/8NztMpl4GYD?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Оформить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Дебетовые карты">
        </div>
        <!-- Исламская карта -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="50" data-category="cards" itemscope itemtype="https://schema.org/Product">
          <span class="badge badge-new">✨ Новинка</span>
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9mMjQ2ZmNjZS1kY2QzLTRlN2MtYTYyMC0wNmM3M2VhNjQ0ODkucG5n" alt="Исламская карта Т-Банка" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Исламская карта Т‑Банка</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Дебетовая карта без процентов, соответствующая принципам шариата.</p>
          <a data-product="Исламская карта" href="https://www.tbank.ru/baf/3i1Y8jnGz3j?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Оформить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Дебетовые карты">
        </div>
        <!-- Т‑Мобайл -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="100" data-category="other" itemscope itemtype="https://schema.org/Product">
          <span class="badge badge-new">✨ Новинка</span>
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy80MzA4M2JlYS0xZTM1LTQyNjgtOTNiYi1iZTE4OTRmNjk4ZDAucG5n" alt="Т-Мобайл" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Т‑Мобайл</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Мобильная связь с бонусами и защитой от спама.</p>
          <a data-product="Т‑Мобайл" href="https://www.tbank.ru/baf/AF2PkIkYhGa?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-green w-full" itemprop="url">Подключить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Мобильная связь">
        </div>
        <!-- Счёт для инвестиций -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-category="invest" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9kOGY0NzQxZC1lZDIxLTQ2ZTgtODlhOS05NjE3MTA1M2E0N2IucG5n" alt="Счёт для инвестиций" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Счёт для инвестиций</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Начните инвестировать с 10 ₽ и получайте бонусы.</p>
          <a data-product="Счёт для инвестиций" href="https://www.tbank.ru/baf/5WhRJUSwjSZ?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Открыть счёт</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Инвестиции">
        </div>
        <!-- Счёт для бизнеса -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="50" data-category="business" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9kMTg4MTkyNC1iNmZmLTRlNjUtYmI0Ny1jZDRlNzNhMGMxYTUucG5n" alt="Счёт для бизнеса" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Счёт для бизнеса</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Удобное РКО для предпринимателей с бонусами.</p>
          <a data-product="Счёт для бизнеса" href="https://www.tbank.ru/baf/7mLaIhRFQfi?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Открыть счёт</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Бизнес">
        </div>
        <!-- Регистрация бизнеса -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="100" data-category="business" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BhZ2VzL2ZpbGVzL2I3ZjhhNjYyLTM3YTktNDYzNS1hMzA5LTkyZDllMmYzMjBjYy5wbmc=" alt="Регистрация бизнеса" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Регистрация бизнеса</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Быстрая регистрация ИП или ООО с поддержкой.</p>
          <a data-product="Регистрация бизнеса" href="https://www.tbank.ru/baf/6jHMWSvejuF?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-amber w-full" itemprop="url">Зарегистрировать</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Бизнес">
        </div>
        <!-- Вклад от 2 месяцев -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-category="other" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy8xMmE0MGRjNi02MjFjLTQ3NjYtOTcyMC0yMjZmOGQwYTYzOTgucG5n" alt="Вклад от 2 месяцев" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Вклад от 2 месяцев</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Гибкие вклады с потенциально высокой доходностью.</p>
          <a data-product="Вклад" href="https://www.tbank.ru/baf/AiZI88WMDHn?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Открыть вклад</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Вклады">
        </div>
        <!-- Сервис Топливо -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="50" data-category="other" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy83NWVkOTgyMy1lNWY4LTRkODAtOTk2Yi1jZDg5ZTk4MzM2NjEucG5n" alt="Сервис Топливо" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Сервис Топливо</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Экономьте на топливе с кешбэком.</p>
          <a data-product="Топливо" href="https://www.tbank.ru/baf/3Zfd1gqI20u?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-green w-full" itemprop="url">Подключить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Сервисы">
        </div>
        <!-- Автоследование -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="100" data-category="invest" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy85NGNiNTc1Zi0xMmJlLTRiMDUtODY3Yy0zZmViMzFmYWZkZDQucG5n" alt="Автоследование" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Автоследование</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Автоматическое управление инвестициями для пассивного дохода.</p>
          <a data-product="Автоследование" href="https://www.tbank.ru/baf/8VkNuYdw7wu?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Начать</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Инвестиции">
        </div>
        <!-- Работа в Т‑Банке -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-category="other" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy85YTNiODhkMC01ZTRmLTQ5OTMtOTRjMC04ZDM1MzZiY2IxZGMucG5n" alt="Работа в Т-Банке" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Работа в Т‑Банке</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Карьерные возможности с гибким графиком и бонусами.</p>
          <a data-product="Работа" href="https://www.tbank.ru/baf/2jybuQ7AbPI?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Подать заявку</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Карьера">
        </div>
        <!-- Подписка Pro -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="50" data-category="other" itemscope itemtype="https://schema.org/Product">
          <span class="badge badge-hot">🔥 Выгодно</span>
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9kMjc2ZjQ2OC1kMmU3LTQ0ZGMtOTE2Ny1mYmYxMGIyNDJjZmUucG5n" alt="Подписка Pro" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Подписка Pro</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Расширенные бонусы и привилегии для клиентов.</p>
          <a data-product="Подписка Pro" href="https://www.tbank.ru/baf/8R2BCjPsOoO?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-amber w-full" itemprop="url">Оформить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Подписки">
        </div>
        <!-- Рефинансирование кредитов -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="100" data-category="other" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9lYzEwNWY3Yy1jOTU0LTQzMjItYjFhYi1jODEyNWM1MDUzMzgucG5n" alt="Рефинансирование кредитов" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Рефинансирование кредитов</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Снизьте ежемесячные платежи и переплату по кредитам.</p>
          <a data-product="Рефинансирование" href="https://www.tbank.ru/baf/4M6C21n69OQ?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Рефинансировать</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Кредиты">
        </div>
        <!-- КАСКО -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-category="insurance" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BmYS1tdWx0aW1lZGlhL2ltYWdlcy9iYzI0NGM4ZS1jNWE1LTQwOTMtODNlMS1jYTFmZTdlOTFmYWYucG5n" alt="КАСКО" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">КАСКО</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Страхование автомобиля на выгодных условиях.</p>
          <a data-product="КАСКО" href="https://www.tbank.ru/baf/73Tzb0jwS46?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Оформить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Страхование">
        </div>
        <!-- Страхование ипотеки -->
        <div class="relative product-card bg-white rounded-2xl p-6 shadow" data-aos="zoom-in" data-aos-delay="50" data-category="insurance" itemscope itemtype="https://schema.org/Product">
          <img src="https://imgproxy.cdn-tinkoff.ru/compressed95/aHR0cHM6Ly9jZG4udGJhbmsucnUvc3RhdGljL3BhZ2VzL2ZpbGVzL2RiOTZkZTZlLWM5OTYtNGE5ZC04MmZjLTk0M2Q0MzU1YWU2ZS5wbmc=" alt="Страхование ипотеки" class="h-24 w-auto mx-auto mb-4 object-contain" loading="lazy" width="150" height="96">
          <h3 class="text-xl font-semibold text-center" itemprop="name">Страхование ипотеки</h3>
          <p class="text-gray-600 text-sm mt-2 mb-4 text-center" itemprop="description">Надёжная защита для ипотечных заёмщиков.</p>
          <a data-product="Страхование ипотеки" href="https://www.tbank.ru/baf/774l6bCECO3?utm_source=site&utm_medium=referral&utm_campaign=product_links" class="btn btn-primary w-full" itemprop="url">Оформить</a>
          <meta itemprop="brand" content="Т-Банк">
          <meta itemprop="category" content="Страхование">
        </div>
      <p class="mt-8 text-xs text-gray-500 text-center max-w-3xl mx-auto">Информация носит рекламный характер и не является публичной офертой. Условия и тарифы уточняйте на сайте Т‑Банка по ссылке соответствующего продукта.</p>
    </div>
  </section>
  <!-- FAQ -->
  <section id="faq" class="py-12 sm:py-16 bg-white">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 class="text-2xl sm:text-3xl font-bold text-center mb-8" data-aos="fade-down">Частые вопросы</h2>
      <div class="space-y-4">
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Это официальный сайт Т‑Банка?</summary>
          <p class="text-gray-600 mt-2 text-sm">Нет. Это партнёрский сайт. Все заявки оформляются на официальном сайте Т‑Банка по безопасным ссылкам.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up" data-aos-delay="50">
          <summary class="font-semibold cursor-pointer">Безопасно ли переходить по ссылкам?</summary>
          <p class="text-gray-600 mt-2 text-sm">Да. Ссылки ведут на домен <span class="font-mono">tbank.ru</span>. Мы не собираем и не храним персональные данные.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up" data-aos-delay="100">
          <summary class="font-semibold cursor-pointer">Есть ли дополнительные комиссии?</summary>
          <p class="text-gray-600 mt-2 text-sm">Нет. Условия полностью соответствуют условиям на сайте Т‑Банка. Возможные комиссии и тарифы указаны у банка.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Карта Т‑Банк Black?</summary>
          <p class="text-gray-600 mt-2 text-sm">Карта Т‑Банк Black предлагает кэшбэк до 30% рублями за покупки, бесплатное обслуживание при хранении от 50 000 ₽, переводы без комиссии до 100 000 ₽ в месяц через СБП и проценты на остаток до 5%. Это удобный инструмент для ежедневных трат и сбережений, помогая экономить на покупках и получать дополнительный доход.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Исламская карта Т‑Банка?</summary>
          <p class="text-gray-600 mt-2 text-sm">Исламская карта соответствует принципам шариата, без процентов и ростовщичества, с ограничениями на харамные сферы. Она позволяет получать кэшбэк с опцией отключения, бесплатные переводы до 30 млн ₽ в месяц и удобное управление финансами в соответствии с религиозными нормами.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Т‑Мобайл?</summary>
          <p class="text-gray-600 mt-2 text-sm">Т‑Мобайл предлагает гибкие тарифы с конструктором, безлимитные сервисы, защиту от спама и бонусы для клиентов банка. Это удобная связь с возможностью экономии на трафике и звонках, идеально для активных пользователей интернета и мессенджеров.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Счёт для инвестиций?</summary>
          <p class="text-gray-600 mt-2 text-sm">Счёт для инвестиций позволяет получать налоговые вычеты до 52 000 ₽ в год, диверсифицировать сбережения и потенциально обогнать инфляцию. Это инструмент для долгосрочного роста капитала с доступом к биржевым инструментам, подходящий для новичков и опытных инвесторов.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Счёт для бизнеса?</summary>
          <p class="text-gray-600 mt-2 text-sm">Счёт для бизнеса предлагает бесплатное открытие, низкие комиссии, онлайн-бухгалтерию и удобный мобильный банк. Это упрощает управление финансами, переводы и отчетность, помогая предпринимателям экономить время и деньги.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Регистрация бизнеса?</summary>
          <p class="text-gray-600 mt-2 text-sm">Регистрация бизнеса в Т‑Банке бесплатна, без походов в ФНС, с помощью в документах и открытием счета. Это ускоряет запуск бизнеса, экономит время и деньги, идеально для начинающих предпринимателей.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Вклад от 2 месяцев?</summary>
          <p class="text-gray-600 mt-2 text-sm">Вклад от 2 месяцев предлагает ставки до 16% годовых, пополнение и капитализацию, что позволяет получать пассивный доход выше инфляции. Это надежный способ сбережений с гарантией до 1,4 млн ₽.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Сервис Топливо?</summary>
          <p class="text-gray-600 mt-2 text-sm">Сервис Топливо позволяет заправляться без выхода из машины, с кэшбэком до 10% и удобством. Это экономит время и деньги на топливе, идеально для водителей.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Автоследование?</summary>
          <p class="text-gray-600 mt-2 text-sm">Автоследование копирует сделки экспертов, автоматизируя инвестиции и диверсифицируя портфель. Это упрощает заработок на бирже для новичков без опыта.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Работа в Т‑Банке?</summary>
          <p class="text-gray-600 mt-2 text-sm">Работа в Т‑Банке предлагает удаленный формат, развитие, бонусы и корпоративные плюшки. Это возможность карьерного роста в динамичной компании.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Подписка Pro?</summary>
          <p class="text-gray-600 mt-2 text-sm">Подписка Pro повышает кэшбэк, ставки по счетам и лимиты, снижает комиссии. Это увеличивает доход и удобство использования продуктов банка.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужно Рефинансирование кредитов?</summary>
          <p class="text-gray-600 mt-2 text-sm">Рефинансирование снижает ставку и платежи, объединяет кредиты без справок. Это экономит деньги и упрощает управление долгами.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужно Каско?</summary>
          <p class="text-gray-600 mt-2 text-sm">Каско покрывает ущерб авто, угон и ремонт, с скидками за аккуратное вождение. Это защищает от финансовых потерь в ДТП.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужно Страхование ипотеки?</summary>
          <p class="text-gray-600 mt-2 text-sm">Страхование ипотеки снижает ставку по кредиту, защищает от рисков потери имущества или здоровья. Это обязательная защита для спокойствия.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужен Кредит наличными?</summary>
          <p class="text-gray-600 mt-2 text-sm">Кредит наличными выдается быстро без справок, с низкими ставками до 5 млн ₽. Это гибкое решение для любых нужд.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужна Пенсия на карту Т‑Банка?</summary>
          <p class="text-gray-600 mt-2 text-sm">Пенсия на карту Т‑Банка дает кэшбэк, проценты на остаток до 5% и бесплатное обслуживание. Это удобный способ получать и тратить пенсию.</p>
        </details>
        <details class="bg-gray-50 rounded-xl p-5 shadow-sm" data-aos="fade-up">
          <summary class="font-semibold cursor-pointer">Почему нужно Приложение Т‑Банка на iOS?</summary>
          <p class="text-gray-600 mt-2 text-sm">Приложение Т‑Банка на iOS удобно управляет финансами, безопасно, с быстрым доступом к услугам. Это современный инструмент для повседневного банкинга.</p>
        </details>
      </div>
    </div>
  </section>
  <!-- Contacts -->
  <section id="contacts" class="py-12 sm:py-16">
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h2 class="text-2xl sm:text-3xl font-bold mb-6" data-aos="fade-down">Свяжитесь с нами</h2>
      <p class="text-gray-600 mb-6" data-aos="fade-up">Есть вопросы или нужна помощь с подбором? Напишите нам в Telegram — ответим в течение рабочего дня.</p>
      <div class="flex items-center justify-center gap-3" data-aos="zoom-in">
        <a href="https://t.me/UK_Sh0p_Support" class="btn btn-primary" data-goal="contact_telegram">Написать в Telegram</a>
        <a href="#top" class="btn btn-amber" aria-label="Наверх" data-goal="scroll_top">Наверх</a>
      </div>
    </div>
  </section>
  <!-- Footer -->
  <footer class="bg-gray-900 text-gray-300 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center">
      <p>&copy; 2025 T‑Bank Guide. Все права защищены.</p>
      <p class="mt-2">Реклама. АО «Т‑Банк», ОГРН 1027739642281, универсальная лицензия ЦБ РФ № 2673.</p>
    </div>
  </footer>
  <!-- Scripts -->
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>
    AOS.init({ duration: 700, once: true, offset: 80 });
    feather.replace();
    // Мобильное меню
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');
    if (menuBtn && mobileNav) {
      menuBtn.addEventListener('click', () => {
        mobileNav.classList.toggle('hidden');
        const isOpen = !mobileNav.classList.contains('hidden');
        menuBtn.innerHTML = isOpen ? '<i data-feather="x"></i>' : '<i data-feather="menu"></i>';
        feather.replace();
      });
    }
    // Фильтры продуктов
    document.querySelectorAll('[data-filter]').forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');
        document.querySelectorAll('.product-card').forEach(card => {
          const category = card.getAttribute('data-category');
          card.style.display = filter === 'all' || category === filter ? 'block' : 'none';
        });
        AOS.refresh();
        try { ym(103734789, 'reachGoal', 'filter_product', { filter }); } catch (e) {}
      });
    });
    // Трекинг кликов по продуктам
    document.querySelectorAll('[data-product]').forEach(el => {
      el.addEventListener('click', () => {
        try { ym(103734789, 'reachGoal', 'click_product', { name: el.getAttribute('data-product') }); } catch (e) {}
      });
    });
    // Трекинг Telegram и Наверх
    document.querySelectorAll('[data-goal="contact_telegram"]').forEach(el => {
      el.addEventListener('click', () => {
        try { ym(103734789, 'reachGoal', 'contact_telegram'); } catch (e) {}
      });
    });
    document.querySelectorAll('[data-goal="scroll_top"]').forEach(el => {
      el.addEventListener('click', () => {
        try { ym(103734789, 'reachGoal', 'scroll_top'); } catch (e) {}
      });
    });
  </script>
</body>
</html>  
'''


# Содержимое sitemap.xml (вставьте полный текст из <DOCUMENT>)
sitemap_content = '''
 
   
     <?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://refbankuk.ru/</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>1.0</priority>
    <keywords>финансовые услуги т банк, рефинансирование кредитов, дебетовые карты</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-adygeya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика адыгея, рефинансирование кредитов в Республика Адыгея, финансовые услуги в Республика Адыгея</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-altay</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика алтай, рефинансирование кредитов в Республика Алтай, финансовые услуги в Республика Алтай</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-bashkortostan</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика башкортостан, рефинансирование кредитов в Республика Башкортостан, финансовые услуги в Республика Башкортостан</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-buryatiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика бурятия, рефинансирование кредитов в Республика Бурятия, финансовые услуги в Республика Бурятия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-dagestan</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика дагестан, рефинансирование кредитов в Республика Дагестан, финансовые услуги в Республика Дагестан</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-ingushetiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика ингушетия, рефинансирование кредитов в Республика Ингушетия, финансовые услуги в Республика Ингушетия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kabardino-balkarskaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк кабардино-балкарская республика, рефинансирование кредитов в Кабардино-Балкарская Республика, финансовые услуги в Кабардино-Балкарская Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-kalmykiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика калмыкия, рефинансирование кредитов в Республика Калмыкия, финансовые услуги в Республика Калмыкия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/karachaevo-cherkesskaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк карачаево-черкесская республика, рефинансирование кредитов в Карачаево-Черкесская Республика, финансовые услуги в Карачаево-Черкесская Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-kareliya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика карелия, рефинансирование кредитов в Республика Карелия, финансовые услуги в Республика Карелия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-komi</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика коми, рефинансирование кредитов в Республика Коми, финансовые услуги в Республика Коми</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-krym</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика крым, рефинансирование кредитов в Республика Крым, финансовые услуги в Республика Крым</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-mariy-el</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика марий эл, рефинансирование кредитов в Республика Марий Эл, финансовые услуги в Республика Марий Эл</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-mordoviya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика мордовия, рефинансирование кредитов в Республика Мордовия, финансовые услуги в Республика Мордовия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-sakha-yakutiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика саха (якутия), рефинансирование кредитов в Республика Саха (Якутия), финансовые услуги в Республика Саха (Якутия)</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-severnaya-osetiya---alaniya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика северная осетия — алания, рефинансирование кредитов в Республика Северная Осетия — Алания, финансовые услуги в Республика Северная Осетия — Алания</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-tatarstan</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика татарстан, рефинансирование кредитов в Республика Татарстан, финансовые услуги в Республика Татарстан</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-tyva</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика тыва, рефинансирование кредитов в Республика Тыва, финансовые услуги в Республика Тыва</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/udmurtskaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк удмуртская республика, рефинансирование кредитов в Удмуртская Республика, финансовые услуги в Удмуртская Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/respublika-khakasiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк республика хакасия, рефинансирование кредитов в Республика Хакасия, финансовые услуги в Республика Хакасия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/chechenskaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк чеченская республика, рефинансирование кредитов в Чеченская Республика, финансовые услуги в Чеченская Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/chuvashskaya-respublika---chuvashiya</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк чувашская республика — чувашия, рефинансирование кредитов в Чувашская Республика — Чувашия, финансовые услуги в Чувашская Республика — Чувашия</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/altayskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк алтайский край, рефинансирование кредитов в Алтайский край, финансовые услуги в Алтайский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/zabaykalьskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк забайкальский край, рефинансирование кредитов в Забайкальский край, финансовые услуги в Забайкальский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kamchatskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк камчатский край, рефинансирование кредитов в Камчатский край, финансовые услуги в Камчатский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/krasnodarskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк краснодарский край, рефинансирование кредитов в Краснодарский край, финансовые услуги в Краснодарский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/krasnoyarskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк красноярский край, рефинансирование кредитов в Красноярский край, финансовые услуги в Красноярский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/permskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк пермский край, рефинансирование кредитов в Пермский край, финансовые услуги в Пермский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/primorskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк приморский край, рефинансирование кредитов в Приморский край, финансовые услуги в Приморский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/stavropolьskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ставропольский край, рефинансирование кредитов в Ставропольский край, финансовые услуги в Ставропольский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/khabarovskiy-kray</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк хабаровский край, рефинансирование кредитов в Хабаровский край, финансовые услуги в Хабаровский край</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/amurskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк амурская область, рефинансирование кредитов в Амурская область, финансовые услуги в Амурская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/arkhangelьskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк архангельская область, рефинансирование кредитов в Архангельская область, финансовые услуги в Архангельская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/astrakhanskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк астраханская область, рефинансирование кредитов в Астраханская область, финансовые услуги в Астраханская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/belgorodskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк белгородская область, рефинансирование кредитов в Белгородская область, финансовые услуги в Белгородская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/bryanskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк брянская область, рефинансирование кредитов в Брянская область, финансовые услуги в Брянская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/vladimirskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк владимирская область, рефинансирование кредитов в Владимирская область, финансовые услуги в Владимирская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/volgogradskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк волгоградская область, рефинансирование кредитов в Волгоградская область, финансовые услуги в Волгоградская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/vologodskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк вологодская область, рефинансирование кредитов в Вологодская область, финансовые услуги в Вологодская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/voronezhskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк воронежская область, рефинансирование кредитов в Воронежская область, финансовые услуги в Воронежская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/ivanovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ивановская область, рефинансирование кредитов в Ивановская область, финансовые услуги в Ивановская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/irkutskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк иркутская область, рефинансирование кредитов в Иркутская область, финансовые услуги в Иркутская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kaliningradskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк калининградская область, рефинансирование кредитов в Калининградская область, финансовые услуги в Калининградская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kaluzhskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк калужская область, рефинансирование кредитов в Калужская область, финансовые услуги в Калужская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kemerovskaya-oblastь---kuzbass</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк кемеровская область — кузбасс, рефинансирование кредитов в Кемеровская область — Кузбасс, финансовые услуги в Кемеровская область — Кузбасс</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kirovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк кировская область, рефинансирование кредитов в Кировская область, финансовые услуги в Кировская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kostromskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк костромская область, рефинансирование кредитов в Костромская область, финансовые услуги в Костромская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kurganskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк курганская область, рефинансирование кредитов в Курганская область, финансовые услуги в Курганская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/kurskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк курская область, рефинансирование кредитов в Курская область, финансовые услуги в Курская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/leningradskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ленинградская область, рефинансирование кредитов в Ленинградская область, финансовые услуги в Ленинградская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/lipetskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк липецкая область, рефинансирование кредитов в Липецкая область, финансовые услуги в Липецкая область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/magadanskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк магаданская область, рефинансирование кредитов в Магаданская область, финансовые услуги в Магаданская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/moskovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк московская область, рефинансирование кредитов в Московская область, финансовые услуги в Московская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/murmanskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк мурманская область, рефинансирование кредитов в Мурманская область, финансовые услуги в Мурманская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/nizhegorodskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк нижегородская область, рефинансирование кредитов в Нижегородская область, финансовые услуги в Нижегородская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/novgorodskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк новгородская область, рефинансирование кредитов в Новгородская область, финансовые услуги в Новгородская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/novosibirskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк новосибирская область, рефинансирование кредитов в Новосибирская область, финансовые услуги в Новосибирская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/omskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк омская область, рефинансирование кредитов в Омская область, финансовые услуги в Омская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/orenburgskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк оренбургская область, рефинансирование кредитов в Оренбургская область, финансовые услуги в Оренбургская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/orlovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк орловская область, рефинансирование кредитов в Орловская область, финансовые услуги в Орловская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/penzenskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк пензенская область, рефинансирование кредитов в Пензенская область, финансовые услуги в Пензенская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/pskovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк псковская область, рефинансирование кредитов в Псковская область, финансовые услуги в Псковская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/rostovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ростовская область, рефинансирование кредитов в Ростовская область, финансовые услуги в Ростовская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/ryazanskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк рязанская область, рефинансирование кредитов в Рязанская область, финансовые услуги в Рязанская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/samarskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк самарская область, рефинансирование кредитов в Самарская область, финансовые услуги в Самарская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/saratovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк саратовская область, рефинансирование кредитов в Саратовская область, финансовые услуги в Саратовская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/sakhalinskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк сахалинская область, рефинансирование кредитов в Сахалинская область, финансовые услуги в Сахалинская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/sverdlovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк свердловская область, рефинансирование кредитов в Свердловская область, финансовые услуги в Свердловская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/smolenskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк смоленская область, рефинансирование кредитов в Смоленская область, финансовые услуги в Смоленская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/tambovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк тамбовская область, рефинансирование кредитов в Тамбовская область, финансовые услуги в Тамбовская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/tverskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк тверская область, рефинансирование кредитов в Тверская область, финансовые услуги в Тверская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/tomskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк томская область, рефинансирование кредитов в Томская область, финансовые услуги в Томская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/tulьskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк тульская область, рефинансирование кредитов в Тульская область, финансовые услуги в Тульская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/tyumenskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк тюменская область, рефинансирование кредитов в Тюменская область, финансовые услуги в Тюменская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/ulьyanovskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ульяновская область, рефинансирование кредитов в Ульяновская область, финансовые услуги в Ульяновская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/chelyabinskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк челябинская область, рефинансирование кредитов в Челябинская область, финансовые услуги в Челябинская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/yaroslavskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ярославская область, рефинансирование кредитов в Ярославская область, финансовые услуги в Ярославская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/moskva</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк москва, рефинансирование кредитов в Москва, финансовые услуги в Москва</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/sankt-peterburg</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк санкт-петербург, рефинансирование кредитов в Санкт-Петербург, финансовые услуги в Санкт-Петербург</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/sevastopolь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк севастополь, рефинансирование кредитов в Севастополь, финансовые услуги в Севастополь</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/evreyskaya-avtonomnaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк еврейская автономная область, рефинансирование кредитов в Еврейская автономная область, финансовые услуги в Еврейская автономная область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/nenetskiy-avtonomnyy-okrug</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ненецкий автономный округ, рефинансирование кредитов в Ненецкий автономный округ, финансовые услуги в Ненецкий автономный округ</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/khanty-mansiyskiy-avtonomnyy-okrug---yugra</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ханты-мансийский автономный округ — югра, рефинансирование кредитов в Ханты-Мансийский автономный округ — Югра, финансовые услуги в Ханты-Мансийский автономный округ — Югра</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/chukotskiy-avtonomnyy-okrug</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк чукотский автономный округ, рефинансирование кредитов в Чукотский автономный округ, финансовые услуги в Чукотский автономный округ</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/yamalo-nenetskiy-avtonomnyy-okrug</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк ямало-ненецкий автономный округ, рефинансирование кредитов в Ямало-Ненецкий автономный округ, финансовые услуги в Ямало-Ненецкий автономный округ</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/donetskaya-narodnaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк донецкая народная республика, рефинансирование кредитов в Донецкая Народная Республика, финансовые услуги в Донецкая Народная Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/luganskaya-narodnaya-respublika</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк луганская народная республика, рефинансирование кредитов в Луганская Народная Республика, финансовые услуги в Луганская Народная Республика</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/zaporozhskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк запорожская область, рефинансирование кредитов в Запорожская область, финансовые услуги в Запорожская область</keywords>
  </url>
  <url>
    <loc>https://refbankuk.ru/khersonskaya-oblastь</loc>
    <lastmod>2025-08-17</lastmod>
    <priority>0.8</priority>
    <keywords>т банк херсонская область, рефинансирование кредитов в Херсонская область, финансовые услуги в Херсонская область</keywords>
  </url>
</urlset>
'''

# Парсинг sitemap
lines = [line.strip() for line in sitemap_content.split('\n') if line.strip()]

regions = []

i = 0
while i < len(lines):
    loc = lines[i]
    if not loc.startswith('https'):
        i += 1
        continue
    lastmod = lines[i+1]
    priority = lines[i+2]
    keywords = lines[i+3]
    i += 4

    if loc == 'https://refbankuk.ru/':
        continue

    slug = loc.split('/')[-1]

    keyword_parts = keywords.split(', ')
    if len(keyword_parts) >= 3:
        third_part = keyword_parts[2]
        match = re.search(r' в (.*)$', third_part)
        if match:
            region_full = match.group(1)
        else:
            region_full = third_part.split(' в ')[1] if ' в ' in third_part else slug.replace('-', ' ').title()
    else:
        region_full = slug.replace('-', ' ').title()

    regions.append((slug, region_full, keywords))

# Создание папки для регионов
os.makedirs('./regions', exist_ok=True)

# Генерация страниц
for slug, region_full, keywords in regions:
    modified_html = index_html

    # Замена главного заголовка
    modified_html = re.sub(r'Ваши финансы с Т‑Банком: карты, вклады, инвестиции и защита', f'Ваши финансы с Т‑Банком в {region_full}: карты, вклады, инвестиции и защита', modified_html)

    # Замена описаний продуктов (добавляем ' в {region_full}' в конец описаний)
    product_descriptions = [
        r'Дебетовая карта с кешбэком до 30% и бесплатным обслуживанием для покупок и путешествий.',
        r'Дебетовая карта без процентов, соответствующая принципам шариата.',
        r'Мобильная связь с бонусами и защитой от спама.',
        r'Начните инвестировать с 10 ₽ и получайте бонусы.',
        r'Удобное РКО для предпринимателей с бонусами.',
        r'Быстрая регистрация ИП или ООО с поддержкой.',
        r'Гибкие вклады с потенциально высокой доходностью.',
        r'Экономьте на топливе с кешбэком.',
        r'Автоматическое управление инвестициями для пассивного дохода.',
        r'Карьерные возможности с гибким графиком и бонусами.',
        r'Расширенные бонусы и привилегии для клиентов.',
        r'Снизьте ежемесячные платежи и переплату по кредитам.',
        r'Страхование автомобиля на выгодных условиях.',
        r'Надёжная защита для ипотечных заёмщиков.'
    ]
    for desc in product_descriptions:
        new_desc = desc.rstrip('.') + f' в {region_full}.'
        modified_html = modified_html.replace(desc, new_desc)

    # Замена в FAQ (добавляем ' в {region_full}' в вопросы и ответы)
    faq_questions = [
        r'Почему нужна Карта Т‑Банк Black?',
        r'Почему нужна Исламская карта Т‑Банка?',
        r'Почему нужен Т‑Мобайл?',
        r'Почему нужен Счёт для инвестиций?',
        r'Почему нужен Счёт для бизнеса?',
        r'Почему нужна Регистрация бизнеса?',
        r'Почему нужен Вклад от 2 месяцев?',
        r'Почему нужен Сервис Топливо?',
        r'Почему нужен Автоследование?',
        r'Почему нужна Работа в Т‑Банке?',
        r'Почему нужна Подписка Pro?',
        r'Почему нужно Рефинансирование кредитов?',
        r'Почему нужно Каско?',
        r'Почему нужно Страхование ипотеки?',
        r'Почему нужен Кредит наличными?',
        r'Почему нужна Пенсия на карту Т‑Банка?',
        r'Почему нужно Приложение Т‑Банка на iOS?'
    ]
    for q in faq_questions:
        new_q = q.rstrip('?') + f' в {region_full}?'
        modified_html = modified_html.replace(q, new_q)

    # В ответах FAQ добавляем ' в {region_full}' в конец
    modified_html = re.sub(r'(\.[^<]*)(</dd>)', r'\1 в {region_full}.\2', modified_html)

    # Замена футера
    modified_html = modified_html.replace('© 2025 T‑Bank Guide. Все права защищены.', f'© 2025 T‑Bank Guide {region_full}. Все права защищены.')

    # Интеграция ключевых слов в описание (например, в первый p)
    modified_html = re.sub(r'Подбирайте продукты с выгодой — кешбэк до 30%, бонусы за оформление и прозрачные условия.', f'Подбирайте продукты с выгодой — кешбэк до 30%, бонусы за оформление и прозрачные условия. Ключевые слова: {keywords}.', modified_html)

    # Сохранение файла
    with open(f'./regions/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(modified_html)

print("Страницы сгенерированы в папке ./regions/")</parameter
</xai:function_call
