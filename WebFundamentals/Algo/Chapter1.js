//Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?

function countdown(number){
	"use strict";
	var arr = [];
	
	for(var i=number; i>=0; i--){
		arr.push(i);
	}

	console.log("Array lenght is: "+(number+1));
	return arr;
		
}