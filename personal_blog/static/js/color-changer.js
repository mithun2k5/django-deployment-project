// taking the help from stackoverflow.

function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = "#";
  for (var i = 0; i <6; i++){
    color = color + letters[Math.floor(Math.random()*16)];
  }
  return color;
}

function changeHeaderColor(){
  Inputcolor = getRandomColor();
  document.getElementById("two").style.color = Inputcolor;
}

setInterval("changeHeaderColor()",500);
