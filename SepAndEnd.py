#Function using 'end' and 'sep' parameters to print desired output
# string1 = "Geeks"
# string2 = "For"
def print_func(string1, string2):
    print ( string1,string2,string1, sep = '$', end = '$')
# Use string1 & string2 with sep and end parameter to print desired output

def main():
    print_func(string1="Geeks",string2="For")

if __name__ == "__main__":
    main()