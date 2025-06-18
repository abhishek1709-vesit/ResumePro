NProgress.start();

window.addEventListener("load", () => {
    NProgress.done();
});

document.addEventListener("DOMContentLoaded", () => {
    const menuList = document.getElementById("menuList") 
    const menuIcon = document.querySelector(".menu-icon");
    const crossIcon = document.querySelector(".cross-icon")
    
    menuIcon.addEventListener("click", () => {
        menuList.classList.toggle("open");
        menuIcon.style.display = "none"
        crossIcon.style.display = "block"
    })

    crossIcon.addEventListener("click", () => {
        menuList.classList.toggle("open");
        crossIcon.style.display = "none"
        menuIcon.style.display = "block"
    })
})
