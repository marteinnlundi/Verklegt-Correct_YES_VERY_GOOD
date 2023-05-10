var slideIndex = 0;
carousel();

function carousel() {
  var offerSlides = document.getElementsByClassName("offer-slide");
  for (var i = 0; i < offerSlides.length; i++) {
    offerSlides[i].style.display = "none";
  }

  slideIndex++;
  if (slideIndex > offerSlides.length) {
    slideIndex = 1;
  }
  offerSlides[slideIndex - 1].style.display = "block";

  setTimeout(carousel, 5000); // Change offer every 5 seconds
}