print("\nWrite a program to print characters from a string which are present at even index numbers.\n")

def print_even_index_char(str):
    '''print char at even index of string'''

    for i in range(len(str)):
        if i%2==0:
            print(str[i],end=" ")
    print()

Str=input("Enter the string: ")
print_even_index_char(Str)