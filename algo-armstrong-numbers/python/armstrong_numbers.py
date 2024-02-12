# How can you make this more scalable and reusable later?
def find_armstrong_numbers(num_list):
    output = []
    for num in num_list:
        strList = [*str(num)]
        value = 0
        for elem in strList:
            value += int(elem) ** len(strList)
        if num == value:
            output.append(num)
    return output