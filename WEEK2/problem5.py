print("\n Write a program to find the sum of digits of a supplied integer.\n")

def sum_digit(num):
    '''returns sum of digits of supplied interger'''
    temp=num
    sum=0
    while temp>0:
        r=temp%10
        sum+=r
        temp//=10
    return sum

num=int(input("Enter the number to get sum of its digit: "))
print(f"sum of the digit of number {num} is {sum_digit(num)}\n")


