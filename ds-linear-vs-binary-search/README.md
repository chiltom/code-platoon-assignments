# Assignment: Linear vs Binary Search

## Instructions:

**Scenario 1: Finding a Number in an Unsorted List**

You are given an unsorted list of integers. Write two functions, one for linear search and one for binary search, to find a specific target number in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer.

```python
# Linear Search
def linear_search_unsorted(arr, target):
    # Your code here
    pass

# Binary Search
def binary_search_unsorted(arr, target):
    # Your code here
    pass

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")
```

**Scenario 2: Finding a Word in a Sorted List**

You have a sorted list of words. Write two functions, one for linear search and one for binary search, to find a specific word in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer.

```python
# Linear Search
def linear_search_sorted_words(word_list, target_word):
    # Your code here
    pass

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    # Your code here
    pass

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")
```

**Scenario 3: Finding the Last Occurrence in a List**

Given a list of integers, write two functions, one for linear search and one for binary search, to find the last occurrence of a specific number in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer.

```python
# Linear Search
def linear_search_last_occurrence(arr, target):
    # Your code here
    pass

# Binary Search
def binary_search_last_occurrence(arr, target):
    # Your code here
    pass

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
```

## Evaluation Criteria:

- Correct implementation of linear and binary search algorithms for each scenario.
- The functions should return both the answer and the number of steps taken.
- Clarity and readability of the code. (DRY SRP)
- Proper documentation and comments.

**Note:** Analyze and discuss the efficiency of linear search and binary search based on the number of steps in each scenario.
