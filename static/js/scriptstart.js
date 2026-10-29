document.addEventListener('DOMContentLoaded', () => {
    const noButtons = document.querySelectorAll('input[type="radio"][value="no"]');

    noButtons.forEach(button => {
        button.checked = true;
    });
});