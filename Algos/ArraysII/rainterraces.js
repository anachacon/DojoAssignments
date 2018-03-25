 function rainTerraces(arr){

    var start = false; //Found beginning of bucket
    var end = false; //Found end of bucket
    var startIndex = 0; //Bucket initial index
    var startHeight = 0; //Bucket initial Height
    
    var bucketLength = 0; //Bucket horizontal size
    var maxHeight = 0; //Max height to determine end of bucket
    var maxIndex = 0; //Max height index

    var localSum = 0; //Water inside bucket
    var totalSum = 0; //Total water

    for (var i=0; i<arr.length; i++){

        //Find Start of Bucket
        if (!start){
            if(arr[i]>arr[i+1]){
                startIndex = i;
                startHeight = arr[i];
                start = true;
                continue;
            }
            continue;
        }
        //Found start on bucket, assume end of bucket will be same height and start adding!
        if(arr[i+1]){
            if(arr[i]<startHeight ){ 
                if(arr[i]>=maxHeight){
                    maxHeight = arr[i];
                    maxIndex = i;
                }
                localSum += (startHeight - arr[i]);
                bucketLength ++;
                end = false;
            }

            //How to determine end of bucket when it never reaches equal height
            else {//Reached end of current bucket
                bucketLength = 0;
                totalSum += localSum;
                localSum = 0;
                startHeight = arr[i];
                startIndex = i;
                end = true; //Found end of bucket
            }
        }
        else{//Reached end of array
            if (!end){ //Last bucket was never closed

                console.log(arr[i]);
                /*if (i > maxIndex  && arr[i] < arr[i-1]){
                    localSum -= startHeight - arr[i];
                }*/

                if(i > maxIndex && arr[i] > arr[i-1]){
                    //maxHeight is not at end of array
                    var lenlocal = maxIndex - startIndex;
                    var difference = (startHeight - maxHeight) * lenlocal;
                    localSum -= difference;
                    console.log("Sum: "+localSum);

                    if (maxIndex - startIndex == 1 && i - maxIndex > 1){
                        maxHeight = startHeight;
                        maxIndex++;
                    }

                    lenlocal = i - maxIndex;
                    difference = (maxHeight - arr[i]) * lenlocal;
                    localSum -= difference;
                }
                else if(arr[i]<startHeight){
                    var difference = (startHeight - maxHeight) * bucketLength;
                    localSum -= difference;
                }
                totalSum += localSum;
            }
            if (maxIndex > 1){
                return totalSum;
            }
            else {
                return 0;
            }
        } 
    }
    return 0;
 }


//Keoni tester funct
function testRainTerrace(func) {
    var tests = [
      {
        given: [3, 1, 1, 4, 2],
        expects: 4
      },
      {
        given: [1, 1, 1, 1, 1],
        expects: 0
      },
      {
        given: [],
        expects: 0
      },
      {
        given: [12, 1, 12, 1, 12],
        expects: 22
      },
      {
        given: [12, 11, 10, 9, 8],
        expects: 0
      },
      {
        given: [3, 1, 2, 1, 4, 2, 1],
        expects: 5
      },
      {
        given: [1, 2, 3, 4, 5, 6, 7, 8],
        expects: 0
      },
      {
        given: [8, 7, 6, 5, 4, 3, 2, 1],
        expects: 0
      },
      {
        given: [8, 4, 3, 10, 7, 3, 2, 6],
        expects: 16
      },
      {
        given: [2, 1, 2, 1, 2],
        expects: 2
      },
      {
        given: [4, 3, 1, 2, 4, 1, 2, 1, 3, 1],
        expects: 11
      },
      {
        given: [4,1,3,1,2,1,2,1],
        expects: 4
      } 
    ];
    var result;
    for (var test of tests) {
      result = func(test.given);
      if (result === test.expects) {
        console.log("------------------------------------");
        console.log("SUCCESS", test.given);
        console.log("------------------------------------");
      } else {
        console.log("------------------------------------");
        console.log("FAILURE", test.given);
        console.log("Expected: ", test.expects);
        console.log("Returned: ", result);
        console.log("------------------------------------");
      }
    }
}

testRainTerrace(rainTerraces);