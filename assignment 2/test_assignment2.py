from assignment2 import add, insert, remove, remove_from_to, replace, prime, gcd, max_to_from, odd, sum_to_from, filter_primes, filter_negative
#1
def test_add():
    assert add([1,2,3], 4) == [1,2,3,4]
    assert add([], 0) == [0]
    assert add([2,4,1,7], 9) == [2,4,1,7,9]

def test_insert():

    assert insert([1, 2, 4], 2, 3) == [1, 2, 3, 4]
    assert insert([2, 3, 4], 0, 1) == [1, 2, 3, 4]
    assert insert([1, 2, 3], 3, 4) == [1, 2, 3, 4]

# 2
def test_remove():
    assert remove([1,2,3,4], 2) == [1, 2, 4]
    assert remove([101, 40, 12], 1) == [101, 12]
    assert remove([5,3,1,8,9,10], 4) == [5, 3, 1, 8, 10]

def test_remove_from_to():
    assert remove_from_to([1,2,3,4,5], 1, 4) == [1]
    assert remove_from_to([10, 20, 30, 40, 50], 0, 3) == [50]
    assert remove_from_to([100, 200, 300, 400], 2, 3) == [100, 200]


def test_replace():
    assert replace([1, 2, 3, 2, 4], [2], [9]) == [1, 9, 3, 9, 4]
    assert replace([1, 2, 2, 3, 4], [2, 2], [8]) == [1, 8, 3, 4]
    assert replace([1, 2, 3, 4], [2, 3], [7, 8]) == [1, 7, 8, 4]


#3
def test_prime():
    assert prime([1, 3, 5, 7, 10], 1, 3) == [3, 5, 7]
    assert prime([4, 6, 8, 9, 12], 0, 4) == []
    assert prime([2, 4, 5, 6, 7], 0, 4) == [2, 5, 7]

def test_odd():
    assert odd([1, 2, 3, 4, 5], 0, 4) == [1, 3, 5]
    assert odd([2, 4, 6, 8, 10], 0, 4) == []
    assert odd([2, 3, 4, 5, 6], 0, 4) == [3, 5]

def test_sum():
    assert sum_to_from([1, 2, 3, 4, 5], 1, 4) == 14
    assert sum_to_from([10, 20, 30], 1, 1) == 20
    assert sum_to_from([1, 2, 3, 4], 0, 3) == 10

#4
def test_gcd():
    assert gcd([8, 12, 16], 0, 2) == 4
    assert gcd([6, 9], 0, 1) == 3
    assert gcd([7], 0, 0) == 7

def test_max_to_from():
    assert max_to_from([1, 5, 3, 9, 2], 0, 4) == 9
    assert max_to_from([2, 3, 8, 1, 4], 1, 3) == 8
    assert max_to_from([5], 0, 0) == 5

# 5
def test_filter_primes():
    assert filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
    assert filter_primes([4, 6, 8, 10, 12]) == []
    assert filter_primes([17]) == [17]


def test_filter_negative():
    assert filter_negative([10, -3, 7, -1, 4, -6]) == [-3, -1, -6]
    assert filter_negative([5, 12, 7, 3]) == []
    assert filter_negative([-10]) == [-10]

if __name__ == '__main__':
    test_add()
    test_insert()
    test_prime()
    test_odd()
    test_sum()
    test_gcd()
    test_max_to_from()
    test_filter_primes()
    test_filter_negative()

