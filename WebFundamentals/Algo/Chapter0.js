
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

