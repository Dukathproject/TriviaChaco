//OBTENER DATOS PARA RANKING
var result = document.getElementById("id_result");
var correct = document.getElementById("id_correcta");
var incorrect = document.getElementById("id_incorrecta");
var pregunta = document.getElementById("id_pregunta");

//OBTENER ELEMENTOS DEL HTML
var question = document.getElementById("question").textContent;
var question_parsed = JSON.parse(question);
var questionDiv = document.getElementById("question");
questionDiv.remove();
var númeroPregunta = document.getElementById("númeroPregunta");
var categoría = document.getElementById("categoría");
var questionFormula = document.getElementById("questionFormula");
var timer = document.getElementById("timer");
var congrats = document.getElementById("congrats");
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
    var boton3 = document.getElementById('b3');
    if(question_parsed['question_' + nPregunta]['respuestas'][2]){
        boton3.style.display= "Block";
    }else{
        boton3.style.display= "None";
    }
    cont = 0;
}

//CUENTA REGRESIVA
setInterval(function(){
    if (time > 0){
        time--
        timer.textContent = 'Tiempo restante: ' + time;
    }else {
        timer.textContent = 'Tiempo agotado. ¡FIN DE LA PARTIDA!';
        setTimeout(function(){
            //GUARDAR VALOR TOTAL
        result.value = puntaje;
        //GUARDAR VALOR PREGUNTA
        pregunta.value = questionFormula.textContent;
        //GUARDAR VALOR DE RESPUESTA CORRECTA
        for(var i = 1; i <= 3; i++){
            var correct_answer = question_parsed['question_' + nPregunta]['respuestas'][i-1];
            if(correct_answer['respuesta_' + i]['correcta'] === true){
                correct.value = correct_answer['respuesta_' + i]['formula'];
            }
        }
        //GUARDAR VALOR DE RESPUESTA INCORRECTA
        incorrect.value = "-"
        document.getElementById("result").submit();
        //FINALIZAR EL JUEGO
            }, 1000);
    }
}, 1000);


// function congratsText(){
//     congrats.textContent = "¡MUY BIEN!";
//     setTimeout(function(){
//         congrats.textContent = "";;
//         }, 3000);
// }
function congratsDisplay(){
    congrats.style.display = "Block";
    congrats.classList.add("shake");
    setTimeout(function(){
        congrats.style.display = "None";
        congrats.classList.remove("shake");
        }, 3000);
}

//BOTON DE SELECCIÓN
function selección(boton) {
    var check = question_parsed['question_' + nPregunta]['respuestas'][boton-1]['respuesta_' + boton]['correcta'];
    if(check === true){
        puntaje++;
        nPregunta++;
        time = 15;
        // congratsText();  
        congratsDisplay();  
        sigPregunta();
    }else{
        //GUARDAR VALOR TOTAL
        result.value = puntaje;
        //GUARDAR VALOR PREGUNTA
        pregunta.value = questionFormula.textContent;
        //GUARDAR VALOR DE RESPUESTA CORRECTA
        for(var i = 1; i <= 3; i++){
            var correct_answer = question_parsed['question_' + nPregunta]['respuestas'][i-1];
            if(correct_answer['respuesta_' + i]['correcta'] === true){
                correct.value = correct_answer['respuesta_' + i]['formula'];
            }
        }
        //GUARDAR VALOR DE RESPUESTA INCORRECTA
        incorrect.value = question_parsed['question_' + nPregunta]['respuestas'][boton-1]['respuesta_' + boton]['formula'];
        document.getElementById("result").submit();
        //FINALIZAR EL JUEGO
    };
}
sigPregunta()