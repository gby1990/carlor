document.addEventListener('DOMContentLoaded',function(){
  var b=document.querySelector('.burger'),m=document.querySelector('.nav ul');
  if(b&&m)b.addEventListener('click',function(){m.classList.toggle('open')});
  var here=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.nav ul a').forEach(function(a){
    if(a.getAttribute('href')===here)a.classList.add('active');
  });
  var y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();
});
