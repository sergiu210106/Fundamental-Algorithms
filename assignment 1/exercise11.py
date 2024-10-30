def prime(x : int):
    '''
    function for verifying if x is prime

    :param x: int
    :return: void
    '''
    if x < 2:
        return 0
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return 0
    return 1

def primepref(n : int):
    '''
    function for generating all numbers of n digits that have all their prefixes prime numbers

    :param n: int
    :return: list
    '''
    
    if n == 1:
        return [2,3,5,7]
    else:
        result = []
        for num in primepref(n-1):
            for digit in range(10):
                if prime(num * 10 + digit) == 1:
                    result.append(num * 10 + digit)
        return result
    

if __name__ == '__main__':
    n = int(input('n = '))
    print(*primepref(n), sep = ', ')
