//OBTENER ELEMENTOS DEL HTML
var question = document.getElementById("question").textContent;
var question_parsed = JSON.parse(question);
var questionDiv = document.getElementById("question");
questionDiv.remove();
var boton1 = document.getElementById("boton1");
var boton2 = document.getElementById("boton2");
var boton3 = document.getElementById("boton3");
var númeroPregunta = document.getElementById("númeroPregunta");
var categoría = document.getElementById("categoría");
var questionFormula = document.getElementById("questionFormula");
var timer = document.getElementById("timer");
var time = 10;

//PUNTAJE
var puntaje = 0;
var nPregunta = puntaje + 1;

//ACTUALIZADO DE TEXTOS
númeroPregunta.textContent = "Pregunta nº: " + nPregunta;
questionFormula.textContent = question_parsed['question_' + nPregunta]['formula'];
categoría.textContent = "Categoría : " + question_parsed['question_' + nPregunta]['categoría'];

//ACTUALIZADO DE RESPUESTAS
var cont = 0;
for(var i = 1; i <= question_parsed['question_' + nPregunta]['respuestas'].length; i++){
    var textoRespuesta = document.getElementById("textoRespuesta" + (i));
    textoRespuesta.textContent = question_parsed['question_' + nPregunta]['respuestas'][cont]['respuesta_' + (i)]['formula'];
    cont++;
};
cont = 0;

//CUENTA REGRESIVA
setInterval(function(){
    if (time > 0){
        time--
        timer.textContent = 'Tiempo restante: ' + time;
    }else {
        timer.textContent = 'Tiempo agotado. ¡FIN DE LA PARTIDA!';
    }
}, 1000);