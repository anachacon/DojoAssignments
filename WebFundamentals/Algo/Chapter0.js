
//Set variable myNumber to 42. Set variable myName to your name. Now swap myNumber into myName & vice versa.

function swap(){
	"use strict";
	var myNumber = 42;
	var myName = "Isabel";
	var temp = myNumber;
	myNumber = myName;
	myName = temp;
	console.log(myName);
}

//Print integers from -52 to 1066 using a FOR loop

function print_int(){
	"use strict";
	for (var i=-52; i<=1066; i++){
		console.log(i);
	}
}

//Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

function call_beCheerful(){
	"use strict";
	for (var i=1; i<=98; ++i){
		beCheerful();
	}
}

function beCheerful(){
	"use strict";
	console.log("Good morning!");
}

//Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

function multiples3(){
	"use strict";
	for (var i=-300; i<=0; i+=3){
		if (i===-3 || i===-6){
			continue;
		}
		console.log(i);
	}
}

//Print integers from 2000 to 5280, using a WHILE.

function print_while(){
	"use strict";
	var i= 2000;
	while(i<=5280){
		console.log(i);
		i++;
	}
}

//If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",

function yourBirthday(x,y){
	"use strict";
	if((x===20 && y ===8) || (y===20 && x===8)){
		console.log("How did you know?");
	}
	else{
		console.log("Just another day...");
	}
}

//Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.

function leapYear(year){
	"use strict";
	if( year%4 === 0 ){
		if( year%100 === 0 ){
			if( year%400 === 0 ){
				console.log("Leap year");
			}
			else{
				console.log("Not a leap year");
			}
		}
		else {
			console.log("Leap year");
		}
	}
	else{
		console.log("Not a leap year");
	}
}
