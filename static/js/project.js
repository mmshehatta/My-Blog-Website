
// function showForm(){

//    if(document.getElementById('show-comment').style.display === 'none')
//    {
//     document.getElementById('show-comment').style.display='block'
//    }
//    else{
//    document.getElementById('show-comment').style.display='none'
//    }

//     console.log('done.')

// }


$(document).ready(function(){
    $('#show-comment').hide(100);
});

$('#btn').click(function(){
    $('#show-comment').toggle(1000)
});

// ****************** showSlides **********************
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
} 

// **************