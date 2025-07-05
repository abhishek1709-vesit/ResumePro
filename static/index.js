NProgress.start();

window.addEventListener("load", () => {
  NProgress.done();
});

document.addEventListener("DOMContentLoaded", () => {
  const menuList = document.getElementById("menuList");
  const menuIcon = document.querySelector(".menu-icon");
  const crossIcon = document.querySelector(".cross-icon");

  menuIcon.addEventListener("click", () => {
    menuList.classList.toggle("open");
    menuIcon.style.display = "none";
    crossIcon.style.display = "block";
  });

  crossIcon.addEventListener("click", () => {
    menuList.classList.toggle("open");
    crossIcon.style.display = "none";
    menuIcon.style.display = "block";
  });
});

const tl = gsap.timeline();

tl.from(".logo", {
  y: -60,
  duration: 1.2,
  delay: 0.5,
  opacity: 0,
});

tl.from("li", {
  y: 60,
  duration: 1.2,
  stagger: 0.2,
  opacity: 0,
});

gsap.from(".menu-icon", {
  y: 30,
  duration: 0.9,
  opacity: 0,
  delay: 0.5,
});

gsap.set(".hero-gradient", { overflow: "hidden" });
tl.from(".hero-gradient", {
  y: 30,
  duration: 0.2,
  opacity: 0,
  onComplete: () => gsap.set(".hero-gradient", { clearProps: "overflow" })
});

tl.from(".hero-text", {
  x: -50,
  duration: 0.5,
  opacity: 0,
  stagger:0.3
});

gsap.from(".features-section", {
  opacity: 0,
  x: 500,
  duration: 2,
  scrollTrigger: {
    trigger: ".features-section",
    scroller: "body",
    // markers: true,
    start: "top 78%",
  },
});
