print("\nWrite a program to create a function cal_sum_sub() that can accept two variables and calculate\n")

def calculation(n1,n2):
    '''returns tuple of sum and sub'''
    sum=n1+n2
    sub=n1-n2

    return sum,sub

num1=int(input("Enter first number: "))
num2=int(input("Enter Second number: "))

sum,sub=calculation(num1,num2)

print(f"sum and subtraction of numbers {num1} and {num2} are {sum} and {sub} respectively. ")