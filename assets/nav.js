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
