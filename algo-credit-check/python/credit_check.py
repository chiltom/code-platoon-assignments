def sum_string_list(list):
    sum = 0
    for elem in list:
        sum += int(elem)
    return sum

def sum_number_list(list):
    sum = 0
    for elem in list:
        sum += elem
    return sum

def credit_check(string):
    num_list = [*string]
    for index, string in enumerate(num_list):
        num_list[index] = int(string)
    counter = 0
    while counter < len(num_list):
        num_list[counter] *= 2
        if num_list[counter] > 9:
            new_list = [*str(num_list[counter])]
            num_list[counter] = sum_string_list(new_list)
        counter += 2
    print(num_list)
    total = sum_number_list(num_list)
    if total % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"