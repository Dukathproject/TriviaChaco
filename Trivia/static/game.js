//OBTENER ELEMENTOS DEL HTML
var question = document.getElementById("question").textContent;
var question_parsed = JSON.parse(question);
var questionDiv = document.getElementById("question");
questionDiv.remove();
var númeroPregunta = document.getElementById("númeroPregunta");
var categoría = document.getElementById("categoría");
var questionFormula = document.getElementById("questionFormula");
var timer = document.getElementById("timer");
var time = 15;

//PUNTAJE
var puntaje = 0;
var nPregunta = 1;

function sigPregunta(){
    //ACTUALIZADO DE TEXTOS
    númeroPregunta.textContent = "Pregunta nº: " + nPregunta;
    questionFormula.textContent = question_parsed['question_' + nPregunta]['formula'];
    categoría.textContent = "Categoría : " + question_parsed['question_' + nPregunta]['categoría'];

    //ACTUALIZADO DE RESPUESTAS
    var cont = 0;
    for(var i = 1; i <= question_parsed['question_' + nPregunta]['respuestas'].length; i++){
        var botón = document.getElementById("botón" + i);
        botón.value = question_parsed['question_' + nPregunta]['respuestas'][cont]['respuesta_' + (i)]['formula'];
        cont++;
    };
    cont = 0;
}

//CUENTA REGRESIVA
setInterval(function(){
    if (time > 0){
        time--
        timer.textContent = 'Tiempo restante: ' + time;
    }else {
        timer.textContent = 'Tiempo agotado. ¡FIN DE LA PARTIDA!';
    }
}, 1000);

//BOTON DE SELECCIÓN
function selección(boton) {
    var check = question_parsed['question_' + nPregunta]['respuestas'][boton-1]['respuesta_' + boton]['correcta'];
    if(check === true){
        console.log(check === true);
        puntaje++;
        nPregunta++;
        time = 15;
        sigPregunta();
    }else{
        //FINALIZAR EL JUEGO
    };
}
sigPregunta()