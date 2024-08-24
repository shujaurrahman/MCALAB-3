print("\nWrite a program to print the sum of the first 10 numbers.\n")

n=int(input("Sum of natural number till : "))

# Range doesn't take last therfore n+1
def sum(n):
    sum=0
    list=[]
    for num in range(n):
        list.append(num)
        sum+=num
    print("Sum of natural numbers ",{*list},f"is {sum}")

sum(n)
