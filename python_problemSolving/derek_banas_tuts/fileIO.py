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
    print("All done ")
fiboSequence(6)
# print(range(6))



""" Read one line at a time using files """


def readOneLine(line):
    # function that prints the desired output from each line

    arrOfWords = line.split()
    arrLength = len(arrOfWords)

    wordLength = []
    for char in arrOfWords:
        wordLength.append(len(char))

    sum = 0
    for num in wordLength:
        sum += num

    print("Number of words are : {}\nAvg length of words is : {:.1f}".format(arrLength,
                                                                             sum / arrLength))


with open("mydata.txt") as myFile:
    lineNumber = 0
    while True:
        line = myFile.readline()

        if not line:
            break

        lineNumber += 1
        print("Line : {}".format(lineNumber))
        readOneLine(line)
