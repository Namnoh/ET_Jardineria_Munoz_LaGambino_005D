// IMPLEMENTACIÓN DE DOM'S

// 1. DOM: MOUSEOVER
// title_color_mouseover.addEventListener('mouseout', function(e) {
function mouseover(e) {
    // CAMBIAR EL COLOR O DISEÑO AL TENER EL MOUSE ENCIMA
    e.style.color = "rgba(173, 58, 167, 0.801)";
    e.style.fontSize = "40px";
    e.style.transitionDuration = ".5s";
  
    // RESETEAR EL COLOR DESPUÉS DE UN TIEMPO
    // setTimeout(function() {
    //   event.target.style.color = "";
    // }, 500);
};

// 2. DOM: MOUSELEAVE
// title_color_mouseover.addEventListener('mouseout', e => {
function mouseout(e) {
    // CAMBIAR EL COLOR O DISEÑO AL TENER EL MOUSE AFUERA
    e.style.color = "black";
    e.style.fontSize = "35px";
};

// 3. DOM: CAMBIAR NOMBRE
function persons_name() {
    var a = prompt('Escribe tu nombre: ');
    if (a == null)
        document.getElementById('real_name').innerHTML = "¡Bienvenid@ a la sección de utilidades!";
    else
        document.getElementById('real_name').innerHTML = "¡Bienvenid@ " + a + " a la sección de utilidades!";
}

// 4. DOM: CLICK BOTÓN CLIMA
function click_clima(e) {
    var text = e.textContent;
    e.innerHTML = "Datos Entregados"
    setTimeout(function() {
        e.innerHTML = text;
    }, 1000);
}


// IMPLEMENTACIÓN DE RUTINA

//Declaramos variables
var operandoa;
var operandob;
var operacion;

function cal(){
    //variables
    var resultado = document.getElementById('resultado');
    var reset = document.getElementById('reset');
    var suma = document.getElementById('suma');
    var resta = document.getElementById('resta');
    var multiplicacion = document.getElementById('multiplicacion');
    var division = document.getElementById('division');
    var igual = document.getElementById('igual');
    var uno = document.getElementById('uno');
    var dos = document.getElementById('dos');
    var tres = document.getElementById('tres');
    var cuatro = document.getElementById('cuatro');
    var cinco = document.getElementById('cinco');
    var seis = document.getElementById('seis');
    var siete = document.getElementById('siete');
    var ocho = document.getElementById('ocho');
    var nueve = document.getElementById('nueve');
    var cero = document.getElementById('cero');
    //Eventos de click
      uno.onclick = function(e){
        resultado.textContent = resultado.textContent  + "1";
    }
    dos.onclick = function(e){
        resultado.textContent = resultado.textContent  + "2";
    }
    tres.onclick = function(e){
        resultado.textContent = resultado.textContent  + "3";
    }
    cuatro.onclick = function(e){
        resultado.textContent = resultado.textContent  + "4";
    }
    cinco.onclick = function(e){
        resultado.textContent = resultado.textContent  + "5";
    }
    seis.onclick = function(e){
        resultado.textContent = resultado.textContent  + "6";
    }
    siete.onclick = function(e){
        resultado.textContent = resultado.textContent  + "7";
    }
    ocho.onclick = function(e){
        resultado.textContent = resultado.textContent  + "8";
    }
    nueve.onclick = function(e){
        resultado.textContent = resultado.textContent  + "9";
    }
    cero.onclick = function(e){
        resultado.textContent = resultado.textContent  + "0";
    }
    reset.onclick = function(e){
        resetear();
    }
    suma.onclick = function(e){
        operandoa = resultado.textContent;
        operacion = "+";
        limpiar();
    }
    resta.onclick = function(e){
        operandoa = resultado.textContent;
        operacion = "-";
        limpiar();
    }
    multiplicacion.onclick = function(e){
        operandoa = resultado.textContent;
        operacion = "*";
        limpiar();
    }
    division.onclick = function(e){
        operandoa = resultado.textContent;
        operacion = "/";
        limpiar();
    }
    igual.onclick = function(e){
        operandob = resultado.textContent;
        resolver();
    }
}

function resolver(){
    var res = 0;
    switch(operacion){
      case "+":
        res = parseFloat(operandoa) + parseFloat(operandob);
        break;
      case "-":
          res = parseFloat(operandoa) - parseFloat(operandob);
          break;
      case "*":
        res = parseFloat(operandoa) * parseFloat(operandob);
        break;
      case "/":
        res = parseFloat(operandoa) / parseFloat(operandob);
        break;
    }
    resetear();
    resultado.textContent = res;
}

function limpiar(){
    resultado.textContent = "";
}
function resetear(){
    resultado.textContent = "";
    operandoa = 0;
    operandob = 0;
    operacion = "";
}

// IMPLEMENTACIÓN DE API
let url = "http://api.weatherunlocked.com/api/current/40.71,-74.00?app_id=4de9ee47&app_key=4cd0b063f0678fe3b913cc3561b1f535"
$("#enviar").click(function(){
    $.get(url, function(data){
        $("#api_data").append(
            "<tr><td class='weather'>" + data.temp_c + " C°" + "</td>" +
            "<td class='weather'>" + data.humid_pct + " %" + "</td>" +
            "<td class='weather'>" + data.windspd_kmh + " km/h" + "</td>" +
            "<td class='weather'>" + data.wx_desc + "</td> </tr>"
            );
    }, "json");
});

function btnover(e) {
    // CAMBIAR EL COLOR O DISEÑO AL TENER EL MOUSE ENCIMA
    // e.style.color = "rgba(173, 58, 167, 0.801)";
    e.style.fontSize = "20px";
    e.style.transitionDuration = "1s";
};

// 2. DOM: MOUSELEAVE

function btnout(e) {
    // CAMBIAR EL COLOR O DISEÑO AL TENER EL MOUSE AFUERA
    // e.style.color = "black";
    e.style.fontSize = "16px";
};