
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

//Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

function call_beCheerful(){
	"use strict";
	for (var i=1; i<=98; ++i){
		beCheerful();
	}
}

function beCheerful(){
	"use strict";
	console.log("Good morning!");
}

//Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

function multiples3(){
	"use strict";
	for (var i=-300; i<=0; i+=3){
		if (i===-3 || i===-6){
			continue;
		}
		console.log(i);
	}
}

//Print integers from 2000 to 5280, using a WHILE.

function print_while(){
	"use strict";
	var i= 2000;
	while(i<=5280){
		console.log(i);
		i++;
	}
}

//If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",

function yourBirthday(x,y){
	"use strict";
	if((x===20 && y ===8) || (y===20 && x===8)){
		console.log("How did you know?");
	}
	else{
		console.log("Just another day...");
	}
}

//Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.

function leapYear(year){
	"use strict";
	
	if(year%400===0){
		console.log("Leap year.");
	}
	else if(year%100===0){
		console.log("Not a leap year.");
	}
	else if (year%4===0){
		console.log("Leap year");
	}
	else{
		console.log("Not a leap year.");
	}
	
	/*
	if( year%4 === 0 ){
		if( year%100 === 0 ){
			if( year%400 === 0 ){
				console.log("Leap year");
			}
			else{
				console.log("Not a leap year");
			}
		}
		else {
			console.log("Leap year");
		}
	}
	else{
		console.log("Not a leap year");
	}*/
}

//Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

function printAndCount(){
	"use strict";
	var count=0;
	for (var i=515; i<=4095; i+=5){
		console.log(i);
		count++;
	}
	console.log("There were "+count+" multiples of 5.");
}

//Print multiples of 6 up to 60,000, using a WHILE.

function multiplesofSix(){
	"use strict";
	var i=6;
	while(i<=60000){
		console.log(i);
		i+=6;
	}
}

//Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

function CodingDojo(){
	"use strict";
	for(var i=1; i<=100; ++i){
		if(i%5 === 0){
			if (i%10 === 0){
				console.log("Coding Dojo");
			}
			else{
				console.log("Coding");
			}
		}
		else{
			console.log(i);
		}
	}
}

//Your function will be given an input parameter incoming. Please console.log this value.

function whatdoYouKnow(incoming){
	"use strict";
	console.log(incoming);
}

//Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?

function oddintegers(){
	"use strict";
	var sum = 0;
	for (var i=-299999; i<300000; i+=2){
			sum += i;
	}
	console.log(sum);
}

//Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.

function positiveNumbers(){
	"use strict";
	var i= 2016;
	while(i>0){
		console.log(i);
		i -=4;
	}
}

//Based from earlier “Countdown By Fours”, given (lowNum, highNum, mult), print the numbers in multiples of mult from highNum down to lowNum, using a FOR loop.

function flexibleCountdown(lowNum, highNum, mult){
	"use strict";
	for (var i=highNum; i>lowNum; i--){
		if(i%mult===0){
			console.log(i);
		}
	}
}

//Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) that one. Do this using a WHILE loop.

function finalCountdown(param1, param2, param3, param4){
	"use strict";
	var i = param2;
	while( i <= param3){
		if (i%param1===0){
			if(i !== param4){
				console.log(i);
			}
		}
		++i;
	}
}