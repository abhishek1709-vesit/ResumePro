console.log("Hello");

document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.querySelector("#drag-area");
  const fileInput = document.querySelector("#fileElem");
  const dragText = document.querySelector(".drag-text");
  const form = document.querySelector(".form-field");
  const submitBtn = document.getElementById("submit-btn");
  const loadingText = document.getElementById("loading-text");

  if (dropArea && fileInput) {
    ["dragenter", "dragover"].forEach((eventName) => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation(); // to prevent default browser handling
        dropArea.classList.add("highlight");
      });
    });

    ["dragleave", "drop"].forEach((eventName) => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropArea.classList.remove("highlight");
      });
    });

    dropArea.addEventListener("drop", (e) => {
      const files = e.dataTransfer.files;
      if (files.length > 0) {
        if (files[0].type === "application/pdf") {
          // console.log(files);
          fileInput.files = files; 
          dragText.textContent = `Selected: ${files[0].name}`;
        } else {
          dragText.textContent = "Please upload a PDF file";
        }
      }
    });

    fileInput.addEventListener("change", (e) => {
      if (fileInput.files.length > 0) {
        dragText.textContent = `Selected: ${fileInput.files[0].name}`;
        dropArea.classList.add("highlight");
      }
    });

    dropArea.addEventListener("click", () => fileInput.click());
    if (form) {
      form.addEventListener("submit", () => {
        if (submitBtn) submitBtn.style.display = "none";
        if (loadingText) loadingText.style.display = "inline-block";
      });
    }
  }
});
