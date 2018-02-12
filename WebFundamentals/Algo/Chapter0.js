
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
