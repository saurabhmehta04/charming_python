class Line(object):
    def __init__(self, coor1, coor2):
        # both the arguments are tuple
        # self.coor1 = coor1
        # self.coor2 = coor2
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())


# map function to check for even numbers => returns a value
def map_demo(x, y):
    if x > y:
        return x
    else:
        return y


lst = [47, 12, 42, 3]

# since we'll return a single value, this would be done with reduce() function
# python3 recommends to use for loop for efficiency as compared to reduce()
# print(list(map((),lst))) # map function will take in the list and return the biggest in the list

# find the largest element in a list
from functools import reduce

# print(list(reduce(lambda x, y: x if x > y else y, lst)))

# using built-in funtion
print(max(lst))

# finding from enumeration
maximum = 0
for i, value in enumerate(lst):
    if value > maximum:
        maximum = value

print("Maximum is : {}".format(maximum))

# find the largest and get its index
print(max(lst))
print(lst.index(max(lst)))

# example of filter
# function to find all the even elements in a list

lst = [42, 12, 17, 21, 20, 43]


def even_num(num):
    if num % 2 == 0:
        return True


print(list(filter(even_num, lst)))

a = [1, 2, 3, 4, 5, 6]
b = [10, 20, 30, 40, 50]
print(list(zip(a, b)))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print("Zipped version is: {}".format(list(zip(d1, d2.items()))))
print("\nSwitcharoo")


def switcharoo(d1, d2):
    dout = {}
    for d1key, d2val in list(zip(d1, d2.items())):
        print("d1key = {}, d2val = {}".format(d1key, d2val))
        dout[d1key] = d2val

    return dout


print(switcharoo(d1, d2))


# Example of decorator
def new_decorator(func):
    # def wrapping_function():
    print("Code would be here, before executing the function")
    func()
    print("Code here will execute after the function")
    # return wrapping_function()


@new_decorator
def func_needs_decorator():
    print("I need decorator")


# Generator in python3
def genCubes(n):
    for num in range(n):
        yield num ** 3


print(list(genCubes(4)))


# example of generator: to calculate fibonacci series
def genfibon(n):
    '''
    Generate a fibonnaci sequence up to n
    '''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in genfibon(10):
    print(num, end=" ")

print()


# understanding generator's yield function
def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # error as all the elements in g have been yielded

print('\n')
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(s_iter)

# collections module

from collections import Counter

l = [1, 2, 3, 2, 2, 2, 2, 3, 4, 5, 6, 6, 6]
letters = Counter(l)
print(letters.most_common(2))

# python debugger
import pdb

x = [1, 2, 3]
y = 2
z = 3
result = y + z
print(result)

a1 = 10
a2 = 20


# practice of decorator
# decorator takes in function and returns a decoratored version of the function
def decorator_demo(func):
    print("*********** Decorating the function ***********")
    print(func(a1, a2))
    print("*********** End of decorator function ***********")


@decorator_demo
def func_needs_decorator_stuff(a, b):
    summation = a + b
    return summation


@decorator_demo
def some_func_with_decorator(a, b):
    print("Another func requiring decorator")


# understanding decorators implicitly

def dec_bar(some_func):
    def inner_func():
        ret = some_func()
        return ret + 1

    # call the inner function, execute it and return the result
    return inner_func()


@dec_bar
def foo():
    return 1

    # decorated = dec_bar(foo)
    # print(decorated)
