$('.shares__slider').slick({
  slidesToShow: 1,
  prevArrow: $('.shares__slider-left'),
  nextArrow: $('.shares__slider-right'),
  dots: true,
  infinite: true,
})



const overlay = document.querySelector('.header__overlay');
const mobileMenu = document.querySelector('.mobile-menu');
const hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', () => {
  mobileMenu.classList.add('mobile-menu--open')
  overlay.classList.add('header__overlay--darken')
})

overlay.addEventListener('click', () => {
  mobileMenu.classList.remove('mobile-menu--open')
  overlay.classList.remove('header__overlay--darken')
})


const recall = document.querySelector('#recall')

recall.addEventListener('click', () => {
  recall.classList.toggle('active')
})
