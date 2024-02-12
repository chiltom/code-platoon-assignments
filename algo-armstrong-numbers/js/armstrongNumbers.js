// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(arr) {
    const output = [];
    for (let num of arr) {
        const strArr = String(num).split("");
        let value = 0
        for (let y = 0; y < strArr.length; y++) {
            value += Number(strArr[y]) ** strArr.length;
        }
        if (num === value) {
            output.push(num);
        }
    }
    return output;
};