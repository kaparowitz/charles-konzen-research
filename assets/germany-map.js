/*
 * germany-map.js — Leaflet initialization for the Germany & Origins page.
 *
 * Renders four pins (Trendelburg, Deisel, Kassel, Bremen) on an Esri World Street Map
 * tile layer, with a 10-mile parish-search circle around Trendelburg and a curved
 * 1859 emigration arc to Bremen. Each pin's popup carries a "scroll to figure" link
 * (delegated via marker `popupopen` so we don't ship inline onclick) and a Google
 * Maps deep-link.
 *
 * Dependencies: Leaflet 1.9.4 (loaded from unpkg in the <head>).
 *
 * Extracted from germany-and-origins.html — May 2026.
 */
(function() {
  var pins = [
    { ll:[51.5917, 9.4181], cls:"origin",   title:"Trendelburg",        yr:"1773–1830s", fig:"fig-trendelburg-today", figLabel:"View Trendelburg photos",  body:"Walled medieval town on the right bank of the Diemel, ten miles north of Kassel in the former Kurfürstentum Hessen. The town parish register holds the long Konze / Kontze paper trail (1773 onward) that drove the leading hypothesis for Charles's origins. Population ~1,500 in the mid-19th century.", gmaps:"https://www.google.com/maps/search/?api=1&query=Trendelburg+Hesse+Germany" },
    { ll:[51.5736, 9.4647], cls:"origin",   title:"Deisel",             yr:"1835–1859", fig:"fig-deisel", figLabel:"View the Deisel drawing",   body:"Village just east of Trendelburg, today an Ortsteil of the Stadt Trendelburg. Site of the contested Entry 195 in the Helmarshausen / Trendelburg parish records. The Deisel emigration list is the document Peter Schräder used in his 12 April 2026 verdict — only one Konze is recorded in the relevant emigration window, and it is not Charles.", gmaps:"https://www.google.com/maps/search/?api=1&query=Deisel+Trendelburg+Hesse+Germany" },
    { ll:[51.3127, 9.4797], cls:"regional", title:"Kassel",             yr:"capital", fig:"fig-kassel", figLabel:"View the Kassel engraving",     body:"Capital of the Kurfürstentum Hessen (Hesse-Kassel) — the state Charles was born a subject of in 1835 and emigrated from in 1859. The Hessian State Archive (HStAM) at Marburg holds the original civil and ecclesiastical records for the Hofgeismar Kirchenkreis villages just to the north. Annexed by Prussia in 1866 — the political shock that Charles commemorated three months later by naming his St. Louis firstborn <em>Friedrich Wilhelm</em>, after the deposed Elector.", gmaps:"https://www.google.com/maps/search/?api=1&query=Kassel+Hesse+Germany" },
    { ll:[53.0793, 8.8017], cls:"port",     title:"Bremen — port of departure", yr:"1859", fig:"fig-bremen-port", figLabel:"View the Bremen port photo", body:"The free Hanseatic city and its downstream outport at <strong>Bremerhaven</strong> (founded 1827) were the dominant German emigration ports of the 1850s. Charles's 1859 census-reported immigration year places him on one of the eight Bremen-to-North-America sailings transcribed in <em>ISTG Vol. 16</em> for the 1858–1860 window. The original Bremen passenger lists were destroyed (purged ca. 1907 + WWII bombing); reconstruction is being attempted from the U.S.-side NARA manifests. ~190 miles north of Trendelburg.", gmaps:"https://www.google.com/maps/search/?api=1&query=Bremen+Germany" }
  ];

  var COLORS = { origin:"#5a8a4a", regional:"#8a6a14", port:"#3a5878" };

  function makeIcon(color) {
    var html = '<div style="background:' + color + '; width:18px; height:18px; border-radius:50%; ' +
               'border:2px solid #fffaf0; box-shadow:0 0 0 1px #5a4a32, 0 2px 5px rgba(0,0,0,0.35);"></div>';
    return L.divIcon({ html:html, className:"ge-fmap-pin", iconSize:[22,22], iconAnchor:[11,11], popupAnchor:[0,-8] });
  }

  function initGeMap() {
    var el = document.getElementById('ge-fmap');
    if (!el || el._leafletInit) return;
    el._leafletInit = true;

    var map = L.map('ge-fmap', { scrollWheelZoom:false }).setView([52.2, 9.1], 7);
    // Esri World Street Map — English-labelled tiles with standard cartographic label placement.
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
      maxZoom: 19,
      attribution: 'Tiles &copy; <a href="https://www.esri.com/">Esri</a> &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom'
    }).addTo(map);

    var bounds = L.latLngBounds([]);

    // 10-mile parish-search radius around Trendelburg (the Hofgeismar Kirchenkreis 10-parish area)
    L.circle([51.5917, 9.4181], {
      radius: 16093, // 10 statute miles in metres
      color: '#5a8a4a',
      weight: 1.5,
      opacity: 0.7,
      fillColor: '#5a8a4a',
      fillOpacity: 0.07,
      dashArray: '5,4',
      interactive: false
    }).addTo(map);

    // 1859 emigration route: Trendelburg → Bremen, drawn as a gentle quadratic curve.
    function curvedPath(p1, p2, curvature, n) {
      var pts = [];
      var dLat = p2[0] - p1[0];
      var dLon = p2[1] - p1[1];
      var ctrlLat = (p1[0] + p2[0]) / 2 + curvature * dLon;
      var ctrlLon = (p1[1] + p2[1]) / 2 - curvature * dLat;
      for (var i = 0; i <= n; i++) {
        var t = i / n;
        var lat = (1-t)*(1-t)*p1[0] + 2*(1-t)*t*ctrlLat + t*t*p2[0];
        var lon = (1-t)*(1-t)*p1[1] + 2*(1-t)*t*ctrlLon + t*t*p2[1];
        pts.push([lat, lon]);
      }
      return pts;
    }
    var arcPoints = curvedPath([51.5917, 9.4181], [53.0793, 8.8017], 0.18, 40);
    L.polyline(arcPoints, {
      color: '#a3441f',
      weight: 2.5,
      opacity: 0.85,
      dashArray: '8,5',
      interactive: false
    }).addTo(map);
    // Midpoint label for the emigration arc
    var midIdx = Math.floor(arcPoints.length / 2);
    L.marker(arcPoints[midIdx], {
      icon: L.divIcon({
        className: 'ge-arc-label',
        html: '<div style="display:inline-block;background:#fffaf0;border:1px solid #a3441f;border-radius:3px;padding:0.18rem 0.65rem;font-family:\'Iowan Old Style\',Georgia,serif;font-size:0.8rem;color:#7a3416;font-weight:700;white-space:nowrap;box-shadow:0 1px 3px rgba(0,0,0,0.18);transform:translate(-50%, -50%);">1859 · ~190 mi to Bremen</div>',
        iconSize: [0, 0],
        iconAnchor: [0, 0]
      }),
      interactive: false,
      keyboard: false
    }).addTo(map);

    // Highlight target figure briefly when the user follows a "scroll to figure" link.
    // The link is a real `<a href="#fig-…">` so it works without JS (browser default
    // jump) and via keyboard (Enter on focus). This handler only adds the
    // smooth-scroll + golden outline polish on top of the native anchor behavior.
    function flashFigure(figId) {
      var t = document.getElementById(figId);
      if (!t) return;
      t.style.outline = '3px solid #d8b366';
      setTimeout(function() { t.style.outline = 'none'; }, 2000);
    }

    pins.forEach(function(p) {
      var marker = L.marker(p.ll, { icon: makeIcon(COLORS[p.cls] || "#5a8a4a"), title: p.title }).addTo(map);
      var figLink = p.fig ? '<a class="openmap" href="#' + p.fig + '" data-figjump="' + p.fig + '"><span aria-hidden="true">📷 </span>' + p.figLabel + ' <span aria-hidden="true">↓</span></a><br>' : '';
      marker.bindPopup(
        '<h3>' + p.title + '</h3>' +
        '<div class="yr">' + p.yr + '</div>' +
        '<div class="body">' + p.body + '</div>' +
        figLink +
        '<a class="openmap" href="' + p.gmaps + '" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">✦ </span>Open in Google Maps</a>',
        { maxWidth: 320 }
      );
      marker.on('popupopen', function(e) {
        var node = e.popup.getElement();
        if (!node) return;
        var link = node.querySelector('a[data-figjump]');
        if (link && !link._jumpBound) {
          link._jumpBound = true;
          // Use 'click' (which fires on Enter activation too) and let the browser
          // perform the hash-jump. We override only to upgrade the jump to a
          // smooth scroll + flash highlight; falling back to default if the
          // figure is missing keeps the anchor working without JS.
          link.addEventListener('click', function(evt) {
            var id = link.getAttribute('data-figjump');
            var t = document.getElementById(id);
            if (!t) return;
            // Smooth-scroll override (skip if user prefers reduced motion).
            var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            if (!reduce) {
              evt.preventDefault();
              t.scrollIntoView({ behavior: 'smooth', block: 'center' });
              // Update the URL hash so Back works as expected.
              if (history && history.pushState) { history.pushState(null, '', '#' + id); }
            }
            flashFigure(id);
          });
        }
      });
      bounds.extend(p.ll);
    });
    var FIT_OPTS = { padding:[60,60], maxZoom:9 };
    // The Germany section may be hidden in a tab when the page first loads, which gives Leaflet a 0×0 container.
    // We need to re-fit bounds (not just invalidateSize) when the tab becomes visible, otherwise the
    // initial fitBounds computed against the 0×0 container leaves the map at a zoom/center where the
    // pins are off-screen.
    function refit() {
      map.invalidateSize();
      if (bounds.isValid()) map.fitBounds(bounds, FIT_OPTS);
    }
    refit();
    setTimeout(refit, 60);
    window.addEventListener('resize', refit);
    var ge = document.getElementById('germany');
    if (ge) {
      new MutationObserver(function(){ if (ge.classList.contains('active') || ge.offsetParent !== null) setTimeout(refit, 60); })
        .observe(ge, { attributes:true, attributeFilter:['class','style'] });
    }
    var germanyBtn = document.querySelector('nav.tabs button[data-target=germany]');
    if (germanyBtn) germanyBtn.addEventListener('click', function(){ setTimeout(refit, 80); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGeMap);
  } else {
    initGeMap();
  }
})();
