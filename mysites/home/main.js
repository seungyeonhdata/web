/*-----menu -------*/
var navMenu = document.getElementById('nav-menu');
toggleMenu = document.getElementById('nav-toggle');
closeMenu = document.getElementById('nav-close');

function showMenu(){
    navMenu.classList.toggle('show');
}
function removeMenu(){
    navMenu.classList.remove('show');
}

toggleMenu.addEventListener('click',showMenu);
closeMenu.addEventListener('click',removeMenu);
var navLink = document.querySelectorAll('.nav_link');
for(var i=0; i<navLink.length;i++){
    navLink[i].addEventListener('click',removeMenu);
}
//navLink.forEach(n => n.addEventListener('click',removeMenu)) =>짧게쓰는법


jQuery(document).ready(function($) {
    $(".scroll").click(function(){             
    $('html,body').animate({scrollTop:$(this).offset().top}, 500);   
    });   
    });
   

/*
var sections = document.querySelectorAll('section[id]');

function scrollActive(){
    var scrollY=window.pageYOffset;
    sections.forEach(current=>{
        var sectionHeight = current.offsetHeight;
        var sectionTop = current.offsetTop;
        var sectionId = current.getAtrribute('id');

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav_menu a[href*='+ sectionId +']').classList.add('active');
        }else{
            document.querySelector('.nav_menu a[href*='+ sectionId +']').classList.remove('active');
        }
    })
}
window.addEventListener('scroll',scrollActive);
*/