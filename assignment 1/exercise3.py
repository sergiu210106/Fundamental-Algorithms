def ex3(n : int, k : int):
    '''
    function for showing all powers of n less than k
    :param n: int
    :param k: int
    :return:
    '''
    p = 1 # initialize product
    result = [] # initialize result list

    while p < k:
        result.append(p) # add to result list
        p = p * n # go to the next element

    print(*result, sep = ', ') #print elements of the result list with separators
        

if __name__ == "__main__":
    n = int(input("n = "))
    k = int(input("k = "))

    ex3(n, k)
