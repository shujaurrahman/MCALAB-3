print("\nWrite a program to check if the given number is a palindrome.\n")
print("12321 is a Palindrome number because after reversing its digits,\n the number becomes 12321 which is same as the original number.\n")

# approach reverse a number check if are equal if yes return true else false
def is_palindrome(num):
    '''Function to check if the number is palindrome or not. return True if yes else False'''
    temp=num
    rev=0

    while temp>0:
        r=temp%10  # get remiander by % (mod)
        rev=rev*10+r  #rev mul by 10 added with rem unit place shift to left 
        temp=temp//10   #divide temprary number  [// specififcally interger division python does float if not specified]

    return rev==num
    
num=int(input("Enter a number to check palindrome: "))
if is_palindrome(num):
   print(f"{num} is palindrome.")
else:
   print(f"{num} is not palindrome.")

