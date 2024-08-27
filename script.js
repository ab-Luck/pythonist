const contactForm = document.getElementById('contact-form');
const successMessage = document.getElementById('success-message');

contactForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(contactForm);

    // You can replace this with your actual email handling logic
    fetch('mehrabrarlak@gmail.com', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            successMessage.textContent = 'Message sent successfully!';
            successMessage.style.display = 'block';
            contactForm.reset();
        } else {
            console.error('Error sending message:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });
});