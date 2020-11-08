def friends_in_trouble(a_angry, b_angry):
    if a_angry != b_angry:
        return False
    else:
        return True


def main():
    testcases = int(input())

    while testcases:
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if string1 == 'True':
            string1 = True
        else:
            string1 = False

        if string2 == 'True':
            string2 = True
        else:
            string2 = False

        print(friends_in_trouble(string1, string2))
    testcases -= 1


if __name__ == "__main__":
    main()
