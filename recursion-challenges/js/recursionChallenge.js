function factorial(num) {
    if (num === 1) {
        return 1
    };
    return num * factorial(num - 1)
};

function palindrome(word, counter = 0) {
    if (counter === Math.floor(word.length / 2)) {
        return true
    };
    if (word[counter] === word[word.length - 1 - counter]) {
        return palindrome(word, counter+1)
    };
    return false
};

function bottles(num, counter = 0) {
    if (num === 1) {
        console.log(`${num} bottle of beer on the wall, ${num} bottle of beer. Take one down, pass it around, ${num - 1} bottles of beer on the wall.`);
        return bottles(num - 1, counter + 1)
    } else if (num === 0) {
        console.log(`No more bottles of beer on the wall, no more bottles of beer. Go to the store, buy some more, ${counter} bottles of beer on the wall.`);
        return null
    } else {
        console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. Take one down, pass it around, ${num - 1} bottles of beer on the wall.`);
        return bottles(num - 1, counter + 1)
    }
};

const order = [
    {'M': 1000},
    {'CM': 900},
    {'D': 500},
    {'CD': 400},
    {'C': 100},
    {'L': 50},
    {'XL': 40},
    {'X': 10},
    {'IX': 9},
    {'V': 5},
    {'IV': 4},
    {'I': 1},
];

function romanNum(num, romanNumeral = "", index = 0) {
    if (num === 0) {
        return romanNumeral
    };
    const key = Object.keys(order[index]);
    const value = Object.values(order[index]);
    if (num - value >= 0) {
        return romanNum(num - value, romanNumeral += key, index)
    } else if (num - value < 0) {
        return romanNum(num, romanNumeral, index + 1)
    }
    return romanNumeral
};

// console.log(factorial(5));
// console.log(palindrome('momo'));
// bottles(10);
// console.log(romanNum(944))