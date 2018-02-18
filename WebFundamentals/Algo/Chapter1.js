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

//Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

function greaterThanGeneralized(arr){
	"use strict";
	
	var count = 0;
	var newarr = [];
	
	if (arr.length === 1){
		return ("Only one value: " + arr[0]);
	}
	else{
		for (var i=0; i<arr.length; i++){
			if( arr[i] > arr[1]){
				count++;
				newarr.push(arr[i]);
			}	
			
		}
	console.log(count);
	return(newarr);
	}	
}

//Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

function thislength(num1, num2){
	"use strict";
	
	var arr = [];
	
	for(var i=0; i<num1; i++){
		arr.push(num2);
	}
	
	if(num1===num2){
		console.log("Jinx!");
	}
	
	return(arr);
	
}

//Your function should accept an array. If the value at [0] is greater than array’s length, print "Too big!"; if the value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

function fitTheFirst(arr){
	"use strict";
	
	if(arr[0] > arr.length){
		console.log("Too big!");
	}
	else if ( arr[0] < arr.length){
		console.log("Too small!");
	}
	else {
		console.log("Just right");
	}
	
}

//Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees. 

//For review, Fahrenheit = (9/5 * Celsius) + 32.


function fahrenheitToCelsius(fDegrees){
	"use strict";
	
	return (fDegrees-32) * 5/9;
}


