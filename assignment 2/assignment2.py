
undo_stack = []
modified = False

# feature 1

def add(my_list: list[int], value: int) -> list[int]:
    '''
    function that adds a number at the end of the list

    :param my_list: list
    :param value: int

    :return: list
    '''
    my_list.append(value)
    return my_list

def insert(my_list : list[int], index : int, value : int):
    '''
    function for inserting a value at a specified index in a list
    :param my_list:
    :param index:
    :param value:
    :return: list
    '''

    my_list.insert(index, value)
    return my_list

# feature 2
def remove(my_list : list[int], index : int) -> list[int]:
    '''
    function that removes the value at the specified index in my_list
    :param my_list:
    :param index:
    :return: list
    '''

    del my_list[index]
    return my_list

def remove_from_to(my_list: list[int], from_index : int, to_index : int):
    '''
    function that removes elements in a list between two indices
    :param my_list:
    :param from_index:
    :param to_index:
    :return: list
    '''
    my_list = my_list[:from_index] + my_list[to_index+1:]
    return my_list

def replace(my_list : list[int], old_value : list[int], new_value : list[int]):
    '''
    function that replaces all occurrences of old_value with new_value
    :param my_list: list
    :param old_value: list
    :param new_value: list
    :return: list
    '''
    i = 0
    while i <= len(my_list) - len(old_value):
        # Check if the sublist at the current position matches old_value
        if my_list[i:i+len(old_value)] == old_value:
            # Replace the sublist with new_value
            my_list[i:i+len(old_value)] = new_value
            # Move the index forward by the length of new_value
            i += len(new_value)
        else:
            i += 1
    return my_list
# feature 3
def isPrime(x : int):
    '''
    function that verifies the primality of x
    :param x: int
    :return: bool
    '''

    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5 + 1), 2):
        if x % i == 0:
            return False
    return True

def prime(my_list : list[int], from_index : int, to_index : int):
    '''
    function that returns a list of all prime numbers between two indices
    :param my_list: list
    :param from_index: int
    :param to_index: int
    :return: list
    '''

    primes = []
    # iterate from from_index to to_index

    for i in range(from_index, to_index + 1):
        # check if prime
        if isPrime(my_list[i]) == True:
            primes.append(my_list[i])
    return primes

def odd(my_list: list[int], from_index : int, to_index : int):
    '''
    function that returns a list of all odd numbers between two indices
    :param my_list: list
    :param from_index: int
    :param to_index: int
    :return: list
    '''

    odds = []
    for i in range(from_index, to_index + 1):
        if my_list[i] % 2 == 1:
            odds.append(my_list[i])

    return odds


# feature 4
def sum_to_from(my_list:list[int], from_index : int, to_index:int) -> int:
    '''
    function that returns the sum between two given indices
    :param my_list: list[int]
    :param from_index: int
    :param to_index: int
    :return: int
    '''

    return sum([my_list[i] for i in range(from_index, to_index + 1)])

def gcd_2(a : int, b : int):
    '''
    function that returns the greatest common divisor of two numbers
    :param a: int
    :param b: int
    :return: int
    '''
    while (b != 0):
        r = a % b
        a, b = b, r
    return a

def gcd(my_list:list[int], from_index: int, to_index:int):
    '''
    function that returns the greatest common divisor of the elements between two indices
    :param my_list: list[int]
    :param from_index: int
    :param to_index: int
    :return: int
    '''
    d = my_list[from_index]

    for i in range(from_index + 1, to_index + 1):
        d = gcd_2(d, my_list[i])

    return d

def max_to_from(my_list: list[int], from_index: int, to_index: int):
    '''
    function that returns the maximum of the elements between two indices
    :param my_list: list[int]
    :param from_index: int
    :param to_index: int
    :return: int
    '''

    return max([my_list[i] for i in range(from_index, to_index + 1)])

# feature 5

def filter_primes(my_list):
    '''
    function that returns a list of the primes in my_list
    :param my_list: list
    :return: list
    '''

    return [i for i in my_list if isPrime(i)]

def filter_negative(my_list):
    '''
    function that returns a list of the negative numbers in my_list
    :param my_list: list
    :return: list
    '''

    return [i for i in my_list if i < 0]

# feature 6

def undo(my_list):
    '''
    function that undoes the last operation
    :param my_list: list
    :return: list
    '''
    if not undo_stack.empty():
        return undo_stack.top()
        undo_stack.pop()
    return my_list

