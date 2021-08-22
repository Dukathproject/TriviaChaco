//GET ELEMENTS

var question = document.getElementById("question").value;
console.log(question)
var boton1 = document.getElementById("boton1");
var boton2 = document.getElementById("boton2");
var boton3 = document.getElementById("boton3");
var textoRespuesta1 = document.getElementById("textoRespuesta1");
var textoRespuesta2 = document.getElementById("textoRespuesta2");
var textoRespuesta3 = document.getElementById("textoRespuesta3");
var timer = document.getElementById("timer")
var time = 10


console.log(boton1.value)
console.log(textoRespuesta1.textContent)



//CUENTA REGRESIVA
setInterval(function(){
    if (time > 0){
        time--
        timer.textContent = 'Tiempo restante: ' + time;
    }else {
        timer.textContent = 'FIN DE LA PARTIDA!';
    }
}, 1000);




//     //UPDATE HTML
//     selectedStory.classList.add("animatedTransition");
//     bodyText.textContent = storyNum.bodytext;
//     if(storyNum.name != ""){
//         userName.textContent = storyNum.name;
//     }else{
//         userName.textContent = "Anonymous";
//     };
//     place.textContent = storyNum.place;
//     date.textContent = storyNum.date;
// }

// var stories = [];
// //GET DATABASE LIST
// fetch('/storiesList').then(res => res.json()).then(function(json) {
//     //POPULATE STORIES TO VAR
//     json.forEach(function(story){
//         stories.push(story);
//     });
//     changeStory();
//     setInterval(function(){
//         changeStory();
//     }, 8000);
// });