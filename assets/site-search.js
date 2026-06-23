/* ============================================================
   Charles Research — site-wide search widget (rebuilt)
   Self-contained · simpler · more robust.
   Include via:  <script defer src="assets/site-search.js"></script>
                 or  ../assets/site-search.js  from a sub-page.
   ============================================================ */
(function () {
  if (window.__cknzSearchLoaded) return;
  window.__cknzSearchLoaded = true;

  // ---- 1 · CSS (vanilla, no CSS variables) ----
  var css = [
    /* 17 May 2026 — moved back to upper-right per user request so the
       search FAB no longer overlaps the dark-mode toggle (which lives at
       bottom-right, right:14px;bottom:14px). Offset 4rem from the top
       clears the sticky site-nav bar (top:0, ~3rem tall). z-index 1050
       sits below the nav (z:1100) so dropdown results never overlay the nav. */
    '.cknz-q { position:fixed; top:4rem; right:1rem; z-index:1050; max-width:300px; width:calc(100% - 2rem); font-family:Georgia,serif; }',
    /* Tap-to-open search icon — hidden on desktop, shown at the phone breakpoint below. */
    '.cknz-toggle { display:none; align-items:center; justify-content:center; width:42px; height:42px; padding:0; border:1px solid #d8b366; border-radius:50%; background:rgba(44,38,32,0.96); color:#d8b366; cursor:pointer; box-shadow:0 2px 8px rgba(0,0,0,0.28); -webkit-tap-highlight-color:transparent; }',
    '.cknz-toggle svg { width:20px; height:20px; display:block; }',
    '.cknz-q input { width:100%; padding:0.55rem 0.9rem 0.55rem 2.2rem; font-size:0.92rem; border:1px solid #5a4a32; border-radius:20px; background:rgba(255,250,240,0.97); color:#2c2620; box-shadow:0 2px 8px rgba(0,0,0,0.18); transition:all 0.15s; box-sizing:border-box; font-family:inherit; outline:none;',
    '  background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'%238a5a14\' stroke-width=\'2.4\' stroke-linecap=\'round\' stroke-linejoin=\'round\'%3E%3Ccircle cx=\'11\' cy=\'11\' r=\'7\'/%3E%3Cpath d=\'m20 20-3.5-3.5\'/%3E%3C/svg%3E");',
    '  background-repeat: no-repeat; background-position: 0.6rem center; background-size: 1.05rem 1.05rem;',
    '}',
    '.cknz-q input:focus { border-color:#d8b366; box-shadow:0 2px 14px rgba(212,160,23,0.32); background-color:#fff; }',
    '.cknz-q input::placeholder { color:#8a7858; font-style:italic; }',
    '.cknz-q .results { display:none; max-height:60vh; overflow-y:auto; margin-top:0.45rem; background:#fffaf0; border:1px solid #5a4a32; border-radius:6px; box-shadow:0 4px 14px rgba(0,0,0,0.22); }',
    '.cknz-q .results.open { display:block; }',
    '.cknz-q .r { display:block; padding:0.55rem 0.85rem; border-bottom:1px solid #ede4d0; text-decoration:none; color:#2c2620; }',
    '.cknz-q .r:last-child { border-bottom:none; }',
    '.cknz-q .r:hover, .cknz-q .r:focus { background:#f8ecc8; outline:none; }',
    '.cknz-q .r .k { display:inline-block; font-size:0.62rem; text-transform:uppercase; letter-spacing:0.05em; padding:1px 6px; border-radius:2px; background:#d8b366; color:#1f1a14; margin-right:0.45rem; vertical-align:middle; font-weight:700; }',
    '.cknz-q .r .k.person, .cknz-q .r .k.child { background:#4a6e34; color:#fff; }',
    '.cknz-q .r .k.civilwar { background:#a04030; color:#fff; }',
    '.cknz-q .r .k.charles { background:#b06820; color:#fff; }',
    '.cknz-q .r .k.immigration { background:#3a5a8c; color:#fff; }',
    '.cknz-q .r .k.germany { background:#4a6e34; color:#fff; }',
    '.cknz-q .r .k.town { background:#8a7858; color:#fff; }',
    '.cknz-q .r .k.theme { background:#6a5a8a; color:#fff; }',
    '.cknz-q .r .k.correspondence, .cknz-q .r .k.family { background:#8a6420; color:#fff; }',
    '.cknz-q .r .ttl { font-weight:700; color:#1f1a14; font-size:0.92rem; }',
    '.cknz-q .r .ds { font-size:0.78rem; color:#5a4a32; margin-top:0.15rem; line-height:1.4; }',
    '.cknz-q .r mark { background:#f1cf85; color:#1f1a14; padding:0 1px; border-radius:1px; }',
    '.cknz-q .empty { padding:0.85rem; font-size:0.85rem; color:#6a5a42; font-style:italic; text-align:center; }',
    '.cknz-q .meta { padding:0.4rem 0.8rem; font-size:0.72rem; color:#6a5a42; background:#f6ebd2; border-top:1px solid #ede4d0; font-style:italic; text-align:center; }',
    /* Phone-size pins the bar to the top-edge (just below the nav) so it
       doesn't sit on top of the dark-mode FAB at the bottom-right. */
    /* Phone (<=640px): collapse the search into a small tap-to-open icon so it
       no longer sits as a bar across the whole screen blocking the view. The
       full-width input bar only appears once .cknz-q gets the .expanded class. */
    '@media (max-width:768px) {',
    '  .cknz-q { top:3.4rem; right:0.55rem; left:auto; bottom:auto; width:auto; max-width:none; padding:0; background:transparent; border:none; box-shadow:none; }',
    '  .cknz-q .cknz-toggle { display:flex; }',
    '  .cknz-q input { display:none; }',
    '  .cknz-q.expanded { right:0.55rem; left:auto; width:min(88vw, 360px); }',
    '  .cknz-q.expanded .cknz-toggle { display:none; }',
    '  .cknz-q.expanded input { display:block; }',
    '  .cknz-q .results { max-height:50vh; margin-top:0.45rem; }',
    '}',
    '@media print { .cknz-q { display:none !important; } }'
  ].join('\n');
  var style = document.createElement('style');
  style.id = 'cknz-search-style';
  style.textContent = css;
  document.head.appendChild(style);

  // ---- 2 · Resolve search index URL relative to this script's location ----
  function ownScriptSrc() {
    var scripts = document.querySelectorAll('script[src]');
    for (var i = 0; i < scripts.length; i++) {
      var s = scripts[i].src;
      if (s && s.indexOf('site-search.js') !== -1) return s;
    }
    return null;
  }
  function searchIndexJsUrl() {
    var s = ownScriptSrc();
    if (s) {
      try { return new URL('search-index.js', s).href; } catch (e) {}
    }
    return 'assets/search-index.js';
  }
  function searchIndexJsonUrl() {
    var s = ownScriptSrc();
    if (s) {
      try { return new URL('../search-index.json', s).href; } catch (e) {}
    }
    return 'search-index.json';
  }

  // ---- 3 · Index loader ----
  // Two strategies: prefer the JSONP-style /assets/search-index.js (works on
  // file:// because <script> can load local files even when fetch can't),
  // fall back to fetching /search-index.json on http(s).
  var _indexPromise = null;
  function loadIndex() {
    if (_indexPromise) return _indexPromise;
    _indexPromise = new Promise(function (resolve, reject) {
      // If a previous load already populated the global, use it directly
      if (window.CKNZ_SEARCH_INDEX && window.CKNZ_SEARCH_INDEX.length) {
        return resolve(window.CKNZ_SEARCH_INDEX);
      }
      // Try the JS-wrapped index first (file:// safe)
      var s = document.createElement('script');
      s.src = searchIndexJsUrl();
      s.async = true;
      s.onload = function () {
        if (window.CKNZ_SEARCH_INDEX && window.CKNZ_SEARCH_INDEX.length) {
          resolve(window.CKNZ_SEARCH_INDEX);
        } else {
          // Loaded but no data — fall back to fetch
          fetchFallback(resolve, reject);
        }
      };
      s.onerror = function () { fetchFallback(resolve, reject); };
      document.head.appendChild(s);
    });
    _indexPromise.catch(function () { _indexPromise = null; }); // allow retry
    return _indexPromise;
  }

  function fetchFallback(resolve, reject) {
    if (!window.fetch) { reject(new Error('No fetch and no script index')); return; }
    fetch(searchIndexJsonUrl()).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    }).then(function (data) {
      window.CKNZ_SEARCH_INDEX = data;
      resolve(data);
    }).catch(function (err) { reject(err); });
  }

  // ---- 4 · Helpers ----
  function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  function escapeHtml(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' })[c];
    });
  }
  function highlight(text, q) {
    if (!q || !text) return escapeHtml(text || '');
    var re = new RegExp(escapeRe(q), 'gi');
    return escapeHtml(text).replace(re, function (m) { return '<mark>' + m + '</mark>'; });
  }
  function score(entry, ql) {
    var t = (entry.t || '').toLowerCase();
    var h = (entry.h || '').toLowerCase();
    var d = (entry.d || '').toLowerCase();
    var b = (entry.b || '').toLowerCase();
    var s = 0;
    if (h.indexOf(ql) === 0) s += 100;
    else if (h.indexOf(ql) !== -1) s += 60;
    if (t.indexOf(ql) !== -1) s += 30;
    if (d.indexOf(ql) !== -1) s += 20;
    if (b.indexOf(ql) !== -1) s += 5;
    return s;
  }
  function resolveUrl(u) {
    if (!u) return '#';
    if (/^https?:\/\//i.test(u) || u.charAt(0) === '/') return u;
    // Make relative URLs absolute against the site root by prefixing.
    // We assume the script is at site-root/assets/site-search.js, so we
    // can derive the site root from the script's own URL.
    var scripts = document.querySelectorAll('script[src]');
    for (var i = 0; i < scripts.length; i++) {
      var s = scripts[i].src;
      if (s && s.indexOf('site-search.js') !== -1) {
        try { return new URL('../' + u, s).href; } catch (e) {}
      }
    }
    return u;
  }

  // ---- 5 · UI ----
  var qWrap, qInput, qResults, qToggle;

  function inject() {
    if (qWrap) return;
    qWrap = document.createElement('div');
    qWrap.className = 'cknz-q';
    qWrap.setAttribute('role', 'search');

    // Phone-only icon that expands the search bar (see setExpanded()).
    qToggle = document.createElement('button');
    qToggle.type = 'button';
    qToggle.className = 'cknz-toggle';
    qToggle.setAttribute('aria-label', 'Open site search');
    qToggle.setAttribute('aria-expanded', 'false');
    qToggle.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';
    qWrap.appendChild(qToggle);

    qInput = document.createElement('input');
    qInput.type = 'search';
    qInput.placeholder = 'Search the site — names, places, documents…';
    qInput.setAttribute('aria-label', 'Search the site');
    qInput.autocomplete = 'off';
    qInput.spellcheck = false;
    qWrap.appendChild(qInput);

    qResults = document.createElement('div');
    qResults.className = 'results';
    qResults.setAttribute('role', 'listbox');
    qWrap.appendChild(qResults);

    document.body.appendChild(qWrap);
  }

  // ---- 6 · Search behavior ----
  var debounceTimer = null;
  function doSearch(q) {
    if (!qResults) return;
    if (!q || q.length < 2) {
      qResults.classList.remove('open');
      qResults.innerHTML = '';
      return;
    }
    qResults.innerHTML = '<div class="empty">Searching…</div>';
    qResults.classList.add('open');
    loadIndex().then(function (idx) {
      if (qInput.value !== q) return; // user already typed more
      var ql = q.toLowerCase();
      var hits = idx.map(function (e) { return { e: e, s: score(e, ql) }; })
                    .filter(function (x) { return x.s > 0; })
                    .sort(function (a, b) { return b.s - a.s; })
                    .slice(0, 12);
      if (!hits.length) {
        qResults.innerHTML = '<div class="empty">No matches for "' + escapeHtml(q) + '"</div>';
        return;
      }
      qResults.innerHTML = hits.map(function (x) {
        var e = x.e;
        var title = e.h || e.t || e.u;
        var desc = e.d || (e.b || '').slice(0, 140);
        var url = resolveUrl(e.u);
        return '<a class="r" href="' + escapeHtml(url) + '">'
          + '<span class="k ' + escapeHtml(e.k || '') + '">' + escapeHtml(e.k || '?') + '</span>'
          + '<span class="ttl">' + highlight(title, q) + '</span>'
          + (desc ? '<div class="ds">' + highlight(desc.slice(0, 160) + (desc.length > 160 ? '…' : ''), q) + '</div>' : '')
          + '</a>';
      }).join('') + '<div class="meta">' + hits.length + ' result' + (hits.length === 1 ? '' : 's') + ' · click to open</div>';
    }).catch(function (err) {
      console.error('site-search: index load failed', err);
      qResults.innerHTML = '<div class="empty">Search index could not be loaded.<br><small>Please reload the page.</small></div>';
    });
  }

  // Expand/collapse the phone search bar. A no-op visually on desktop, where
  // the toggle is hidden and the input is always shown.
  function setExpanded(on) {
    if (!qWrap) return;
    qWrap.classList.toggle('expanded', !!on);
    if (qToggle) qToggle.setAttribute('aria-expanded', on ? 'true' : 'false');
    if (on) {
      requestAnimationFrame(function () { try { qInput.focus(); } catch (e) {} });
    } else if (qResults) {
      qResults.classList.remove('open');
    }
  }

  function wire() {
    inject();

    // Tap the icon to reveal the search field; tap again to hide it.
    qToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      setExpanded(!qWrap.classList.contains('expanded'));
    });

    qInput.addEventListener('input', function () {
      clearTimeout(debounceTimer);
      var v = qInput.value;
      debounceTimer = setTimeout(function () { doSearch(v); }, 90);
    });
    qInput.addEventListener('focus', function () {
      if (qInput.value && qInput.value.length >= 2) doSearch(qInput.value);
    });
    document.addEventListener('click', function (e) {
      if (qWrap && !qWrap.contains(e.target)) {
        qResults.classList.remove('open');
        setExpanded(false);
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && qResults) {
        qResults.classList.remove('open');
        if (document.activeElement === qInput) qInput.blur();
        setExpanded(false);
      }
    });

    // Lazy-load the index only on the user's first interaction with the
    // search box (focus, click, or '/' shortcut). Saves ~236 KB for the
    // ~95% of visitors who never search. (Audit-fix pass, 8 May 2026.)
    var _indexWarmed = false;
    function warmOnce() {
      if (_indexWarmed) return;
      _indexWarmed = true;
      loadIndex().catch(function () {});
    }
    if (qInput) {
      qInput.addEventListener('focus', warmOnce, { once: true });
      qInput.addEventListener('mousedown', warmOnce, { once: true });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && document.activeElement !== qInput) {
        e.preventDefault();
        if (qInput) { setExpanded(true); warmOnce(); }
      }
    });

    window.siteSearch = doSearch;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
