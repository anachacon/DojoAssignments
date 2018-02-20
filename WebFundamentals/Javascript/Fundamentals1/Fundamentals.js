//FANCY ARRAY

function fancyArray(arr){
	"use strict";
	
	var reversed = arr.pop();
	var character = arr.pop();

	if( reversed === true){
		for (var i=(arr.length-1); i>=0; i--){
		console.log(i+" "+character+" "+arr[i]);
		}
	}
	else{
		for (var j=0; j < arr.length; j++){
		console.log(j+" "+character+" "+arr[j]);
		}
	}
	
}