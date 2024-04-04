var coup=0;
var joueur=["1","2","1","2","1","2","1","2","1","1","2"];
var debut=["e2","e7","g1","b8","f1","a7","b5","g8","e1","h1","f8"];
var fin=["e4","e5","f3","c6","b5","a6","a4","f6","g1","f1","e7"];

var lettres=["a","b","c","d","e","f","g","h"];

var noirs={"a8":"&#9820;","b8":"&#9822;","c8":"&#9821;","d8":"&#9819;","e8":"&#9818;","f8":"&#9821;","g8":"&#9822;","h8":"&#9820;","a7":"&#9823;","b7":"&#9823;","c7":"&#9823;","d7":"&#9823;","e7":"&#9823;","f7":"&#9823;","g7":"&#9823;","h7":"&#9823;"};

var blancs={"a2":"&#9817;","b2":"&#9817;","c2":"&#9817;","d2":"&#9817;","e2":"&#9817;","f2":"&#9817;","g2":"&#9817;","h2":"&#9817;","a1":"&#9814;","b1":"&#9816;","c1":"&#9815;","d1":"&#9813;","e1":"&#9812;","f1":"&#9815;","g1":"&#9816;","h1":"&#9814;"};

function createHLine(echiquier) {
  var case1=document.createElement("div");
  case1.setAttribute("class","numeroHV");
  echiquier.appendChild(case1);
  for(var j=0;j<8;j++) {
    var case2=document.createElement("div");
    case2.setAttribute("class","numeroH");
    case2.innerHTML=lettres[j].toUpperCase();
    echiquier.appendChild(case2);
  }
  case1=document.createElement("div");
  case1.setAttribute("class","numeroHV");
  echiquier.appendChild(case1);
}
function createEchiquier(echiquier) {
  createHLine(echiquier);
  for(var i=8;i>0;i--) {
    var case1=document.createElement("div");
    case1.setAttribute("class","numeroV");
    case1.innerHTML=i;
    echiquier.appendChild(case1);
    for(var j=0;j<8;j++) {
      // Q2
      var case2=document.createElement("div");
      var couleurCase="noir";
      if ((i+j)%2==0) couleurCase="blanc";
      case2.setAttribute("class",couleurCase);
      // finQ2
      case2.setAttribute("id",lettres[j]+i);
      echiquier.appendChild(case2);
    }
    case1=document.createElement("div");
    case1.setAttribute("class","numeroV");
    case1.innerHTML=i;
    echiquier.appendChild(case1);
  }
  createHLine(echiquier);
}
// Q1
var e=document.getElementById("echiquier");
createEchiquier(e);

// finQ1
// Q3
for(id in noirs) {
var c=document.getElementById(id);
c.innerHTML=noirs[id]; }
for(id in blancs) {
var c=document.getElementById(id);
c.innerHTML=blancs[id]; }
// finQ3
// Q4 
var btn=document.getElementById("next");
btn.addEventListener("click",next);
function next() 
}