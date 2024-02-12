def linear_search(value_to_find, array_to_search_through):
    
    index = 0
    
    for elem in array_to_search_through:
        if (elem == value_to_find):
            return index
        index += 1
    
    return None
    
def linear_search_global(value_to_find, array_to_search_through):
    
    index_list = []
    index = 0
    
    for elem in array_to_search_through:
        if (elem == value_to_find):
            index_list.append(index)
        index += 1
    
    if not index_list:
        return None
    else:
        return index_list
