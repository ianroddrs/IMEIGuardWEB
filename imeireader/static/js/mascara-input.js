// MASCARA
 
function mascara(el) {
    const input = el;
    var cursorPosition = input.selectionStart;
    var oldValue = input.value;
    input.value = el.getAttribute('mask') == 'imei' ? mnumber(input.value) : mbop(input.value);
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

function mnumber(v) {
    v = v.replace(/\D/g, ""); 
    if (v.length > 15) {
        v = v.slice(0, 15);
    }
    return v;
}

function validateIMEI(imei) {
    imei = imei.replace(/\D+/g, ''); // remove espaços e hífens
    if (imei.length !== 15) return false; // IMEI deve ter 15 dígitos
  
    let sum = 0;
    for (let i = 0; i < 15; i++) {
      let digit = parseInt(imei[i], 10);
      if (i % 2 === 0) { // dígito par
        digit *= 2;
        if (digit > 9) digit -= 9; // se maior que 9, some os dígitos
      }
      sum += digit;
    }
  
    return sum % 10 === 0; // IMEI é válido se a soma for múltiplo de 10
  }