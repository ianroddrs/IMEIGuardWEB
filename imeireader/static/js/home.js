let currentCameraIndex = 1
let cameraIds = [];
const html5QrCode = new Html5Qrcode("reader", {
    formatsToSupport: [Html5QrcodeSupportedFormats.CODE_128],
    experimentalFeatures: {useBarCodeDetectorIfSupported: true }
});

function ScannerBox(context){
    if(context == 'add'){
        document.querySelector('#scanner-container').classList.remove('d-none')
    } else if(context == 'remove'){
        document.querySelector('#scanner-container').classList.add('d-none')
        document.querySelector("#btn-switch").classList.add('d-none')
        html5QrCode.stop()
    }
}

function switchCamera() {
    if (cameraIds.length > 0) {
      currentCameraIndex = (currentCameraIndex + 1) % cameraIds.length;
      const nextCameraId = cameraIds[currentCameraIndex];
      html5QrCode.stop().then(() => {
        startScanner(nextCameraId);
      }).catch((err) => {
        console.error(err);
      });
    }
}

function showScanner(){
    ScannerBox('add');
    Html5Qrcode.getCameras().then(devices => {
        if (devices && devices.length) {
            cameraIds = devices.filter(
                device => device.label.toLowerCase().includes("back") || 
                device.label.toLowerCase().includes("traseira") ||
                device.label.toLowerCase().includes("iriun")
            ).map(device => device.id);
            if (cameraIds.length) {
                startScanner(cameraIds[cameraIds.length > 1 ? currentCameraIndex : 0]);
            } else {
                console.error("Nenhuma câmera traseira encontrada.");
            }
        }
        let text = ''
        devices.forEach(element => {
            text += `${element.label}\n`
        });
        alert(text)
    }).catch(err => {
        console.error(err);
    });
}

function startScanner(cameraId){

    html5QrCode.start(
        cameraId,
        {fps: 10, qrbox: calculateQrBoxSize(),aspectRatio: 1},
        qrCodeMessage => {
            resultado = document.getElementById("resultado")
            resultado.classList.remove('d-none')
            if(/^\d{15}$/.test(qrCodeMessage)){
                resultado.innerHTML = `<span>${qrCodeMessage}</span><button onclick="addIMEI('${qrCodeMessage}')" class="btn ms-3 btn-sm btn-primary rounded-pill" type="button">Pesquisar</button>`
            }else{
                resultado.innerHTML = '<span class="text-danger p-3">Código escaneado não se encaixa nos padrões de IMEI</span>';
            }
            
        }
    )
    if (cameraIds.length > 1) {
        setTimeout(function() {
            document.querySelector("#btn-switch")
            let btnSwitch = document.createElement('div')
            btnSwitch.className = "w-100 position-absolute z-3 d-flex justify-content-center align-items-center"
            btnSwitch.style.right = "0"
            btnSwitch.style.left = "0"
            btnSwitch.style.bottom = "20px"
            btnSwitch.id = "btn-switch"
            btnSwitch.innerHTML = `<button type="button" onclick="switchCamera()" class="rounded-circle btn btn-light fs-2"><i class="bi bi-arrow-repeat"></i></button>`
            document.getElementById("reader").appendChild(btnSwitch)
        }, 1000);
    }
    
}

function calculateQrBoxSize() {
    var larguraTela = document.querySelector('#modal-scan').clientWidth;

    qrboxWidth = (larguraTela*300)/500
    qrboxHeight = 80
    
    return {width: qrboxWidth, height: qrboxHeight}
}

function addIMEI(code){
    formulario = document.getElementById('pesquisa')
    input = document.getElementById('imei-input')
    input.value = code
    ScannerBox("remove")
    formulario.submit()
}

// MASCARA

function mascara() {
    const input = document.querySelector('#imei-input');
    var cursorPosition = input.selectionStart;
    var oldValue = input.value;
    input.value = mnumber(input.value);
    var diff = input.value.length - oldValue.length;
    input.selectionStart = input.selectionEnd = Math.max(0, cursorPosition + diff);
}

function mnumber(v) {
    v = v.replace(/\D/g, ""); 
    if (v.length > 15) {
        v = v.slice(0, 15);
    }
    return v;
}   
  
document.getElementById('pesquisa').addEventListener('submit', function(event) {
    const input = document.querySelector('#imei-input');
    if (input.value.length < 15) {
      alert('Por favor, digite todos os 15 dígitos do IMEI.');
      event.preventDefault();
    }
  });