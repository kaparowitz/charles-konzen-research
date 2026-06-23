// Embed zoom controller for PDF/image viewers.
// Sets a CSS custom property --embed-zoom on the .embed-wrap element. CSS uses that to scale
// the embed's pixel size beyond the wrapper, so the wrapper's overflow:auto provides horizontal
// and vertical scroll bars and the user can pan around the zoomed page.
(function () {
  function setZoom(wrap, zoom) {
    // Capture the user's current visible center BEFORE the zoom change. We'll use this to
    // preserve their viewing position across the zoom — i.e., the same content stays in the
    // visible window, just at a different zoom level. This matches how native browser /
    // PDF-viewer zoom works.
    var oldZoom = parseFloat(getComputedStyle(wrap).getPropertyValue('--embed-zoom')) || 1;
    var oldCenterX = wrap.scrollLeft + wrap.clientWidth / 2;
    var oldCenterY = wrap.scrollTop + wrap.clientHeight / 2;
    var ratio = zoom / oldZoom;

    wrap.style.setProperty('--embed-zoom', String(zoom));
    var readout = wrap.parentNode.querySelector('.zoom-readout');
    if (readout) readout.textContent = Math.round(zoom * 100) + '%';
    var btns = wrap.parentNode.querySelectorAll('.zoom-group button[data-zoom]');
    btns.forEach(function (b) {
      b.classList.toggle('active', Math.abs(parseFloat(b.dataset.zoom) - zoom) < 0.01);
    });

    // Apply the new scroll position to keep the visible center stable. Embed elements (PDF
    // viewers in particular) sometimes resize asynchronously after the CSS variable changes,
    // so the wrapper's scrollWidth may not reflect the new dimensions until later. Apply the
    // scroll at multiple delays so at least one of them lands after the resize has settled.
    function applyScroll() {
      var newScrollLeft = oldCenterX * ratio - wrap.clientWidth / 2;
      var newScrollTop = oldCenterY * ratio - wrap.clientHeight / 2;
      wrap.scrollLeft = Math.max(0, Math.min(wrap.scrollWidth - wrap.clientWidth, newScrollLeft));
      wrap.scrollTop = Math.max(0, Math.min(wrap.scrollHeight - wrap.clientHeight, newScrollTop));
    }
    requestAnimationFrame(applyScroll);
    setTimeout(applyScroll, 60);
    setTimeout(applyScroll, 200);
  }

  function step(wrap, delta) {
    var current = parseFloat(getComputedStyle(wrap).getPropertyValue('--embed-zoom')) || 1;
    var next = Math.max(0.5, Math.min(5, Math.round((current + delta) * 100) / 100));
    setZoom(wrap, next);
  }

  function attach(controls) {
    // Find the embed-wrap that this controls toolbar is governing — assume it's the
    // immediately preceding .embed-wrap sibling.
    var wrap = controls.previousElementSibling;
    while (wrap && !wrap.classList.contains('embed-wrap')) {
      wrap = wrap.previousElementSibling;
    }
    if (!wrap) return;

    controls.querySelectorAll('button[data-zoom]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        setZoom(wrap, parseFloat(btn.dataset.zoom));
      });
    });
    var minus = controls.querySelector('button[data-zoom-step="-"]');
    var plus = controls.querySelector('button[data-zoom-step="+"]');
    if (minus) minus.addEventListener('click', function () { step(wrap, -0.25); });
    if (plus) plus.addEventListener('click', function () { step(wrap, +0.25); });

    var fs = controls.querySelector('button[data-fullscreen]');
    if (fs) {
      fs.addEventListener('click', function () {
        if (wrap.requestFullscreen) wrap.requestFullscreen();
        else if (wrap.webkitRequestFullscreen) wrap.webkitRequestFullscreen();
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.embed-controls').forEach(attach);
  });
})();
