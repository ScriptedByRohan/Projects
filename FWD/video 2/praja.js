var a = 10
console.log("the valus of a", a)
// 4 pillars 

var a = document.querySelector("h1")
console.log(a)

a.innerHTML= "CHANGED HTML"

a.style.color="red"
a.style.backgroundColor = "white"

a.addEventListener("click", function(){
    a.innerHTML = "CHANGED HTML (USING eventListner)"
    a.style.color = "white"
    a.style.backgroundColor="red"

})