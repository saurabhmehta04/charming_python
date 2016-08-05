"""

Print the fibonacci sequence => 0 1 1 2 3 5 8 13

0 1 1 2 3 5 8 13
1 2 3 4 5 6 7

"""

"""Generate the fibo sum """
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# print(fibo(6))


"""Generate the """
def fiboSequence(n):
    # a, b = 0, 1
    # print(a)
    # print(b)

    i = 0
    while i < n:
        # temp = a + b
        # print(temp)
        # b, a = temp, b
        print(fibo(i))
        i += 1

fiboSequence(6)
# print(range(6))