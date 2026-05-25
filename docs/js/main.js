// БЭМ: поведение блока nav (бургер-меню)
const burger = document.querySelector(".nav__burger");
const navList = document.querySelector(".nav__list");

if (burger && navList) {
  burger.addEventListener("click", () => {
    navList.classList.toggle("nav__list--open");
  });
}
