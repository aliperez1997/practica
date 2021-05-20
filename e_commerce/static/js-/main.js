const xbtn = document.querySelector('#close');
const alerta = document.querySelector('#alerta');
const navb = document.querySelector('#navb');
const navbtn = document.querySelector('#navb-btn')

navbtn.onclick = () => expanNavb();
xbtn.onclick = () => cerrarAlerta();

function cerrarAlerta(){
    alerta.remove();
}

function expanNavb(){
    const clase = navb.classList
     
    if(clase[1] == 'collapse'){
        navb.classList.remove('collapse')
    }else if(clase[2] == 'collapse'){
        navb.classList.remove('collapse')
    }else{
        navb.classList.add('collapse')
    }
}