/* ============================================================
   Charles Research — figure lightbox (simplified)
   Click any figure containing one of the signature SVGs to open
   a fullscreen view. Self-contained: include via
     <script defer src="assets/figure-lightbox.js"></script>
   ============================================================ */
(function () {
  if (window.__cknzLightboxLoaded) return;
  window.__cknzLightboxLoaded = true;

  // ---- 1 · CSS ----
  var css = [
    '.cknz-lb {',
    '  position:fixed; left:0; top:0; right:0; bottom:0;',
    '  width:100vw; height:100vh;',
    '  background:rgba(31,26,20,0.94);',
    '  z-index:99999;',
    '  display:flex; flex-direction:column;',
    '  align-items:stretch; justify-content:stretch;',
    '  cursor:zoom-out;',
    '  animation:cknz-lb-in 0.18s ease-out;',
    '}',
    '@keyframes cknz-lb-in { from {opacity:0;} to {opacity:1;} }',
    '.cknz-lb-bar {',
    '  flex:0 0 auto; padding:0.6rem 1rem;',
    '  background:rgba(0,0,0,0.55);',
    '  border-bottom:1px solid rgba(212,160,23,0.4);',
    '  color:#f6f1e7; font-family:Georgia,serif; font-size:0.9rem;',
    '  display:flex; align-items:center; gap:1rem;',
    '  cursor:default;',
    '}',
    '.cknz-lb-bar .ttl { flex:1; min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; color:#d4a017; font-weight:700; letter-spacing:0.04em; }',
    '.cknz-lb-bar .hint { font-size:0.78rem; color:#c8b896; font-style:italic; flex:0 0 auto; }',
    '.cknz-lb-bar a, .cknz-lb-bar button {',
    '  background:rgba(255,250,240,0.08); color:#f6f1e7;',
    '  border:1px solid rgba(212,160,23,0.4);',
    '  border-radius:3px; padding:0.3rem 0.7rem;',
    '  font-family:monospace; font-size:0.82rem;',
    '  cursor:pointer; text-decoration:none;',
    '  transition:all 0.12s ease; flex:0 0 auto;',
    '}',
    '.cknz-lb-bar a:hover, .cknz-lb-bar button:hover { background:rgba(212,160,23,0.22); border-color:#d4a017; }',
    '.cknz-lb-bar button.close { padding:0.25rem 0.65rem; font-size:1.2rem; line-height:1; }',
    '.cknz-lb-stage {',
    '  flex:1 1 auto; position:relative; overflow:hidden;',
    '  cursor:zoom-out;',
    '  display:flex; align-items:center; justify-content:center;',
    '  padding:1.5rem;',
    '}',
    '.cknz-lb-stage img {',
    '  max-width:100%; max-height:100%;',
    '  width:auto; height:auto;',
    '  object-fit:contain;',
    '  background:#fffaf0;',
    '  border:1px solid rgba(212,160,23,0.5);',
    '  border-radius:3px;',
    '  filter:drop-shadow(0 6px 24px rgba(0,0,0,0.55));',
    '  cursor:zoom-in;',
    '}',
    '.cknz-lb-stage img.zoomed {',
    '  max-width:none; max-height:none;',
    '  width:auto; height:auto;',
    '  cursor:zoom-out;',
    '}',
    '@media (max-width:720px) {',
    '  .cknz-lb-bar { padding:0.5rem 0.6rem; gap:0.4rem; font-size:0.82rem; }',
    '  .cknz-lb-bar .hint { display:none; }',
    '  .cknz-lb-stage { padding:0.6rem; }',
    '}',
    '@media print { .cknz-lb { display:none !important; } }',
    '/* zoom button on figures */',
    'figure.zoomable, figure[data-zoomable] { position:relative; }',
    'button.cknz-zoom-btn {',
    '  position:absolute; top:0.7rem; right:0.7rem;',
    '  width:38px; height:38px;',
    '  display:inline-flex; align-items:center; justify-content:center;',
    '  background:#2c2620;',
    '  color:#f6e6b8; font-size:1.35rem; font-weight:700;',
    '  font-family:inherit; line-height:1; padding:0;',
    '  border:1.5px solid #d4a017;',
    '  border-radius:4px;',
    '  box-shadow:0 2px 8px rgba(0,0,0,0.4);',
    '  cursor:zoom-in;',
    '  transition:all 0.15s ease;',
    '  z-index:5;',
    '}',
    'button.cknz-zoom-btn:hover, button.cknz-zoom-btn:focus-visible {',
    '  background:#d4a017; color:#1f1a14;',
    '  border-color:#1f1a14;',
    '  transform:scale(1.08); outline:none;',
    '  box-shadow:0 3px 10px rgba(0,0,0,0.45);',
    '}'
  ].join('\n');
  var style = document.createElement('style');
  style.id = 'cknz-lightbox-style';
  style.textContent = css;
  document.head.appendChild(style);

  // ---- 2 · openLightbox ----
  function openLightbox(svgSrc, title) {
    closeLightbox();
    var lb = document.createElement('div');
    lb.className = 'cknz-lb';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', title || 'Figure detail');

    var bar = document.createElement('div');
    bar.className = 'cknz-lb-bar';

    var ttl = document.createElement('span');
    ttl.className = 'ttl';
    ttl.textContent = title || 'Figure';
    bar.appendChild(ttl);

    var hint = document.createElement('span');
    hint.className = 'hint';
    hint.textContent = 'click image to toggle 100% · esc to close';
    bar.appendChild(hint);

    var dl = document.createElement('a');
    dl.href = svgSrc;
    dl.setAttribute('download', '');
    dl.textContent = 'DOWNLOAD';
    bar.appendChild(dl);

    var openTab = document.createElement('a');
    openTab.href = svgSrc;
    openTab.target = '_blank';
    openTab.rel = 'noopener';
    openTab.textContent = 'OPEN IN TAB';
    bar.appendChild(openTab);

    var close = document.createElement('button');
    close.type = 'button';
    close.className = 'close';
    close.setAttribute('aria-label', 'Close');
    close.textContent = '×';
    close.addEventListener('click', function (e) { e.stopPropagation(); closeLightbox(); });
    bar.appendChild(close);

    lb.appendChild(bar);

    var stage = document.createElement('div');
    stage.className = 'cknz-lb-stage';
    var img = document.createElement('img');
    img.src = svgSrc;
    img.alt = title || 'Figure';
    img.addEventListener('click', function (e) {
      e.stopPropagation();
      img.classList.toggle('zoomed');
    });
    stage.appendChild(img);
    lb.appendChild(stage);

    // Backdrop click closes (but not on the image itself or the bar)
    lb.addEventListener('click', function (e) {
      if (e.target === lb || e.target === stage) closeLightbox();
    });

    document.body.appendChild(lb);
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
    document.addEventListener('keydown', escListener);
  }

  function escListener(e) {
    if (e.key === 'Escape') closeLightbox();
  }
  function closeLightbox() {
    var existing = document.querySelector('.cknz-lb');
    if (existing) existing.remove();
    document.documentElement.style.overflow = '';
    document.body.style.overflow = '';
    document.removeEventListener('keydown', escListener);
  }

  // ---- 3 · Wire figures ----
  var SIGNATURES = [
    'surname-trail.svg', 'life-timeline.svg', 'candidate-funnel.svg',
    'research-arc.svg', 'family-poster.svg', 'og-card.svg'
  ];

  function getFigSrc(fig) {
    var obj = fig.querySelector('object[data]');
    if (obj) {
      var d = obj.getAttribute('data');
      if (d) return d;
    }
    var img = fig.querySelector('img[src]');
    if (img) {
      var s = img.getAttribute('src');
      if (s) return s;
    }
    return '';
  }

  function getFigTitle(fig) {
    var t = fig.getAttribute('aria-label') || '';
    var cap = fig.querySelector('figcaption');
    if (!t && cap) {
      var strong = cap.querySelector('strong');
      t = strong ? strong.textContent.trim() : cap.textContent.trim().slice(0, 80);
    }
    if (!t) {
      // Try the eyebrow div above the object (used on index.html)
      var eyebrow = fig.querySelector(':scope > div');
      if (eyebrow) t = eyebrow.textContent.trim().slice(0, 80);
    }
    return t || 'Figure';
  }

  function shouldZoom(src) {
    if (!src) return false;
    for (var i = 0; i < SIGNATURES.length; i++) {
      if (src.indexOf(SIGNATURES[i]) !== -1) return true;
    }
    return false;
  }

  // Inline an <object>-embedded SVG so its <a> links work natively in the
  // parent document. Two strategies, file://-safe order:
  //   1) Look up the SVG markup in window.CKNZ_INLINE_SVGS (loaded by
  //      <script src="assets/figures/inline-svgs.js">). Works on file://.
  //   2) Fall back to fetch() (works on http(s) but blocked on file://).
  function fileNameOf(src) {
    var m = (src || '').match(/([^\/]+\.svg)(?:\?|#|$)/i);
    return m ? m[1] : src;
  }
  function applyInlineSvg(svgText, src, obj) {
    try {
      var doc = new DOMParser().parseFromString(svgText, 'image/svg+xml');
      var svg = doc.documentElement;
      if (!svg || svg.tagName.toLowerCase() !== 'svg') return false;
      if (!svg.hasAttribute('width')) svg.setAttribute('width', '100%');
      if (!svg.hasAttribute('height')) svg.setAttribute('height', 'auto');
      svg.style.display = 'block';
      svg.style.maxWidth = '100%';
      svg.style.height = 'auto';
      // Resolve relative <a href> against the SVG's URL so links still point
      // at the correct page from any embedding location, then drop target="_top".
      var XLINK = 'http://www.w3.org/1999/xlink';
      var anchors = svg.querySelectorAll('a');
      Array.prototype.forEach.call(anchors, function (a) {
        var href = a.getAttribute('href') || a.getAttributeNS(XLINK, 'href');
        if (!href) return;
        if (!/^(https?:|mailto:|tel:|#|\/)/i.test(href)) {
          try {
            var resolved = new URL(href, new URL(src, location.href).href).href;
            a.setAttribute('href', resolved);
            a.setAttributeNS(XLINK, 'href', resolved);
          } catch (e) { /* keep original */ }
        }
        a.removeAttribute('target');
      });
      var imported = document.importNode(svg, true);
      obj.parentNode.replaceChild(imported, obj);
      return true;
    } catch (e) {
      console.warn('SVG inline parse failed', src, e);
      return false;
    }
  }
  function inlineSvgInObject(obj, fig, title) {
    var src = obj.getAttribute('data');
    if (!src) return;
    var fileName = fileNameOf(src);
    // Strategy 1 — JS bundle (file://-safe)
    if (window.CKNZ_INLINE_SVGS && window.CKNZ_INLINE_SVGS[fileName]) {
      applyInlineSvg(window.CKNZ_INLINE_SVGS[fileName], src, obj);
      return;
    }
    // Strategy 2 — fetch fallback (only works on http(s))
    if (!window.fetch) return;
    fetch(src).then(function (r) {
      return r.ok ? r.text() : Promise.reject(new Error('HTTP ' + r.status));
    }).then(function (svgText) {
      applyInlineSvg(svgText, src, obj);
    }).catch(function (err) {
      console.warn('Could not inline SVG via fetch', src, err);
    });
  }

  function wireFigures() {
    var figs = document.querySelectorAll('figure');
    Array.prototype.forEach.call(figs, function (fig) {
      if (fig.__cknzWired) return;
      var src = getFigSrc(fig);
      if (!shouldZoom(src) && !fig.classList.contains('zoomable') && !fig.hasAttribute('data-zoomable')) return;
      fig.__cknzWired = true;
      fig.classList.add('zoomable');

      var title = getFigTitle(fig);

      // If the figure embeds via <object>, replace it with inline SVG so
      // its internal <a> links work natively in the parent document.
      var obj = fig.querySelector('object[type="image/svg+xml"][data]');
      if (obj && shouldZoom(obj.getAttribute('data'))) {
        inlineSvgInObject(obj, fig, title);
      }

      // Add the explicit zoom button
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'cknz-zoom-btn';
      btn.setAttribute('aria-label', title + ' — click to enlarge');
      btn.title = 'Click to enlarge';
      btn.textContent = '⤢';
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        openLightbox(src, title);
      });
      fig.appendChild(btn);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wireFigures);
  } else {
    wireFigures();
  }

  window.cknzLightbox = { open: openLightbox, close: closeLightbox, wire: wireFigures };
})();
