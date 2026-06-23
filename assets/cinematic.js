/* ============================================================
   Cinematic layer · scroll behavior
   - Reveals chapter cards as they enter the viewport
   - Smooth-scrolls the cover CTA to the first chapter
   - Honors prefers-reduced-motion
   ============================================================ */
(function () {
  'use strict';

  const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    // --- 1. Reveal chapter cards on scroll ---
    const chapters = document.querySelectorAll('.cinema-chapter');
    let io = null;
    if (chapters.length) {
      if (reduce || !('IntersectionObserver' in window)) {
        chapters.forEach(c => c.classList.add('is-visible'));
      } else {
        io = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              io.unobserve(entry.target);
            }
          });
        }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
        chapters.forEach(c => io.observe(c));
      }
    }

    // --- 1b. Tab-aware reveal — when a tab section becomes active,
    //         force-reveal any chapter cards inside it (the IO can't
    //         see elements whose parent was display:none on first paint).
    function revealChaptersInside(section) {
      const cs = section.querySelectorAll('.cinema-chapter');
      cs.forEach(function (c, i) {
        // Stagger so they fade in one-by-one rather than snap-revealing.
        setTimeout(function () { c.classList.add('is-visible'); }, 80 + i * 110);
      });
    }
    document.querySelectorAll('section.page').forEach(function (s) {
      if (s.classList.contains('active') && s.querySelector('.cinema-chapter')) {
        revealChaptersInside(s);
      }
    });
    if ('MutationObserver' in window) {
      const mo = new MutationObserver(function (muts) {
        muts.forEach(function (m) {
          if (m.attributeName !== 'class') return;
          const t = m.target;
          if (t.matches && t.matches('section.page') &&
              t.classList.contains('active') &&
              t.querySelector('.cinema-chapter')) {
            revealChaptersInside(t);
            // Also scroll the cover into view for a clean reveal moment.
            const cov = t.querySelector('.cinema-cover');
            if (cov && !reduce) {
              setTimeout(function () {
                cov.scrollIntoView({ behavior: 'smooth', block: 'start' });
              }, 60);
            }
          }
        });
      });
      document.querySelectorAll('section.page').forEach(function (s) {
        mo.observe(s, { attributes: true, attributeFilter: ['class'] });
      });
    }

    // --- 2. Smooth-scroll cover CTA ---
    document.querySelectorAll('[data-cine-scroll]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        const sel = el.getAttribute('data-cine-scroll');
        const target = sel ? document.querySelector(sel) : null;
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
        }
      });
    });

    // --- 3. Subtle parallax on the cover backdrop ---
    if (!reduce) {
      const cover = document.querySelector('.cinema-cover');
      if (cover) {
        let raf = null;
        window.addEventListener('scroll', function () {
          if (raf) return;
          raf = requestAnimationFrame(function () {
            raf = null;
            const y = window.scrollY;
            if (y < window.innerHeight) {
              cover.style.setProperty('--cine-y', y + 'px');
              const portrait = cover.querySelector('.cinema-cover__portrait-frame');
              const type = cover.querySelector('.cinema-cover__type');
              if (portrait) portrait.style.transform = 'translateY(' + (y * 0.18) + 'px)';
              if (type) type.style.transform = 'translateY(' + (y * 0.08) + 'px)';
            }
          });
        }, { passive: true });
      }
    }
  });
})();
