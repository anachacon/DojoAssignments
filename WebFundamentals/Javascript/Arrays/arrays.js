//Make a function that copies an array, ONLY accepting the items that are numbers.

function numbersOnly (arr){
	"use strict";
	
	var newArr = [];
	
	for (var i=0; i<arr.length; i++){
		
		if(typeof arr[i]==="number"){
			newArr.push(arr[i]);
		}
				
	}

	return(newArr);
	
}