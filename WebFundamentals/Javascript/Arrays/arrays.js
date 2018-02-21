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

function numbersOnlyRemove (arr){
	"use strict";
	
		for (var i = 0; i < arr.length; i++) {
			
			while(typeof (arr[i]) !== "number"){
				
				for (var k = i; k < arr.length; k++) {
					
					arr[k] = arr[k+1];

				}
				arr.pop();
			}
		
		}
	
	return(arr);
}