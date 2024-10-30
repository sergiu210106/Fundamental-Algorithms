def digit_product(x : int):
    '''
    function that returns the digit product of a number

    :param x: int
    :return: int
    '''
    result = 1
    copy = x

    while copy > 0:
        result = result * (copy % 10)
        copy //= 10

    return result
def start_number(n : int, k : int):
    '''
    function that returns the smallest number with n digits and the smallest number of n digits divisible by k

    :param n: int
    :param k: int
    :return: tuple
    '''
    p = 1
    while n > 1:
        n -= 1
        p *= 10

    if p % k == 0:
        return p, p
    else:
        return p, p / k * k + k

def ex19(n : int, k : int):
    '''
    function that prints all numbers with n digits that are divisible by k with the property that they are equal to
    k multiplied by their digit product
    :param n: int
    :param k: int
    :return: prints all numbers with the required property
    '''
    p, start = start_number(n, k)

    for i in range(start, p*10, k):
        if i == digit_product(i) * k:
            print(i, end = " ")

if __name__ == '__main__':
    n = int(input("n = "))
    k = int(input("k = "))
    ex19(n, k)