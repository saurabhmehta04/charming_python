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


if __name__ == '__main__':
    main()
