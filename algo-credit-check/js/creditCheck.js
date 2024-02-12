function sumStringArr(arr) {
    let sum = 0;
    for (let elem of arr) {
        sum += Number(elem)
    }
    return sum;
}

function sumNumArr(arr) {
    let sum = 0;
    for (let elem of arr) {
        sum += elem
    }
    return sum;
}

function creditCheck(str) {
    const numArr = str.split("");
    for (let i = 0; i < numArr.length; i++) {
        numArr[i] = Number(numArr[i]);
    }
    for (let i = 0; i < numArr.length; i += 2) {
        numArr[i] *= 2;
        if (numArr[i] > 9) {
            const newArr = numArr[i].toString().split("");
            numArr[i] = sumStringArr(newArr);
        }
    }
    const total = sumNumArr(numArr);
    if (total % 10 === 0) {
        return "The number is valid!";
    } else {
        return "The number is invalid!";
    }
}

module.exports = creditCheck;