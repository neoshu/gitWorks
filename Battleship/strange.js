//set each td an id from "00" to "66"
function setId() {
    let tmp_list1 = [];
    for (let i=0; i<7; i++) {
        tmp_list1.push(i.toString());
    }
    let ids = [];
    for (let i=0; i<tmp_list1.length; i++) {
        for (let j=0; j<tmp_list1.length; j++) {
            ids.push(tmp_list1[i] + tmp_list1[j]);
        }
    }
    let tds = document.getElementsByTagName("td");
    for (let k=0; k<tds.length; k++) {
        tds[k].setAttribute("id", ids[k]);
    }
}
setId();

let message = {
    displayMsg: function(msg) {
        let messageArea = document.getElementById("messageForUser");
        messageArea.innerHTML = msg;
    },
    displayHit: function(location) {
        let cell = document.getElementById(location);
        cell.setAttribute("class", "hit");
    },
    displayMiss: function(location) {
        let cell = document.getElementById(location);
        cell.setAttribute("class", "miss");
    }
};

//convert eg. "A0" to "00" and fire
/*function Fire() {
    let myGuess = document.getElementById("guess").value; //What you input, it is string
    if (myGuess.length === 2) {
        if (myGuess[0]<="G" && myGuess[0]>="A" && myGuess[1]<=6 && myGuess[1]>=0) {
            let tmp=["A", "B", "C", "D", "E", "F", "G"];
            var result = tmp.indexOf(myGuess[0]) + myGuess[1]; // 1+"2" --> "12"
            console.log(result);
            
        }else {alert("The wrong input");}
    } else {alert("Only 2 characters allowed");}
    if (shipLocation.includes(result)) {
        message.displayMsg("You've hit it");
        message.displayHit(result);
    } else {
        message.displayMsg("You missed it");
        message.displayMiss(result);
    }
} */
let tmpList =[];
//Assign the ships location randomly according to the ships number
function assign() {
    let shipNum = document.getElementById("number").value;
    let chances = document.getElementById("guess").value; //If it is blank, value is ""

    if (shipNum < 50 && shipNum > 0 && chances !== "") {
        let Num = Number(shipNum); //ship number you entered
        let noRepeat = [];
        let start = 0;
        while (start < Num) {
            let p_lf = Math.floor(Math.random() * 7).toString();
            let p_rg = Math.floor(Math.random() * 7).toString();
            let position = p_lf + p_rg; //the random position
            if (noRepeat.includes(position)) {
                continue;
            }
            noRepeat.push(position);
            start++;
        }
        console.log(noRepeat);
        tmpList = noRepeat;
    } else {
        alert("Check the number or chances");
    }
    let countNum = document.getElementById("count");
    countNum.innerHTML = chances;
} 

//Set every cell a click behavior 
let cells = document.getElementsByTagName("td");
for (let i=0; i<cells.length; i++) {
    cells[i].setAttribute("onclick", "clickHere(this)");
}
let hitCount=[]; // To determine the hit total number
let judge = true; //The judge to terminate the game
function clickHere(target) {
    if (judge) {
        if (tmpList.includes(target.getAttribute("id"))) {
            target.setAttribute("class", "hit");
            hitCount.push(target.getAttribute("id"));
        } else {
            target.setAttribute("class", "miss");
        }
        let countLimit = document.getElementById("count");
        let tmp = countLimit.innerHTML;
        tmp = tmp - 1;
        countLimit.innerHTML = tmp;
        if (hitCount.length ==Number(document.getElementById("number").value) && tmp>=0) {
            alert("You win");
            judge = false;
        }
        if (hitCount.length<document.getElementById("number").value && tmp==0) {
            alert("You lose");
            judge = false;
        }
    }
    

}