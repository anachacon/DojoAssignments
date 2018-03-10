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



