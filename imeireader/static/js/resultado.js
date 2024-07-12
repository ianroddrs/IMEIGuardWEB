if(screen.width <= 450){
    document.querySelectorAll('.offcanvas-end').forEach(element => {
        element.classList.remove('offcanvas-end')
        element.classList.add('offcanvas-bottom')
    }); 
}
