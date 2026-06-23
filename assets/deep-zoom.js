/* ============================================================
   Deep-zoom viewer — lazy-loads OpenSeadragon from CDN only
   when at least one <figure class="deep-zoom"> exists on the
   page, then upgrades each one into a pannable / zoomable
   canvas.  Falls back gracefully to the static <img> whenever
   the zoom canvas cannot open (CDN blocked, offline, open-failed,
   or a load timeout) — the opaque "loading" overlay is always
   cleared so the static scan is never left hidden behind it.
   ============================================================ */
(function () {
  var OSD_URL = 'https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js';
  var OSD_IMAGES = 'https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/';
  var LOAD_TIMEOUT = 8000; // ms before we give up on OSD and show the static image

  function loadOnce(url) {
    if (window.__osd_loading__) return window.__osd_loading__;
    window.__osd_loading__ = new Promise(function (resolve, reject) {
      if (window.OpenSeadragon) { resolve(window.OpenSeadragon); return; }
      var s = document.createElement('script');
      s.src = url;
      s.async = true;
      // Guard against a script that loads but never defines OpenSeadragon,
      // and against a CDN that simply hangs.
      var to = setTimeout(function () { reject(new Error('OpenSeadragon load timed out')); }, LOAD_TIMEOUT);
      s.onload = function () { clearTimeout(to); window.OpenSeadragon ? resolve(window.OpenSeadragon) : reject(new Error('OpenSeadragon undefined after load')); };
      s.onerror = function () { clearTimeout(to); reject(new Error('Failed to load OpenSeadragon')); };
      document.head.appendChild(s);
    });
    return window.__osd_loading__;
  }

  /* Reveal the static <img> and clear the loading overlay + any
     half-initialised OSD canvas. Safe to call more than once. */
  function revealStatic(stage) {
    if (!stage) return;
    var loading = stage.querySelector('.dz-loading');
    if (loading && loading.parentNode) loading.parentNode.removeChild(loading);
    var osd = stage.querySelector('.osd-container');
    if (osd && osd.parentNode) osd.parentNode.removeChild(osd);
    var fallback = stage.querySelector('.dz-fallback');
    if (fallback) fallback.style.display = 'block';
  }

  function upgrade(figure, OpenSeadragon) {
    var stage = figure.querySelector('.dz-stage');
    if (!stage) return;
    var src = figure.getAttribute('data-src') || (stage.querySelector('img') && stage.querySelector('img').getAttribute('src'));
    if (!src) return;

    var loading = stage.querySelector('.dz-loading');
    var container = document.createElement('div');
    container.className = 'osd-container';
    container.style.position = 'absolute';
    container.style.inset = '0';
    stage.appendChild(container);

    var opened = false;

    try {
      var viewer = OpenSeadragon({
        element: container,
        prefixUrl: OSD_IMAGES,
        tileSources: { type: 'image', url: src },
        showNavigator: figure.hasAttribute('data-nav'),
        navigatorPosition: 'BOTTOM_RIGHT',
        gestureSettingsMouse: { clickToZoom: true, dblClickToZoom: true },
        gestureSettingsTouch: { pinchToZoom: true, dblClickToZoom: true },
        animationTime: 0.4,
        blendTime: 0.15,
        constrainDuringPan: true,
        visibilityRatio: 0.85,
        minZoomLevel: 0.6,
        maxZoomPixelRatio: 8,
        showRotationControl: true,
        showFullPageControl: true,
        autoHideControls: true,
        controlsFadeDelay: 1800,
        timeout: 30000
      });
      viewer.addOnceHandler('open', function () {
        opened = true;
        if (loading && loading.parentNode) loading.parentNode.removeChild(loading);
        var fallback = stage.querySelector('.dz-fallback');
        if (fallback) fallback.style.display = 'none';
      });
      viewer.addHandler('open-failed', function () {
        revealStatic(stage); // show the static scan instead of a stuck overlay
      });
    } catch (e) {
      revealStatic(stage);
      return;
    }

    // Safety net: if OSD never fires 'open' (image fails to decode, a silent
    // hang, etc.), drop the overlay so the static scan is visible.
    setTimeout(function () { if (!opened) revealStatic(stage); }, LOAD_TIMEOUT);
  }

  function init() {
    var figures = document.querySelectorAll('figure.deep-zoom');
    if (!figures.length) return;
    loadOnce(OSD_URL).then(function (OpenSeadragon) {
      figures.forEach(function (f) { upgrade(f, OpenSeadragon); });
    }).catch(function () {
      // CDN blocked / offline / timed out — reveal every static scan.
      figures.forEach(function (f) { revealStatic(f.querySelector('.dz-stage')); });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
