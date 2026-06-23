/* ============================================================
   Site nav + footer (shared partials) — JavaScript
   Charles Research · added 8 May 2026 (audit-fix pass)
   Keyboard navigation added · 16 May 2026 (P9 a11y pass)
   ============================================================
   Drives the grouped-dropdown nav on standalone pages.
   The home page (index.html) has its own SPA-tab logic in
   cinematic.js / inline scripts; this file is for every other
   page so the nav is interactive there too.

   Keyboard behavior (WAI-ARIA Authoring Practices · menubar pattern):
   - On a closed group-btn:
       ArrowDown / Enter / Space : open menu, focus first item
       ArrowRight / ArrowLeft    : move focus to next/prev group-btn
   - Within an open menu:
       ArrowDown / ArrowUp       : move focus to next/prev item
       Home / End                : focus first / last item
       Escape                    : close menu, return focus to group-btn
       ArrowLeft / ArrowRight    : close current menu, focus prev/next
                                   group-btn (do NOT auto-open)
       Tab                       : default browser behavior (leaves nav)
   - Click outside or Escape elsewhere also closes any open menu.
   ------------------------------------------------------------ */
(function () {
  'use strict';

  function init() {
    var navs = document.querySelectorAll('nav.site-nav-shared');
    if (!navs.length) return;

    navs.forEach(function (nav) {
      var groupBtns = Array.prototype.slice.call(nav.querySelectorAll('.group-btn'));

      // Track which group-btn opened the currently-visible menu so we can
      // return focus there when the menu closes (Escape / outside-click).
      var lastOpener = null;

      function closeAll(restoreFocus) {
        var hadOpen = !!nav.querySelector('.group-menu:not([hidden])');
        nav.querySelectorAll('.group-menu').forEach(function (m) { m.hidden = true; });
        groupBtns.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
        if (restoreFocus && hadOpen && lastOpener) {
          try { lastOpener.focus(); } catch (e) { /* noop */ }
        }
        if (!hadOpen) lastOpener = null;
      }

      function openMenu(btn, focusFirst) {
        var menu = btn.parentElement.querySelector('.group-menu');
        if (!menu) return null;
        closeAll(false);
        menu.hidden = false;
        btn.setAttribute('aria-expanded', 'true');
        lastOpener = btn;
        if (focusFirst) {
          var first = menu.querySelector('a[role="menuitem"], button[role="menuitem"], [role="menuitem"]');
          if (first) {
            try { first.focus(); } catch (e) { /* noop */ }
          }
        }
        return menu;
      }

      function menuItems(menu) {
        if (!menu) return [];
        return Array.prototype.slice.call(
          menu.querySelectorAll('a[role="menuitem"], button[role="menuitem"], [role="menuitem"]')
        );
      }

      // Group-btn click + keyboard handlers.
      groupBtns.forEach(function (btn, gIdx) {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          var menu = btn.parentElement.querySelector('.group-menu');
          if (!menu) return;
          var wasOpen = !menu.hidden;
          if (wasOpen) {
            closeAll(false);
          } else {
            openMenu(btn, false);
          }
        });

        btn.addEventListener('keydown', function (e) {
          var menu = btn.parentElement.querySelector('.group-menu');
          var isOpen = menu && !menu.hidden;
          switch (e.key) {
            case 'ArrowDown':
            case 'Enter':
            case ' ':
              e.preventDefault();
              openMenu(btn, true);
              break;
            case 'ArrowUp':
              // Open and focus last item — useful for screen-reader users.
              e.preventDefault();
              var mUp = openMenu(btn, false);
              var itemsUp = menuItems(mUp);
              if (itemsUp.length) {
                try { itemsUp[itemsUp.length - 1].focus(); } catch (er) { /* noop */ }
              }
              break;
            case 'ArrowRight':
              e.preventDefault();
              var nextIdx = (gIdx + 1) % groupBtns.length;
              if (isOpen) closeAll(false);
              try { groupBtns[nextIdx].focus(); } catch (er) { /* noop */ }
              break;
            case 'ArrowLeft':
              e.preventDefault();
              var prevIdx = (gIdx - 1 + groupBtns.length) % groupBtns.length;
              if (isOpen) closeAll(false);
              try { groupBtns[prevIdx].focus(); } catch (er) { /* noop */ }
              break;
            case 'Escape':
              if (isOpen) {
                e.preventDefault();
                closeAll(true);
              }
              break;
          }
        });
      });

      // Menu-item keyboard navigation (delegated on each menu so we can
      // freely re-target as menus open/close).
      nav.querySelectorAll('.group-menu').forEach(function (menu) {
        menu.addEventListener('keydown', function (e) {
          var items = menuItems(menu);
          if (!items.length) return;
          var current = document.activeElement;
          var idx = items.indexOf(current);
          var opener = menu.parentElement && menu.parentElement.querySelector('.group-btn');
          var openerIdx = opener ? groupBtns.indexOf(opener) : -1;

          switch (e.key) {
            case 'ArrowDown':
              e.preventDefault();
              try { items[(idx + 1 + items.length) % items.length].focus(); } catch (er) { /* noop */ }
              break;
            case 'ArrowUp':
              e.preventDefault();
              try { items[(idx - 1 + items.length) % items.length].focus(); } catch (er) { /* noop */ }
              break;
            case 'Home':
              e.preventDefault();
              try { items[0].focus(); } catch (er) { /* noop */ }
              break;
            case 'End':
              e.preventDefault();
              try { items[items.length - 1].focus(); } catch (er) { /* noop */ }
              break;
            case 'Escape':
              e.preventDefault();
              closeAll(true);
              break;
            case 'ArrowRight':
              if (openerIdx !== -1) {
                e.preventDefault();
                var rIdx = (openerIdx + 1) % groupBtns.length;
                closeAll(false);
                try { groupBtns[rIdx].focus(); } catch (er) { /* noop */ }
              }
              break;
            case 'ArrowLeft':
              if (openerIdx !== -1) {
                e.preventDefault();
                var lIdx = (openerIdx - 1 + groupBtns.length) % groupBtns.length;
                closeAll(false);
                try { groupBtns[lIdx].focus(); } catch (er) { /* noop */ }
              }
              break;
            case 'Tab':
              // Let Tab work normally — closing the menu would be jarring
              // when the user is just trying to leave the nav region.
              break;
          }
        });
      });

      // Close menus on outside click; restore focus only if focus is
      // inside the nav (otherwise the user clicked away and shouldn't
      // be yanked back).
      document.addEventListener('click', function (e) {
        if (!nav.contains(e.target)) {
          var focusInside = nav.contains(document.activeElement);
          closeAll(focusInside);
        }
      });

      // Close menus on Escape from anywhere (kept for back-compat with
      // pre-existing behavior). When triggered globally, restore focus
      // to the last opener if the user was somewhere inside the nav.
      document.addEventListener('keydown', function (e) {
        if (e.key !== 'Escape') return;
        if (!nav.querySelector('.group-menu:not([hidden])')) return;
        var focusInside = nav.contains(document.activeElement);
        closeAll(focusInside);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
