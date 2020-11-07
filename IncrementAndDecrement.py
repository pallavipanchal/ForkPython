def do_operation(x, y):
    # Your code here
    x -= 1
    y += 1
    print(x)
    print(y)


def main():
    testcases = int((input()))  # testcases
    while (testcases > 0):
        input1 = input().split()
        x = int(input1[0])
        y = int(input1[1])
        do_operation(x, y)
        testcases -= 1


if __name__ == "__main__":
    main()
