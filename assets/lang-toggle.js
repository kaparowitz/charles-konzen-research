/* ============================================================
   lang-toggle.js
   Charles Research · added 28 Jun 2026 · rev 2 (relative links)
   ------------------------------------------------------------
   Mounts a small EN | DE flag switcher into the site header/nav,
   pinned TOP-RIGHT, so German visitors can jump to the German
   (/de/) mirror of the page they are reading — and back. The host
   nav gets a `nav-has-lang` class that reserves right-edge padding,
   so the switch never overlaps the menu buttons. If a page has no
   nav, the switch falls back to a fixed top-right button.

   When a page has no German translation yet, the DE side is shown
   dimmed and does nothing (you stay on the current page) rather
   than redirecting to the German homepage.

   Links are built as RELATIVE paths (origin-independent), so the
   toggle works the same whether the site is opened locally
   (file://), from a subfolder, or served at the domain root on
   Netlify. The path from the current page to the site root is
   discovered from this script's own src ("assets/…", "../assets/…",
   "../../assets/…"), so no absolute "/…" paths are ever used.

   Behaviour
   ---------
   • On an English page  → DE links to the German mirror de/<path>
     IF translated (listed in window.CHARLES_DE_PAGES from
     de-pages.js); otherwise DE links to the German homepage
     de/index.html (graceful fallback).
   • On a German page (/de/…) → EN links back to the English
     original, which always exists.
   • The current language is marked and is not a link.
   Hidden in print.
   ============================================================ */
