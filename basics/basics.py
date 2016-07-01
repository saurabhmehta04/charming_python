# Python 3 refresher


def main():
    print("Demo")


def stringPermutation(string):
    string = string.replace(" ", "")
    reverse = string[::-1]
    print(reverse == string)

if __name__ == '__main__':
    main()
    stringPermutation("nitin")
