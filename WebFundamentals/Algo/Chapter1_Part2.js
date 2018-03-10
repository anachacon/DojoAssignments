//Given an array, write a function that changes all positive numbers in the array to “big”.

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

//Create a function that takes array of numbers. The function should print the lowest 
//value in the array, and return the highest value in the array.

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