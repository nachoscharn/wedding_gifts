document.addEventListener('DOMContentLoaded', function() {
    const giftButtons = document.querySelectorAll('.gift-button');
    const modal = document.getElementById('gift-form-modal');
    const closeBtn = document.querySelector('.close');
    const giftInput = document.getElementById('gift');
    const amountInput = document.getElementById('amount');

    giftButtons.forEach(button => {
        button.addEventListener('click', function() {
            const gift = button.getAttribute('data-gift');
            const amount = button.getAttribute('data-amount');
            giftInput.value = gift;
            amountInput.value = amount;
            modal.style.display = 'block';
        });
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
