print("\nWrite a program to remove characters from a string starting from position \nn to the end  and return a new string. Example: remove_chars(\"aligarh\", 3) should return ali.\n")

def remove_char(str,n):
    '''remove char starting from n till end'''
    return str[:n]

str=input("Enter the string: ") 
n=int(input("Enter the starting index char of the string : "))
result=remove_char(str,n)

print(f"Original string: {str}")
print(f"String after removing char from strating index {n} till end is : {result} ")