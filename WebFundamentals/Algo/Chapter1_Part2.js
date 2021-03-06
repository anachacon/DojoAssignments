/*Given an array, write a function that changes all positive numbers in the array to “big”.*/

function biggieSize(arr){
    for (var i=0; i<arr.length; ++i){
        if(arr[i]>0){
            arr[i]="Big";
        }
    }
}

arr = [1,-3,-5,0,3,4,-6];
biggieSize(arr);
//console.log(arr);

/*Create a function that takes array of numbers. The function should print the lowest 
value in the array, and return the highest value in the array.*/

function printandreturn(arr){
    var low=0;
    var high=0;
    for (var i=0; i<arr.length; i++){
        if (arr[i] > high){
            high = arr[i];
        }
        else if (arr[i] < low){
            low = arr[i];
        }
    }
    console.log(low);
    return high;     
}

arr = [1,-3,-5,0,3,4,-6];
console.log(printandreturn(arr));

/*Build a function that takes array of numbers.
The function should print second-to-last value in the array, 
and return first odd value in the array.*/

function printsecond(arr){
    console.log(arr[arr.length-2]);
    for (var i =0; i<arr.length; i++){
        if (arr[i]%2 != 0){
            return(arr[i]);
        }
    }
}

arr = [10,20,30,3];
console.log(printsecond(arr));


/*Given array, create a function to return a new array 
where each value in the original has been doubled. Calling double([1,2,3]) 
should return [2,4,6] without changing original.*/


function doublevision(arr){
    var Newarr=[];
    for (var i=0; i<arr.length; i++){
        Newarr[i]=arr[i]*2;
    }
    return Newarr;
}

arr=[1,2,3];
console.log(doublevision(arr));

/*Given array of numbers, create function to replace last value with number of positive values.
Example: countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.*/

function countpositives(arr){
    var counter=0;
    for (var i=0; i<arr.length; i++){
        if (arr[i]>0){
            counter++;
        }
    }
    arr[arr.length-1] = counter;
}

var arr=[-1,-1,1,1,1,1];
countpositives(arr);
console.log(arr);

/*Create a function that accepts an array. Every time that array has three odd values in a 
row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"*/

function thatsodd(arr){
    var odd=0;
    var even=0;
    for(var i=0; i<arr.length; i++){
        if (arr[i]%2 == 0){
            ++even;
            if(even==3){
                console.log("Even more so!");
                even = 0;
            }
        }
        else{
            ++odd;
            if(odd==3){
                console.log("That's odd!");
                odd = 0;
            }
        }
    }    
}

arr = [3,3,3,2,2,2,1,2,3,1,1];
thatsodd(arr);
