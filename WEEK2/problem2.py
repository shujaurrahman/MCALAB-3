print("\n Write a program to count the total number of digits in a number using a while loop.\n")

def count_digit(num):
    '''returns the number of digit in a number'''

    temp=num
    i=0
    while temp>0:
        temp=temp//10
        i+=1
    
    return i

num=int(input("Enter a number : "))
print(f"The number of digit in number {num} are {count_digit(num)}")