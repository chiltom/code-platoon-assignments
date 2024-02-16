def factorial(num) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)

def palindrome(word, counter = 0) -> bool:
    if counter == len(word) // 2:
        return True
    if word[counter] == word[len(word) - 1 - counter]:
        return palindrome(word, counter+1)
    return False

def bottles(num, counter = 0):
    if num == 1:
        print(f"{num} bottle of beer on the wall, {num} bottle of beer. Take one down, pass it around, {num - 1} bottles of beer on the wall.")
        return bottles(num - 1, counter + 1)
    elif num == 0:
        print(f"No more bottles of beer on the wall, no more bottles of beer. Go to the store, buy some more, {counter} bottles of beer on the wall.")
        return None
    else:
        print(f"{num} bottles of beer on the wall, {num} bottles of beer. Take one down, pass it around, {num - 1} bottles of beer on the wall.")
        return bottles(num - 1, counter + 1)
    
values = {
	'M': 1000,
	'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}

order = ['M', 'CM', 'D', 'CD', 'C', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def romanNum(num, roman_numeral = '', index = 0):
    if num == 0:
        return roman_numeral
    
    key = order[index]
    value = values[key]
    
    if num - value >= 0:
        return romanNum(num - value, roman_numeral + key, index)
    elif num - value < 0:
        return romanNum(num, roman_numeral, index + 1)
    
    return roman_numeral

# print(factorial(5))
# print(palindrome('racecar'))
# bottles(10)
# print(romanNum(944))