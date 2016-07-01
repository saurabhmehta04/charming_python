# Python 3 refresher


def main():
    print("Demo")


def stringPermutationWithFunctions(string):
    string = string.replace(" ", "")
    reverse = string[::-1]
    print(reverse == string)


def stringPermutationWithoutFunctions(string):
    stringStrippedSpaces = string.replace(" ", "")
    for i, char in enumerate(stringStrippedSpaces):
        if char != stringStrippedSpaces[-i - 1]:
            return False
    return True

if __name__ == '__main__':
    main()
    stringPermutationWithFunctions("nitin")
    stringPermutationWithoutFunctions("nitin")
