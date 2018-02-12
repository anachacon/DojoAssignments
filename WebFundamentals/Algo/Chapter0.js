
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