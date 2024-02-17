def flatten_list(lst, counter = 0):
    # Create my_list to append nums to
    my_list = []
    
    # Start loop over input list
    while counter < len(lst):
        # If element at index is an int, append it to the output list and increment counter
        if isinstance(lst[counter], int):
            my_list.append(lst[counter])
            counter += 1
        # If element at index is another list, recursively call flatten_list to return a sublist to the current index
        else:
            sublist = flatten_list(lst[counter])
            # Reset output list by adding sublist to it and increment counter
            my_list = my_list + sublist
            counter += 1
    
    return my_list
    
    
    
    
    
print(flatten_list([1, [2], [3, [4, 5, [6]]], 7]))