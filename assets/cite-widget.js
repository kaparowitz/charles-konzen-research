/* ============================================================
   Cite-this-page widget — Charles Research
   Reads <title>, canonical URL, and dateModified (from JSON-LD
   when present, else <meta name="last-modified">, else today)
   and renders Chicago / NGSQ / MLA citations into the footer.
   ============================================================ */
(function () {
  function escHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c];
    });
  }
  function fmtDateLong(iso) {
    var d = iso ? new Date(iso) : new Date();
    if (isNaN(d.getTime())) d = new Date();
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  }
  function fmtDateShort(iso) {
    var d = iso ? new Date(iso) : new Date();
    if (isNaN(d.getTime())) d = new Date();
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }
  function fmtDateIso(iso) {
    var d = iso ? new Date(iso) : new Date();
    if (isNaN(d.getTime())) d = new Date();
    return d.toISOString().slice(0, 10);
  }
  function pageTitle() {
    var t = (document.title || 'Charles Research')
      .replace(/\s*[—–|]\s*Charles Research\s*$/i, '')
      .trim();
    if (!t || /^Charles Research/i.test(t)) {
      return 'Charles Research: A Genealogical Investigation';
    }
    return t;
  }
  function canonicalUrl() {
    var l = document.querySelector('link[rel="canonical"]');
    if (l && l.href) return l.href;
    return location.origin + location.pathname;
  }
  function dateModified() {
    var ld = document.querySelector('script[type="application/ld+json"]');
    if (ld) {
      try {
        var data = JSON.parse(ld.textContent);
        var stack = [data];
        while (stack.length) {
          var n = stack.pop();
          if (!n) continue;
          if (Array.isArray(n)) { for (var i = 0; i < n.length; i++) stack.push(n[i]); continue; }
          if (typeof n === 'object') {
            if (n.dateModified) return n.dateModified;
            if (n['@graph']) stack.push(n['@graph']);
            for (var k in n) if (n[k] && typeof n[k] === 'object') stack.push(n[k]);
          }
        }
      } catch (e) { /* ignore */ }
    }
    var m = document.querySelector('meta[name="last-modified"]');
    if (m && m.content) return m.content;
    return null; // -> today
  }

  function buildCitations(ctx) {
    var authorChicago = 'Johnson, Jed, with Peter Schräder';
    var authorMla     = 'Johnson, Jed, and Peter Schräder';
    var title = ctx.pageTitle;
    var siteTitle = 'Charles Research: A Genealogical Investigation';
    var url = ctx.url;
    var lastRev = fmtDateLong(ctx.dateMod);
    var accessed = fmtDateLong(new Date().toISOString());
    var year = (ctx.dateMod ? new Date(ctx.dateMod) : new Date()).getFullYear() || 2026;
    var samePage = (title === siteTitle || /^Charles Research/i.test(title));

    var chicago = samePage
      ? authorChicago + '. "' + siteTitle + '." Last revised ' + lastRev + '. ' + url + ' (accessed ' + accessed + ').'
      : authorChicago + '. "' + title + '." ' + siteTitle + '. Last revised ' + lastRev + '. ' + url + ' (accessed ' + accessed + ').';

    var ngsq = authorChicago + ', "' + title + '," ' + siteTitle + ' (database online), ' + url + ' : accessed ' + accessed + ', last revised ' + lastRev + '.';

    var mla = samePage
      ? authorMla + '. ' + siteTitle + '. ' + year + '. Web. ' + accessed + '. <' + url + '>.'
      : authorMla + '. "' + title + '." ' + siteTitle + '. ' + year + '. Web. ' + accessed + '. <' + url + '>.';

    return { chicago: chicago, ngsq: ngsq, mla: mla };
  }

  function init() {
    var widget = document.getElementById('cite-this-page');
    if (!widget) return;
    var ctx = {
      pageTitle: pageTitle(),
      url: canonicalUrl(),
      dateMod: dateModified()
    };
    var cites = buildCitations(ctx);

    widget.querySelectorAll('.cite-out').forEach(function (el) {
      var style = el.getAttribute('data-style');
      if (cites[style] != null) el.textContent = cites[style];
    });

    var doi = (document.documentElement.getAttribute('data-doi') || '').trim();
    var doiRow = document.getElementById('cite-doi-row');
    if (doi && doiRow) {
      doiRow.hidden = false;
      var doiOut = doiRow.querySelector('.cite-out');
      if (doiOut) doiOut.textContent = 'https://doi.org/' + doi;
    }

    var modEl = widget.querySelector('.cite-modified');
    if (modEl) {
      modEl.textContent = fmtDateLong(ctx.dateMod);
      modEl.setAttribute('datetime', fmtDateIso(ctx.dateMod));
    }

    widget.querySelectorAll('.cite-copy').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var key = btn.getAttribute('data-target');
        var src = widget.querySelector('.cite-out[data-style="' + key + '"]');
        if (!src) return;
        var text = src.textContent;
        var done = function () {
          var orig = btn.textContent;
          btn.classList.add('copied');
          btn.textContent = 'Copied';
          setTimeout(function () { btn.classList.remove('copied'); btn.textContent = orig; }, 1400);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, function () {
            // fallback below
            try {
              var ta = document.createElement('textarea');
              ta.value = text; ta.setAttribute('readonly', '');
              ta.style.position = 'absolute'; ta.style.left = '-9999px';
              document.body.appendChild(ta);
              ta.select(); document.execCommand('copy');
              document.body.removeChild(ta);
              done();
            } catch (e) { /* ignore */ }
          });
        } else {
          try {
            var ta = document.createElement('textarea');
            ta.value = text; ta.setAttribute('readonly', '');
            ta.style.position = 'absolute'; ta.style.left = '-9999px';
            document.body.appendChild(ta);
            ta.select(); document.execCommand('copy');
            document.body.removeChild(ta);
            done();
          } catch (e) { /* ignore */ }
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
