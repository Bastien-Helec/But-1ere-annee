var jours=[1,2,3,4,5,6,7,8,9,10];
var tmin=[7.0,7.0,4.4,2.7,8.2,2.3,4.1,5.5,11.6,8.2];
var courbe1={
  label: "Température minimum en °C",
  backgroundColor: "darkcyan",
  borderColor: "darkcyan",
  data: tmin,
  pointRadius: 5,
  pointHoverRadius: 10,
  fill: false
};
var wind = [68.5,79.6,42.6,64.8,50.0,18.5,18.5,38.9,38.9,35.2]
var courbe2={
  label: "Vitesse du vent en km/h",
  backgroundColor: "darkorchid",
  borderColor: "darkorchid",
  data: wind,
  pointRadius: 5,
  pointHoverRadius: 10,
  fill: false
};

var colors =["black","yellow","blue","magenta","aqua","coral","red","chartreuse"];

var config={
  type: "line",
  data: {labels: jours, datasets: [courbe1]},
  options: {
    title: {display: true, text: "Béziers en 2007"}
  }

};

window.onload=function() {
  var ctx=document.getElementById("canvas").getContext("2d");
  config.data.datasets.push(courbe2);
  window.graph1=new Chart(ctx,config);
};

// Q2  faire une boucle sur les elements d'un tableau en creant des balises option avec l'attribut value et le contenu de l'element, puis en l'ajoutant a la liste deroulante 

var colors=colors.sort()
console.log(colors);
var select=document.getElementById("couleurs");

for (var i=0;i<colors.length;i++) {
  var opt=document.createElement("option");
  opt.setAttribute("value",colors[i]);
  opt.innerHTML=colors[i];
  select.appendChild(opt);
};
// Q3 
var selectCouleur=document.getElementById("couleurs");
selectCouleur.addEventListener("change", function() {
var val=this.options[this.selectedIndex].value;
var txt=this.options[this.selectedIndex].text;
console.log("Couleur "+this.selectedIndex+": "+val+" -> "+txt);

//  modification du backgroundcolor et bordercolor de la courbe1
courbe1.backgroundColor=val;
courbe1.borderColor=val;
window.graph1.update();
});

//Q4 

var axeX={
  display: true,
  scaleLabel: {display: true, labelString: "Numéro du jour"}
  };
  var axeY1={
    id: "yTmin",
  position: "left",
  ticks: {suggestedMin: 2, suggestedMax: 12},
  display: true,
  scaleLabel: {display: true, labelString: "Température en °C"}
  };
  var axeY2={
    id: "yWind",
  position: "right",
  ticks: {suggestedMin: 0, suggestedMax: 100},
  display: true,
  scaleLabel: {display: true, labelString: "Vitesse du vent en km/h"}
  };
  config.options.scales={xAxes: [axeX], yAxes: [axeY1],};
  
// Q5
var selectinput=document.getElementById("echelles");
//  avec this 
selectinput.addEventListener("change", function() {
  config.options.scales.xAxes[0].scaleLabel.display=this.checked;
config.options.scales.yAxes[0].scaleLabel.display=this.checked;
window.graph1.update();
if (this.checked==true) {
  console.log("affichage actif");} else {
    console.log("affichage inactif");
  }
});
