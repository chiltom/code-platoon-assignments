# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
    updated_string1 = string1.lower().replace(" ", "")
    updated_string2 = string2.lower().replace(" ", "")
    list1 = sorted([*updated_string1])
    list2 = sorted([*updated_string2])
    longest = 0
    if (len(list1) > len(list2)):
        longest = len(list1)
    else:
        longest = len(list2)
    for num in range(longest):
        if list1[num] != list2[num]:
            return False
    return True


# Part 2
def anagrams_for(word, list_of_words):
    output = []
    for wordTwo in list_of_words:
        if is_character_match(word, wordTwo):
            output.append(wordTwo)
    return output
