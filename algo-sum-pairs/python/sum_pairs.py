def sum_pairs(num_list, sum_value):
    output_list = []
    for value in num_list:
        for next_values in num_list:
            if (value + next_values == sum_value and value <= next_values):
                output_list.append([value, next_values])
    if len(output_list) == 0:
        return "unable to find pairs"
    elif len(output_list) == 1:
        return output_list[0]
    else:
        return output_list
        
        
        
        
        
print(sum_pairs([1, 2, 3, 4, 5], 7))