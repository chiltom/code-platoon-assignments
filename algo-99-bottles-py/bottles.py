def bottle_song(num):
    for x in range(num, 0, -1):
        print_string(x)
    print(
        f"No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {num} bottles of beer on the wall.")


def print_string(num):
    bottle_word = ""
    if num > 1 or num == 0:
        bottle_word = "bottles"
    else:
        bottle_word = "bottle"
    if num >= 2:
        print(f"{num} {bottle_word} of beer on the wall, {num} {bottle_word} of beer. Take one down and pass it around, {num - 1} {bottle_word} of beer on the wall.")
    elif num == 1:
        print(f"{num} {bottle_word} of beer on the wall, {num} {bottle_word} of beer. Take one down and pass it around, no more bottles of beer on the wall.")


bottle_song(5)