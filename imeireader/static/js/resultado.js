function mascara() {
    const input = document.querySelector('[mask="bop"]');
    var cursorPosition = input.selectionStart;
    var oldValue = input.value;
    input.value = mbop(input.value);
    var diff = input.value.length - oldValue.length;
    input.selectionStart = input.selectionEnd = Math.max(0, cursorPosition + diff);
}

function mbop(v) {
    v = v.replace(/\D/g, "");
    v = v.replace(/(\d)(\d{1})$/, "$1-$2");
    v = v.replace(/^(\d{5,9})(\d{6})/g, "$1.$2");
    v = v.replace(/^(\d{1,5})(\d{4})/g, "$1/$2");
    return v;
}