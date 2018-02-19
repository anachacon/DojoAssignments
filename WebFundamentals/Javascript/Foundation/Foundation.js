/*Declare variables of the following types:
4 Numbers
3 Strings
2 Booleans
1 Undefined Variable
Give the variables descriptive names (ex: string1 and string2)
Print each one to the console with a description (ex: console.log("The First String:", string1);)
Try to be creative! (don't use 1, 2, 3, and 4 for your numbers -- test out negatives or decimals!)*/

function DoDeclare(){
	"use strict";
	var day= 18;
	var temp= -40;
	var weekday= 7;
	var month= 2;
	
	var channel="Weather report";
	var name="Isabel Chacon";
	var location="Seattle";
	
	var snowing= false;
	var raining = true;
	
	var sunny;
	
	console.log("Hello, my name is: "+name+". This is the "+channel+" for "+location+". This is the "+month+" month of the year, "+day+" day of the month and "+weekday+" day of the week. The temperature will be "+temp+" degrees. Changes of snowing are "+snowing+" and of rain are "+raining+". Sun conditions are "+sunny);
}

//Can I have the time

function tellTime(hour, minute, period){
	"use strict";
	
	var message= "It's ";
	
	if(minute < 30){
		message += "just after " +hour;
	}
	else if(minute > 30){
		if(hour===12){
			hour--;
		}
		message += "almost "+(hour+1);
	}
	else{
		message += "half past "+ hour;
	}
	
	if(period==="AM"){
		message += " in the morning.";
	}
	else{
		message += " in the evening.";
	}
	
	console.log(message);
}


//Days until my bday

function birthday(days){
	"use strict";
	
	for(var i=days; i>=0; --i){
		if (i >= 30){
		console.log(i+" days until my birthday. Such a long time... =(");
		}
		else if(i <30 && i > 5){
			console.log(i+" days until my birthday. We're getting closer =)!");
		}
		else if(i>0){
			console.log(i+" DAYS UNTIL MY BIRTHDAY!!!");
		}
		else{
			console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
			console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
			console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");
		}
	}
	
}






