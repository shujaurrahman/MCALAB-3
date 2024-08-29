print("\nWrite a program to accept a string from the user and display characters that are present at even index numbers.\n")

def print_even_index_char(str):
    '''print char at even index of string'''

    for i in range(len(str)):
        if i%2==0:
            print(str[i],end=" ")
    print()

Str=input("Enter the string: ")
print_even_index_char(Str)