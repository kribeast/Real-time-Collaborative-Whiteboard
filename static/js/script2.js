let canvas = document.getElementById("demo-canvas");
const context = canvas.getContext("2d");
const undoButton = document.getElementById('undo-btn');
const redoButton = document.getElementById('redo-btn');


canvas.width = window.innerWidth- 20;
canvas.height = window.innerHeight;

let x;
let y;
let mouseDown = false;


window.onmousedown = (e) => {
  x = e.clientX;
  y = e.clientY;
  context.moveTo(x, y);
  mouseDown = true;
};

window.onmouseup = (e) => {
  mouseDown = false;
};

let undoStack = [];
let redoStack = [];

window.onmousemove = (e) => {
  x = e.clientX;
  y = e.clientY;

  if (mouseDown) {
    context.lineTo(x, y);
    context.stroke();

    undoStack.push({
      action: 'draw',
      x: x,
      y: y
    });
    // console.log(undoStack);
    redoStack = [];
  }
};

function undo() {
  if (undoStack.length > 0) {
    let lastAction = undoStack.pop(); 
    if (lastAction.action === 'draw') {
      context.clearRect(0, 0, canvas.width, canvas.height);
      redrawUndoStack();
    }
    redoStack.push(lastAction);
  }
}

function redo() {
  if (redoStack.length > 0) {
    let lastAction = redoStack.pop();
    if (lastAction.action === 'draw') {
      context.lineTo(lastAction.x, lastAction.y);
      context.stroke();
      undoStack.push(lastAction);
    }
  }
}

undoButton.addEventListener('click', undo);
redoButton.addEventListener('click', redo);

function clearCanvas() {
  context.clearRect(0, 0, canvas.width, canvas.height);
  undoStack = [];
  redoStack = [];
  context.beginPath()
}

function redrawUndoStack() {
  context.beginPath();
  for (let i = 0; i < undoStack.length; i++) {
    // console.log(undoStack);
    let action = undoStack[i];
    if (action.action === 'draw') {
      context.lineTo(action.x, action.y);
    }
  }
  context.stroke();
}

