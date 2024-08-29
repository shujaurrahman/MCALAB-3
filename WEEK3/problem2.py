print("\nWrite a program to print the following pattern using a for loop:\n")

def number_pattern():
    '''return number pattern '''
    for i in range(1,6,1):
        count=1
        for j in range(1,i+1,1):
            print(j,end=" ")
        print()
    for i in range(4,0,-1):
        for j in range(1,i+1,1):
            print(j,end=" ")
        print()

def star_pattern():
    '''returns star pattern'''
    for i in range(6):
        count=1
        for j in range(i):
            if count==5:
                print("#",end=' ')
            else:
                print("*",end=' ')
            count=count+1
        print()
    for i in range(4,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

n=int(input("Enter 1 for star pattern and any number for number pattern : "))
if n==1:
    star_pattern()
else:
    number_pattern()

print()