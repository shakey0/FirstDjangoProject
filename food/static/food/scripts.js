document.addEventListener('DOMContentLoaded', function() {

    function checkNavbarClass() {
        const navbar = document.getElementById('navbar');
        if (window.innerWidth < 500) {
            navbar.classList.remove('fixed-top');
        } else {
            if (!navbar.classList.contains('fixed-top')) {
                navbar.classList.add('fixed-top');
            }
        }
    }
    
    checkNavbarClass();
    window.addEventListener('resize', checkNavbarClass);


    const inputField = document.getElementById('item-price');

    function formatInput(value) {
        const numericValue = value.replace(/[^0-9.]/g, '');
        return '£' + numericValue;
    }

    if (inputField) {
        inputField.value = formatInput(inputField.value);
    
        inputField.addEventListener('input', function() {
            this.value = formatInput(this.value.replace('£', ''));
        });
    
        // Ensure cursor position is always after £ sign
        inputField.addEventListener('click', function() {
            const val = this.value;
            const poundPos = val.indexOf('£') + 1;
            if (this.selectionStart < poundPos) {
            this.setSelectionRange(poundPos, poundPos);
            }
        });
    
        // Prevent cursor from moving before £ sign on keydown
        inputField.addEventListener('keydown', function(e) {
            const val = this.value;
            const poundPos = val.indexOf('£') + 1;
            if ((e.key === 'ArrowLeft' && this.selectionStart <= poundPos) || 
                (e.key === 'Backspace' && this.selectionStart <= poundPos)) {
            e.preventDefault();
            }
        });
    }
});
