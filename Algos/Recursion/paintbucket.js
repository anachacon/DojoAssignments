function floodFill(canvas2D, startXY, newColor){

    //Set coordinates
    var coorX = startXY[0];
    var coorY = startXY[1];

    //Get max length and max height of Canvas2D for comparisons
    var maxHeight = canvas2D.length - 1;
    var maxLen = canvas2D[0].length -1 ;

    //Base case
    if (coorX > maxHeight || coorY > maxLen){
        return null;
    }

    //Save original color to temp and change value
    var startColor = canvas2D[coorX][coorY];
    canvas2D[coorX][coorY] = newColor;

    //Check left, right, top, and bottom adjacent and call function if equal

    var newCoor = [0,0];
    var leftAdj = coorY - 1;
    var rightAdj = coorY + 1;
    var top = coorX - 1;
    var bottom = coorX + 1;

    if (leftAdj >= 0){
        if(canvas2D[coorX][leftAdj] == startColor){
            newCoor = [coorX, leftAdj];
            canvas2D = floodFill(canvas2D, newCoor, newColor);
        }
    }

    if (rightAdj <= maxLen){
        if(canvas2D[coorX][rightAdj] == startColor){
            newCoor = [coorX, rightAdj];
            canvas2D = floodFill(canvas2D, newCoor, newColor);
        }
    }

    if (top >= 0){
        if(canvas2D[top][coorY] == startColor){
            newCoor = [top, coorY];
            canvas2D = floodFill(canvas2D, newCoor, newColor);
        }
    }

    if (bottom <= maxHeight){
        if(canvas2D[bottom][coorY] == startColor){
            newCoor = [bottom, coorY];
            canvas2D = floodFill(canvas2D, newCoor, newColor);
        }
    }

    return canvas2D;
}

var canvas2D = [[ 2, 3, 3, 4, 0], 
                [ 7, 3, 3, 5, 3], 
                [ 6, 5, 3, 4, 1], 
                [ 1, 2, 3, 3, 3]];
 
var startXY = [2,2];
var newColor = 1;

console.log(floodFill(canvas2D, startXY, newColor));