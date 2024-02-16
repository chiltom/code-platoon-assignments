
def count_up(num: int, count: int = 0) -> None:
    print(count)
    if count == num:
        return None
    return count_up(num, count+1)

# count_up(10)

def count_down(num: int) -> None:
    print(num)
    if num == 0:
        return None
    return count_down(num-1)

# count_down(10)