(function () {
  'use strict';

  // ---- path from current page to the site root (from this script's src) ----
  function rootPrefix() {
    var ss = document.getElementsByTagName('script');
    for (var i = 0; i < ss.length; i++) {
      var src = ss[i].getAttribute('src') || '';
      var idx = src.indexOf('assets/lang-toggle.js');
      if (idx !== -1) return src.slice(0, idx);   // "", "../", "../../", …
    }
    return '';
  }
  var ROOTP = rootPrefix();
  var DEPTH = (ROOTP.match(/\.\.\//g) || []).length;

  // ---- current page expressed relative to the site root --------------------
  var pn = location.pathname || '/';
  if (pn === '') pn = '/';
  if (pn.charAt(pn.length - 1) === '/') pn += 'index.html';
  var segs = pn.split('/').filter(Boolean);
  var pageFromRoot = segs.slice(Math.max(0, segs.length - (DEPTH + 1))).join('/');
  if (!pageFromRoot) pageFromRoot = 'index.html';

  var isDE = (pageFromRoot === 'de') || (pageFromRoot.indexOf('de/') === 0);
  var enRel = isDE ? pageFromRoot.replace(/^de\//, '') : pageFromRoot;
  if (enRel === '' || enRel === 'de') enRel = 'index.html';

  var manifest = window.CHARLES_DE_PAGES || [];
  function hasDE(p) { return manifest.indexOf(p) !== -1; }

  var deAvailable = isDE ? true : hasDE(enRel);
  var deRel = deAvailable ? ('de/' + enRel) : 'de/index.html';

  // ---- relative-path helpers ----------------------------------------------
  function dirname(p) { var i = p.lastIndexOf('/'); return i === -1 ? '' : p.slice(0, i); }
  function relpath(target, base) {
    var t = target.split('/').filter(Boolean);
    var b = base.split('/').filter(Boolean);
    var i = 0;
    while (i < t.length && i < b.length && t[i] === b[i]) i++;
    var parts = [];
    for (var k = i; k < b.length; k++) parts.push('..');
    parts = parts.concat(t.slice(i));
    return parts.join('/') || '.';
  }
  var curDir = dirname(pageFromRoot);
  var enHref = relpath(enRel, curDir);
  var deHref = relpath(deRel, curDir);

  // ---- inline SVG flags (render identically on every OS) -------------------
  var FLAG_EN =
    '<svg class="lt-flag" viewBox="0 0 60 30" width="20" height="12" aria-hidden="true" focusable="false">' +
    '<clipPath id="ltuk"><rect width="60" height="30"/></clipPath>' +
    '<g clip-path="url(#ltuk)">' +
    '<rect width="60" height="30" fill="#012169"/>' +
    '<path d="M0,0 60,30 M60,0 0,30" stroke="#fff" stroke-width="6"/>' +
    '<path d="M0,0 60,30 M60,0 0,30" stroke="#C8102E" stroke-width="4"/>' +
    '<path d="M30,0 V30 M0,15 H60" stroke="#fff" stroke-width="10"/>' +
    '<path d="M30,0 V30 M0,15 H60" stroke="#C8102E" stroke-width="6"/>' +
    '</g></svg>';
  var FLAG_DE =
    '<svg class="lt-flag" viewBox="0 0 5 3" width="20" height="12" aria-hidden="true" focusable="false">' +
    '<rect width="5" height="3" y="0" fill="#000"/>' +
    '<rect width="5" height="2" y="1" fill="#D00"/>' +
    '<rect width="5" height="1" y="2" fill="#FFCE00"/>' +
    '</svg>';

  // ---- styles (one-shot) ---------------------------------------------------
  function injectStyles() {
    if (document.getElementById('lang-toggle-styles')) return;
    var s = document.createElement('style');
    s.id = 'lang-toggle-styles';
    s.textContent =
      /* host nav reserves space on its right so the switch never overlaps the menu buttons */
      '.nav-has-lang{position:relative;padding-right:7rem;}' +
      '.lang-toggle-fab{position:absolute;top:.45rem;right:.6rem;z-index:60;' +
      'display:inline-flex;align-items:stretch;overflow:hidden;' +
      'background:var(--bg-card,#fffaf0);' +
      'border:1px solid var(--border-medium,#a88a4a);border-radius:999px;' +
      'box-shadow:0 2px 8px rgba(0,0,0,.22);' +
      'font:600 11px/1 var(--font-ui,system-ui,sans-serif);' +
      'letter-spacing:.04em;text-transform:uppercase;}' +
      /* fallback when no host nav is found on the page */
      '.lang-toggle-fab.is-floating{position:fixed;top:.5rem;right:.6rem;z-index:1101;}' +
      '.lang-toggle-fab .lt-seg{display:inline-flex;align-items:center;gap:.35rem;' +
      'padding:.4rem .55rem;color:var(--text-body,#2c2620);text-decoration:none;' +
      'border:none;background:transparent;cursor:pointer;' +
      'transition:background .18s ease,color .18s ease;}' +
      '.lang-toggle-fab .lt-seg + .lt-seg{border-left:1px solid var(--border-medium,#a88a4a);}' +
      '.lang-toggle-fab .lt-seg:hover{background:var(--brand,#d8b366);color:#1c1710;}' +
      '.lang-toggle-fab .lt-seg.is-current{background:var(--brand-dark,#8a6420);color:#fff;cursor:default;}' +
      '.lang-toggle-fab .lt-seg.is-current:hover{background:var(--brand-dark,#8a6420);color:#fff;}' +
      '.lang-toggle-fab .lt-seg.lt-na{opacity:.4;cursor:not-allowed;}' +
      '.lang-toggle-fab .lt-seg.lt-na:hover{background:transparent;color:var(--text-body,#2c2620);}' +
      '.lang-toggle-fab .lt-flag{display:block;border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.12);}' +
      '.lang-toggle-fab .lt-seg:focus-visible{outline:2px solid var(--brand,#d8b366);outline-offset:2px;}' +
      '@media (max-width:720px){.nav-has-lang{padding-right:6rem;}' +
      '.lang-toggle-fab{top:.4rem;right:.5rem;}.lang-toggle-fab .lt-seg{padding:.35rem .45rem;}}' +
      '@media print{.lang-toggle-fab{display:none!important;}}';
    document.head.appendChild(s);
  }

  // ---- build & mount -------------------------------------------------------
  function seg(opts) {
    var el;
    if (opts.current) {
      el = document.createElement('span');
      el.className = 'lt-seg is-current';
      el.setAttribute('aria-current', 'true');
    } else {
      el = document.createElement('a');
      el.className = 'lt-seg';
      el.href = opts.href;
      el.title = opts.title;
    }
    el.innerHTML = opts.flag + '<span class="lt-label">' + opts.label + '</span>';
    return el;
  }

  function build() {
    injectStyles();
    var wrap = document.createElement('div');
    wrap.className = 'lang-toggle-fab';
    wrap.setAttribute('role', 'navigation');
    wrap.setAttribute('aria-label', 'Language / Sprache');

    wrap.appendChild(seg({
      current: !isDE, href: enHref, flag: FLAG_EN, label: 'EN',
      title: 'View this page in English'
    }));

    if (isDE || deAvailable) {
      // German version of THIS page exists → switch in place
      wrap.appendChild(seg({
        current: isDE, href: deHref, flag: FLAG_DE, label: 'DE',
        title: 'Diese Seite auf Deutsch ansehen'
      }));
    } else {
      // Not translated yet → stay on the current page (no jump to the
      // German homepage); shown dimmed with an explanatory tooltip.
      var na = document.createElement('span');
      na.className = 'lt-seg lt-na';
      na.setAttribute('aria-disabled', 'true');
      na.title = 'Diese Seite ist noch nicht auf Deutsch verfügbar';
      na.innerHTML = FLAG_DE + '<span class="lt-label">DE</span>';
      wrap.appendChild(na);
    }

    // Mount into the site header/nav (top-right); fall back to a fixed
    // floating button only if no nav is present on the page.
    var nav = document.querySelector('#tabs, nav.tabs, .site-nav-shared, .de-topbar');
    if (nav) {
      nav.classList.add('nav-has-lang');
      nav.appendChild(wrap);
    } else {
      wrap.classList.add('is-floating');
      document.body.appendChild(wrap);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build, { once: true });
  } else {
    build();
  }
})();
