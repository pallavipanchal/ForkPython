def inPutCat():
    a = input()  ## input in a single line()
    s, i, f = a.split(' ')  ## split the a into three parts: string, integer, and f.
    print(
        s + " " + str(int(i) + float(f)))  ##type cast i to int, f to float. Add i with f. Typecast the result to string


def main():
    testcases = int((input()))  # testcases
    while (testcases > 0):
        inPutCat()
        testcases -= 1


if __name__ == "__main__":
    main()
