let html5QrcodeScanner = new Html5QrcodeScanner(
  "reader",
  {
    fps: 10,
    qrbox: {
      width: 250,
      height: 100
    },
    formatsToSupport: [
      Html5QrcodeSupportedFormats.CODE_128
    ] 
  },
);

html5QrcodeScanner.render(

  function onScanSuccess(decodedText, decodedResult) {

    console.log(`Code matched = ${decodedText}`, decodedResult)

  },
  
  function onScanFailure(error) {

    console.warn(`Code scan error = ${error}`);

  }
  
)