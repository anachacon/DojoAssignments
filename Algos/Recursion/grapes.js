function gotAnyGrapes(bags, index=0, include=0, exclude=0) {
    // Base Case: if we've reached the end of the array
    if(index === bags.length){
        // return the larger of the two sums
        return exclude <= include ? include : exclude;
    }

    // compute value of exclude before include computation to ensure we do not miss an index
    let newSum = exclude <= include ? include : exclude;

    // include is the sum that includes the current index
    // exclude is the larger of the two sums before adding current value
    include = exclude + bags[index];
    exclude = newSum;

    return gotAnyGrapes(bags, index+1, include, exclude);
}


console.log (gotAnyGrapes([2,10,10,2,2,5]));