__author__ = 'Falcon'
# using python 3.5
import re


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

    d = {'k1': [1, 2, 3]}
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
    print()
    l.append(6)
    print(l)


    #   lambda, map(), reduce(), filter()

    #   function are implemented as objects..check dir(function_name)
    def caller(f):
        f()

    def hello():
        print("Hello World")

    caller(hello)

    #     why function within functions, sorted, map, reduce, filter
    print(sorted([1, 4, 2]))
    print(sorted([1, -1, 0]))
    # if we need to customize this using absolute value
    print(abs(-2))
    print("Sorting using high order functions: ", sorted([1, -2, 0], key=abs))

    print(sorted(['foo', 'bar']))

    #     maps
    #     on the left hand side: we have a,b,c and takes in a function to make it x,y,z on the right hand side
    map(str, [1, 2, 3])  # returns ['1', '2', '3']

    #     perfect example of map()
    def add_2(x):
        return x*2

    a = map(add_2, [1, 2, 3, 4, 5, 6])
    print(*a)

    count = 0
    l = ['a', 'b', 'c']
    for item in l:
        print(count, end=" ")
        print(item)
        count += 1

#     using enumerate
    for count, item in enumerate(l):
        print(count, " ", item)

#     decorators
    def func():
        return 1

    print(func())

    s = "This is a global variable"

    def func1():
        print(locals())

    print(globals().keys())

#     function can be assigned to a variable
    func2 = func

#     decorators
    def hello(name = "jose"):
        print("The hello() function has been executed")

        def greet():
            return '\t this is inside the greet() function'

        def welcome():
            return '\t This is inside the welcome() function'

        if name == "jose":
            return greet
        else:
            return welcome

        # print(greet())  ... unreachable code from here
        # print(welcome())
        # print("Now we are back inside the hello() function")

    hello()
    print('calling welcome')
#     greet() and welcome() are not visible here due to scoping

#     designing decorator
    def new_decorator(func):
        def wrap_func():
            print("Code here, before executing the func")
            func()
            print("Code here will execute after the func")
        return wrap_func()

    # option1: passing a func to the decorator
    # def func_needs_decorator():
    #     print("This function needs decorator")
    #
    # func_needs_decorator = new_decorator(func_needs_decorator)
    # print("\nDecorator: ", func_needs_decorator, '\n')

    # option2: using "@"
    print("********** DECORATOR **********")

    @new_decorator
    def func_needs_decorator():
        print('Using @: This function needs a decorator')

    test = 10

    @new_decorator
    def decorator_func():
        test = 20
        print("New Decorator function")
    print(test)

#     regular expressions
    patterns = ['term1', 'term2']

    str1 = 'This is test string, term1 is the culprit'

    for pattern in patterns:
        if re.search(pattern, str1):
            print("Found ")
        else:
            print("Not found")

    patt = 'term1'
    str2 = 'this is term1 a string'
    match = re.search(patt, str2)
    print(type(match))


if __name__ == '__main__':
    main()
