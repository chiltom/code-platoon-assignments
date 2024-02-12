def factorial(num):

    product = 1

    for x in range(num, 0, -1):
        product *= x

    return product
