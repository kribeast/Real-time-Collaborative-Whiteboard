let canvas = document.getElementById('demo-canvas');
let ctx = canvas.getContext("2d");

canvas.width = 0.98 *window.innerWidth;
canvas.height = window.innerHeight;


let x;
let y;
let mouseDown = false

window.onmousedown = (e) =>{
    ctx.moveTo(x, y);
    mouseDown = true
}

window.onmouseup = (e) =>{
    mouseDown = false
}

window.onmousemove = (e) =>{
    x=e.clientX;
    y=e.clientY;
    
    if(mouseDown){
        ctx.lineTo(x,y)
        ctx.stroke()
    }
}