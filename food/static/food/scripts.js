document.addEventListener('DOMContentLoaded', function() {
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
