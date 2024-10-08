def find(inputString):
    uCount=0
    lCount=0
    aCount=0
    dCount=0

    for char in inputString:
        if char.isupper():
            uCount+=1
        if char.islower():
            lCount+=1
        if char.isalpha():
            aCount+=1
        if char.isdigit():
            dCount+=1

    return uCount,lCount,aCount,dCount

inputString=input("Enter a string : ")

uCount,lCount,aCount,dCount=find(inputString)

print()

print(f"Number of uppercase characters : {uCount}")
print(f"Number of lowercase characters : {lCount}")
print(f"Number of alphabets : {aCount}")
print(f"Number of digits : {dCount}")