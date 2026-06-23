/* ============================================================
   theme-toggle.js
   Charles Research · added 9 May 2026
   Updated 9 May 2026 — dark mode is now the site default;
   simplified from a 3-state (auto/light/dark) cycle to a
   2-state toggle (dark ⇄ light). Absent or unrecognised
   localStorage value → dark.
   ============================================================
   Renders a small sun/moon toggle, persists the user's choice
   in localStorage under "theme", and synchronises the <html>
   element's class so dark-mode.css fires correctly.

   Class semantics (matches dark-mode.css):
     <html class="theme-dark">   → DARK (default)
     <html class="theme-light">  → user explicitly chose LIGHT

   The accompanying inline init script (in every <head>) sets
   the class BEFORE first paint; this file just builds the UI.
   ------------------------------------------------------------ */
(function () {
  'use strict';

  var STORE_KEY = 'theme';
  var ROOT = document.documentElement;

  // ---- helpers ---------------------------------------------------
  function getPref()      { try { return localStorage.getItem(STORE_KEY); } catch (e) { return null; } }
  function setPref(value) {
    try { localStorage.setItem(STORE_KEY, value); } catch (e) {}
  }

  function applyClass(pref) {
    ROOT.classList.remove('theme-light', 'theme-dark');
    ROOT.classList.add(pref === 'light' ? 'theme-light' : 'theme-dark');
  }

  // Default to dark unless the user explicitly chose light.
  function currentPref() {
    return getPref() === 'light' ? 'light' : 'dark';
  }

  function effectiveTheme() { return currentPref(); }

  // Two-state cycle: dark ⇄ light
  function nextPref(p) { return p === 'light' ? 'dark' : 'light'; }

  // ---- icons (inline SVG so no font-loading flash) ---------------
  var ICONS = {
    light: '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.5 4.5l2.1 2.1M17.4 17.4l2.1 2.1M4.5 19.5l2.1-2.1M17.4 6.6l2.1-2.1"/></g></svg>',
    dark: '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path fill="currentColor" d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
  };
  var LABELS = {
    light: 'Theme: Light (click for Dark)',
    dark:  'Theme: Dark (click for Light)'
  };
  var BADGES = { light: 'Light', dark: 'Dark' };

  // ---- styles (one-shot, scoped to .theme-toggle-fab) -------------
  function injectStyles() {
    if (document.getElementById('theme-toggle-styles')) return;
    var s = document.createElement('style');
    s.id = 'theme-toggle-styles';
    s.textContent =
      '.theme-toggle-fab{position:fixed;right:14px;bottom:14px;z-index:2147483600;' +
      'display:inline-flex;align-items:center;gap:.45rem;padding:.5rem .75rem;' +
      'background:var(--bg-card,#fffaf0);color:var(--text-body,#2c2620);' +
      'border:1px solid var(--border-medium,#a88a4a);border-radius:999px;' +
      'box-shadow:0 4px 14px rgba(0,0,0,.18);font:600 12px/1 var(--font-ui,system-ui,sans-serif);' +
      'letter-spacing:.04em;text-transform:uppercase;cursor:pointer;' +
      'transition:transform .15s ease,box-shadow .15s ease,background .2s,color .2s;}' +
      '.theme-toggle-fab:hover{transform:translateY(-1px);box-shadow:0 6px 18px rgba(0,0,0,.24);}' +
      '.theme-toggle-fab:focus-visible{outline:2px solid var(--brand,#d8b366);outline-offset:2px;}' +
      '.theme-toggle-fab svg{display:block;color:var(--brand-dark,#8a6420);}' +
      '.theme-toggle-fab .ttf-badge{font-variant-numeric:tabular-nums;}' +
      '@media print{.theme-toggle-fab{display:none!important;}}';
    document.head.appendChild(s);
  }

  // ---- build & mount ---------------------------------------------
  function build() {
    injectStyles();
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'theme-toggle-fab';
    btn.setAttribute('aria-live', 'polite');

    function render() {
      var pref = currentPref();
      btn.innerHTML = ICONS[pref] + '<span class="ttf-badge">' + BADGES[pref] + '</span>';
      btn.title = LABELS[pref];
      btn.setAttribute('aria-label', LABELS[pref]);
    }

    btn.addEventListener('click', function () {
      var pref = nextPref(currentPref());
      setPref(pref);
      applyClass(pref);
      render();
    });

    render();
    document.body.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build, { once: true });
  } else {
    build();
  }
})();
