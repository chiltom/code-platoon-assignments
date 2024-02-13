""" 
Scenario 1: Finding a number in an unsorted list
Returns:
    list: returns list with index of target value and steps required to find target value
"""

# Linear search function to find a specific target number in a list
def linear_search_unsorted(lst, target) -> list:
    # Initialize variable to count steps
    steps = 0
    # Loop through list and compare for target
    for index, num in enumerate(lst):
        # Increment step counter
        steps += 1
        if num == target:
            return [index, steps]
    # Return -1 if target not found in list
    return -1

# Binary search function 
def binary_search_unsorted(lst, target) -> list:
    # Sort the list to ensure loop will not miscompare values in left and right limits
    sorted_list = sorted(lst)
    # Initialize variables to count steps and left and right limits by index
    steps = 0
    left = 0
    right = len(sorted_list) - 1
    # Loop through list for search
    while left <= right:
        # Increment step counter
        steps += 1
        middle = (left + right) // 2
        # Compare values and move left and right limits depending on middle indices place in list and value comparison
        if lst[middle] == target:
            return [middle, steps]
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    # If target not found, return -1
    return -1

# Scenario 1 test
# unsorted_list = [42, 15, 7, 30, 22, 10, 18]
# target_1 = 30
# result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
# result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
# print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
# print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")



"""
 Scenario 2: Finding a Word in a Sorted List
 Returns: 
    list: returns list with index of target value and steps required to find target value
"""

def linear_search_sorted_words(word_list, target_word) -> list:
    steps = 0
    for index, word in enumerate(word_list):
        steps += 1
        if word == target_word:
            return [index, steps]
    return -1

def binary_search_sorted_words(word_list, target_word) -> list:
    steps = 0
    left = 0
    right = len(word_list) - 1
    
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if word_list[middle] == target_word:
            return [middle, steps]
        elif word_list[middle] < target_word:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1

# Scenario 2 Test
# sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
# target_2 = 'orange'
# result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
# result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
# print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")



"""
Scenario 3: Finding the Last Occurrence in a List
Returns: 
    list: returns list with index of target value and steps required to find target value
"""

def linear_search_last_occurrence(lst, target) -> list:
    steps = 0
    last = -1
    for index, num in enumerate(lst):
        steps += 1
        if num == target:
            last = index
    
    return [last, steps]

def binary_search_last_occurrence(lst, target) -> list:
    steps = 0
    left = 0
    right = len(lst) - 1
    last = -1
    
    # TODO: Fix loop so it exits after the last finding of the number
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if lst[middle] == target:
            last = target
            left = middle
        elif lst[middle] > target:
            right = middle - 1
            if lst[right] == target:
                last = right
                return [last, steps]
        else:
            left = middle + 1
    
    return [last, steps]
    
# Scenario 3 Test
# occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
# target_3 = 10
# result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
# result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
# print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
# print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
# print(sorted(occurrence_list))