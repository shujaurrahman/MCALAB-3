print("\nWrite a program to print the following pattern using a for loop:\n")

for i in range(5,0,-1):
    count=0
    for j in range(i,0,-1):
        if count%2==0:
            print("*",end=' ')
        else:
            print(j,end=' ')
        count=count+1
    print()