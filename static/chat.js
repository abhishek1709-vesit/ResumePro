document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById("chat-form")
    const loadingText = document.querySelector(".processing")
    if (form) {
      form.addEventListener("submit", () => {
        if (loadingText) loadingText.style.display = "inline-block";
      });
    }
    
})