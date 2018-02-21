//RANDOM CHANCE

	//WIN -> random between 50 - 100
	//Use math.random and math.floor to pick random number of coins
	//Use math.random to determine if they won

function randomChance(quarters){
	"use strict";
	
	for (var i=quarters; i>0; i--){
	
		var random = Math.floor((Math.random() * 100) + 1);
		
			if (random === 70){
				var price = Math.floor(Math.random() * 50)+50;
				return (i + price);
			}
	}
	
	return(0);
	
}

	
	
	
	