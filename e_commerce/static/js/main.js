const xbtn = document.querySelector('#close');
const alerta = document.querySelector('#alerta');

xbtn.onclick = () => cerrarAlerta();

function cerrarAlerta(){
    alerta.remove();
}