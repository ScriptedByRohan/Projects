var bul = document.querySelector("#bulb")
var but = document.querySelector("button")
var ck = 0

but.addEventListener("click", function(){
    if(ck == 0){
    bul.style.backgroundColor = "yellow"
    ck = 1
    but.innerHTML = "Off"
    }else {
        bul.style.backgroundColor = "white"
        ck = 0;
        but.innerHTML = "on"
    }
})