function sumPairs(numArr, sumValue) {
    outputArr = [];
    for (let i = 0; i < numArr.length; i++) {
        for (let y = i; y < numArr.length; y++) {
            if (numArr[i] + numArr[y] == sumValue) {
                outputArr.push([numArr[i], numArr[y]])
            }
        }
    }
    if (outputArr.length == 0) {
        return "unable to find pairs";
    } else if (outputArr.length == 1) {
        return outputArr[0];   
    }
    else {
        return outputArr;
    }
}

module.exports = sumPairs;