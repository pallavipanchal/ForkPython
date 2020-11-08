# Function to check value and
# return accordingly
def check_status(a, b, status):
    ##Your code here
    if status == True:
        if a < 0 and b < 0:
            return True;
        else:
            return False
    else:
        if ((a > 0 and b < 0) or (a < 0 and b > 0)):
            return True
        else:
            return False


def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while testcases:
        a = int(input())
        b = int(input())
        flag = input()

        if flag == "True":
            flag = True
        else:
            flag = False

        if (check_status(a, b, flag) is True):
            print("True")
        else:
            print("False")

    testcases -= 1


if __name__ == "__main__":
    main()
