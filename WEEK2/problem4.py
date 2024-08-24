print("\nWrite a program to use a loop to find the factorial of a given number.\n")

def factorial(num):
    '''returns factorial of a number'''
    if num<0:
        return -1
    if num==0 or num==1:
        return 1
    
    fact=1
    for i in range(1,num+1):
        fact*=i
    
    return fact

num=int(input("Enter the number to find its factorial: "))
print(f"The factorial of the number {num} is {factorial(num)}")