// Get the header element
const header = document.querySelector('.banner-container');

// Get the offset position of the header
const sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. 
// Remove "sticky" when you leave the scroll position
function stickyHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

// Listen for the scroll event and call the stickyHeader function
window.addEventListener('scroll', stickyHeader);
