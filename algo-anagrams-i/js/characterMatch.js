exports.isCharacterMatch = function(string1, string2) {
    arr1 = string1.toLowerCase().replace(/\s/g, "").split("").sort();
    arr2 = string2.toLowerCase().replace(/\s/g, "").split("").sort();
    let longest = 0;
    if (arr1.length > arr2.length) {
        longest = arr1.length;
    } else {
        longest = arr2.length;
    }
    for (let i = 0; i < longest; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }
    return true;
};

exports.anagramsFor = function(word, listOfWords) {
    output = [];
    for (let wordTwo of listOfWords) {
        if (this.isCharacterMatch(word, wordTwo)) {
            output.push(wordTwo);
        }
    }
    return output;
};

