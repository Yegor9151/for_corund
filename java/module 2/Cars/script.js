let tm;
let cars;
let cx;
let gameBegin; // 1 - игра запущена, 0 - игра не запущена

function timerGo() {
    for(let i = 0; i < 5; i++) {
        cx[i] = cx[i] - Math.floor((Math.random() * 7 + 2));

        if(cx[i] <= 30) {
            window.clearInterval(tm);
            gameBegin = 0;
            cars[i].style.border = "5px ridge yellow";
            return
        }
        cars[i].style.left = "" + cx[i] + "px";
    }
}

function go() {
    // alert("Hello");
    if(gameBegin == 1) return;
    gameBegin = 1;

    cars = new Array();
    for(let i = 0; i < 5; i++){
        cars[i] = document.getElementById("p" + i);
        cars[i].style.border = "none";
    }
    cx = new Array();
    for(let i = 0; i < 5; i++){
        cx[i] = 600;
    }
    tm = window.setInterval(timerGo, 50)
}