const contactForm = document.getElementById("contactForm");

if (contactForm) {
    contactForm.addEventListener("submit", function () {
        const submitButton = contactForm.querySelector('button[type="submit"]');

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.textContent = "Sending...";
        }
    });
}