roman_numeral_to_arabic = {
    "M": 1000,
    "CMXLIV": 944,
    "D": 500,
    "C": 100,
    "L": 50,
    "XLIV":44,
    "XIV": 14,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}

def to_roman(num):
    output = ""
    for letter in roman_numeral_to_arabic.keys():
        count = int(num / roman_numeral_to_arabic[letter])
        if count >= 1:
            output += count * letter
            num -= count * roman_numeral_to_arabic[letter]
    return output