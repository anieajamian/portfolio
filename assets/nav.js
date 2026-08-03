document.addEventListener('DOMContentLoaded', function(){
  var toggle = document.querySelector('.nav-toggle');
  var inner = document.querySelector('.nav-inner');
  if(!toggle || !inner) return;

  toggle.addEventListener('click', function(){
    var isOpen = inner.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  inner.querySelectorAll('.nav-right a').forEach(function(link){
    link.addEventListener('click', function(){
      inner.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
});

/* Nav gains a subtle shadow once scrolled off the hero */
(function(){
  var nav = document.querySelector('header.site-nav');
  if(!nav) return;
  var update = function(){
    nav.classList.toggle('is-scrolled', window.scrollY > 4);
  };
  update();
  window.addEventListener('scroll', update, { passive: true });
})();

/* Scroll reveal — fade/rise elements in as they enter the viewport.
   Only below-the-fold elements are ever hidden, so nothing animates on
   load and above-the-fold content is shown instantly. */
(function(){
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce || !('IntersectionObserver' in window)) return;

  var selector = '.section-head, .work-card, .hero-img, .proj-summary, .stat-row, .screen-row, .screen-solo';
  var els = document.querySelectorAll(selector);
  if(!els.length) return;

  // Gentle diagonal stagger for cards sharing a grid row.
  document.querySelectorAll('.work-grid').forEach(function(grid){
    grid.querySelectorAll('.work-card').forEach(function(card, i){
      card.style.transitionDelay = (i % 2) * 70 + 'ms';
    });
  });

  var vh = window.innerHeight || document.documentElement.clientHeight;
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

  els.forEach(function(el){
    // Already in view on load → leave it visible, no animation.
    if(el.getBoundingClientRect().top < vh * 0.92) return;
    el.classList.add('reveal');
    observer.observe(el);
  });
})();
