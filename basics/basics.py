__author__ = 'Falcon'
# using python 3.5


def main():
    print("Hello World")
    print(3/2)  # prints 1.5
    print(2**3)  # prints 2^3 which is 8
    print(2 ^ 2, end=" ")  # don't want line break after this print ... outputs 0
    print(2 + 10 * 10 + 3)  # performs multiplication and then addition left to right
    a = 5  # variable 5
    b = a  # creates a "copy" with same id and value
    print(a)  # 5
    print(id(a))  # 4297538016
    a = 10
    print(id(b))  # 4297538016
    print(b)  # 5
    print(a)  # 10

    '''
        Strings
        can have single and double quotes
    '''
    print("using single inside 'double'")
    # print('"using single inside 'double"') error...
    s = "Hello World"
    print(s[1:3])  # starts from index 0, everything from 1 till 3-1 ... outputs el

#     python dictionaries
    my_dict = {'key1': 10, 'key2': 'value2'}
    print(my_dict)
    print(my_dict['key1'].__class__)

#     creating a new empty dictionary
    d = {}
    print(d)
    d['animal'] = 'Dog'
    print(d)

    ex = {'key1': {'key2': {'key3': 'value1'}}}
    print(ex)
    print(ex['key1']['key2']['key3'])  # getting the value1
    print(ex.keys(), ex.values())

#     returning tuples from the list
    print(my_dict.items())

    d = {'k1' : [1,2,3]}
    print(d['k1'].__class__)  # prints list
    print(d['k1'][0])  # prints 1

#     tuples
    t = (1, 2, 3, 3, 4, 5, 6)
    print(t.__class__)
    print(len(t))
    print(t[-1])  # prints the last value
    print("count :", t.count(3), " starting at index: ", t.index(3))

    a, b = 2, 3
    if a > b:
        a, b = 4, 5

    print(a, b)

#     loops
    l = [1, 2, 3, 4, 5]

    for num in l:
        if num % 2 != 0:    # checks for the odd numbers in the list
            print(num, end=" ")


if __name__ == '__main__':
    main()
