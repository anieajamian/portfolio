document.addEventListener('DOMContentLoaded', function(){
  var triggers = document.querySelectorAll('.hero-img img, .proj-body img, .screen-row img, .screen-solo img');
  if(!triggers.length) return;

  var overlay = document.createElement('div');
  overlay.className = 'lightbox';
  overlay.innerHTML = '<button class="lightbox-close" aria-label="Close">&times;</button><img alt="">';
  document.body.appendChild(overlay);

  var overlayImg = overlay.querySelector('img');
  var closeBtn = overlay.querySelector('.lightbox-close');

  function open(src, alt){
    overlayImg.src = src;
    overlayImg.alt = alt || '';
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function close(){
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  triggers.forEach(function(img){
    var wrap = document.createElement('div');
    wrap.className = 'img-zoom-wrap';
    img.parentNode.insertBefore(wrap, img);
    wrap.appendChild(img);

    var badge = document.createElement('span');
    badge.className = 'zoom-badge';
    badge.setAttribute('aria-hidden', 'true');
    badge.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="2"/><path d="M21 21l-4.35-4.35" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
    wrap.appendChild(badge);

    wrap.addEventListener('click', function(){
      open(img.src, img.alt);
    });
  });

  closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', function(e){
    if(e.target === overlay) close();
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape') close();
  });
});
