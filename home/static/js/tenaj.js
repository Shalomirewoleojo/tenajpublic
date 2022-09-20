var array = document.querySelector(".array");
// var drop = document.querySelector("#drop");
// var down = document.querySelector(".down");
const menu2 = document.querySelector("#menu");

// drop.addEventListener('mouseover', down1);
// drop.addEventListener('mouseout', up);

array.style.height = "0vh";
// down.style.display = "none";

function menu() {
    if (array.style.height == "0vh"){
        array.style.height = "200px";
    }
    else {
        array.style.height = "0vh";
    }
    
}

let clicked = false;
menu2.addEventListener("click", () =>{
    if (!clicked) {
        clicked = true;
        menu2.innerHTML = 'close';
    }
    else {
        clicked = false;
        menu2.innerHTML = 'menu';
    }
})

// function down1(){
//     if(screen.max-width == '767px'){
//         if (down.style.display == "none"){
//             down.style.display = "block";
//             array.style.height = "";
//         }

//     }
// }

// function up(){
//     if(screen.max-width == '767px'){
//         if (down.style.display == "block" ){
//             down.style.display = "none"
//         }
//     }
// }