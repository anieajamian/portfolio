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
    img.addEventListener('click', function(){
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
