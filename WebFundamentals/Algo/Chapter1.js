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

//Your function will receive an array with two numbers. Print the first value, and return the second.

function printReturn(arr){
	"use strict";
	console.log(arr[0]);
	return arr[1];
}

//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).


function firstPlusLength(arr){
	"use strict";
	
	if(isNaN(arr[0])){
		return ("Wrong data type");
	} 
	else{
		return arr[0] + arr.length;
	}
	
}

//For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

function greaterThanSecond(){
	"use strict";
	
	var arr= [1,3,5,7,9,13];
	var count = 0;
	
	for (var i=0; i<arr.length; i++){
		if( arr[i] > arr[1]){
			count++;
			console.log(arr[i]);
		}		
	}
	
	return(count);
}

