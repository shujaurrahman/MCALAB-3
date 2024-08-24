print("\nWrite a program to extract each digit from an integer in reverse order.")

def reverse_digit(number):
    '''return reverse of number'''
    temp=number
    while temp>0:
        r=temp%10
        # we get digit r as last digit and that has to be printed 
        print(r)
        temp=temp//10

num=int(input("Enter number to reverse: "))
print(f"Reverse of the number {num} is ")
reverse_digit(num)
        