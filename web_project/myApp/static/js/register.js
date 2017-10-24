document.getElementById("schools").addEventListener("click",change_pic,false);
function change_pic(thing){
  var element = document.getElementById("schools");
  var school = element.options[element.selectedIndex].value;
  print("why");
  element.style.backgroundImage = 'url(/static/images/UCLA.jpg)';
  if(thing.className.match(/(?:^|\s)ChicoState(?!\S)/)){
    var pic = document.getElementByID("schools").elements;
    var obj = {}
  }
}
