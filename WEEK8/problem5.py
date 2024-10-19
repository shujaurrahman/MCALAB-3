def separate_string(input_string):
    L1=[]
    L2=[]

    for char in input_string:
        if char.isalpha():
            L1.append(char)
        elif char.isdigit():
            L2.append(int(char))

    return L1,L2

input_string=input("Enter a string with alphabets and numbers : ")
L1,L2=separate_string(input_string)

print("List of alphabets : ", L1)
print("List of numbers : ", L2)