# checks for errors or invalid inputs
def isValid(index, my_list):
    '''
    function for verifying if an index is in the list
    :param index: int
    :param my_list: list
    :return: bool
    '''
    return index in range(len(my_list))

# main() + ui

if __name__ == '__main__':
    option = 0
    my_list = [26, 8, 47, 44, 36, 2, 34, 95, 50, 76]
    while True:
        # creating menu
        print("Current list :", my_list)
        print("Choose an option from the following:")
        print("1. Add a value to the list")
        print("2. Insert a value at a specified index in the list")
        print("3. Remove a value from a specified index in the list")
        print("4. Remove elements between two indices in the list")
        print("5. Replace all occurrences of a subarray with another subarray")
        print("6. Return a list of all prime numbers between two indices")
        print("7. Return a list of all odd numbers between two indices")
        print("8. Return the sum of the numbers between two indices")
        print("9. Return the greatest common divisor of numbers between two indices")
        print("10. Remove all composite numbers from the list")
        print("11. Remove all positive numbers from the list")
        print("12. Undo last operation")
        print("13. Stop")

        if modified == True:
            undo_stack.append(my_list[:])

        modified = False

        try:
            option = int(input("You should enter a number between 1 and 13 : "))

            if option in range(1, 14):
                # valid option -> we consider all cases

                match option:
                    case 1:
                        try:
                            value = int(input("Provide a value that should be added to the list : "))

                            my_list = add(my_list, value)

                        except ValueError:
                            print("Invalid Value")

                    case 2:
                        try:
                            value = int(input("Provide a value that should be inserted : "))
                            index = int(input("Provide an index where the value should be inserted at : "))

                            if isValid(index, my_list):
                                my_list = insert(my_list, index, value)
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 3:
                        try:
                            index = int(input("Provide an index you want removed from the list : "))

                            if isValid(index, my_list):
                                my_list = remove(my_list, index)
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 4:
                        try:
                            from_index = int(input("Provide from_index : "))
                            to_index = int(input("Provide to_index : "))

                            if isValid(from_index, my_list) and isValid(to_index, my_list) and from_index <= to_index:
                                my_list = remove_from_to(my_list,from_index,to_index)
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 5:
                        try:
                            old_value_string = input("Provide a subarray that you want to replace (integers separated by spaces) : ").split()

                            old_value = []

                            for i in old_value_string:
                                old_value.append(int(i))

                            new_value_string = input("Provide the replacement subarray : ").split()

                            new_value = []

                            for i in new_value_string:
                                new_value.append(int(i))

                            my_list = replace(my_list, old_value, new_value)

                        except ValueError:
                            print("Invalid Value")

                    case 6:
                        try:
                            from_index = int(input("Provide from_index : "))
                            to_index = int(input("Provide to_index : "))

                            if isValid(from_index, my_list) and isValid(to_index, my_list) and from_index <= to_index:
                                print(prime(my_list,from_index,to_index))
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 7:
                        try:
                            from_index = int(input("Provide from_index : "))
                            to_index = int(input("Provide to_index : "))

                            if isValid(from_index, my_list) and isValid(to_index, my_list) and from_index <= to_index:
                                print(odd(my_list,from_index,to_index))
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")
                    case 8:
                        try:
                            from_index = int(input("Provide from_index : "))
                            to_index = int(input("Provide to_index : "))

                            if isValid(from_index, my_list) and isValid(to_index, my_list) and from_index <= to_index:
                                print(sum_to_from(my_list,from_index,to_index))
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 9:
                        try:
                            from_index = int(input("Provide from_index : "))
                            to_index = int(input("Provide to_index : "))

                            if isValid(from_index, my_list) and isValid(to_index, my_list) and from_index <= to_index:
                                print(gcd(my_list,from_index,to_index))
                            else:
                                print("Invalid Value")

                        except ValueError:
                            print("Invalid Value")

                    case 10:
                        my_list = filter_primes(my_list)

                    case 11:
                        my_list = filter_negative(my_list)

                    case 12:
                        if len(undo_stack) > 1:
                            undo_stack.pop()
                            my_list = undo_stack[-1]

                    case 13:
                        break

                if option in [1,2,3,4,5,10,11]:
                    modified = True


            else:
                print("Invalid Option")

        except ValueError:
            print("Invalid Option")



