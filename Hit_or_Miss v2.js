var rNum = 6;

var comp1 = [];
var ids = [];
for (var i = 0; i<=rNum; i++) {
    comp1.push(i.toString());
}
var comp2 = comp1;
var comp = [];
for (var i=0; i<comp1.length; i++) {
    for (var n=0; n<comp2.length; n++){
        comp.push(comp1[i] + comp2[n]);
    }
}

// To assign evert td an id and an onclick attribute
element_tds = document.getElementsByTagName("td");
for (var i=0; i<element_tds.length; i++) {
    element_tds[i].setAttribute("id", "t"+comp[i]);
    element_tds[i].setAttribute("onclick", "spot(this)");
} //Every td has id from t00 to t66

function getInputValue () {
    var inc = 0;
    var count = document.getElementById("input").value;
    if (count <= 49) { // count is a string instead of number
        while (inc < count) {
            var le = Math.floor(Math.random()*7).toString();
            var ri = Math.floor(Math.random()*7).toString();
            var adder = "t" + le + ri;
            if (ids.includes(adder)) {continue;}
            ids.push(adder);
            inc ++;
        }
    } else {alert("You should not enter a number greater than 49");}
    
}

function limit() {
    var chance = Number(document.getElementById("chance").value);
    var num = Number(document.getElementById("input").value);
    if ( chance<num) {
        alert("Are you kidding me?");
    }
}

// To estimate whether the td you spotted is the one in ids array, if true, 
// then add the background image
function spot(target) {
    var tmp = target.getAttribute("id");
    if (ids.includes(tmp)) {
        target.setAttribute("class", "addShip");
    }
}

