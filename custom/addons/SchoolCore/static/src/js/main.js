document.addEventListener('DOMContentLoaded', function () {
    console.log("EduVerse frontend script loaded.");

    const buttons = document.querySelectorAll("button");
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            alert("Button clicked!");
        });
    });
});
