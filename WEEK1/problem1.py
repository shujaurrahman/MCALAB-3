

print("\nWrite a program to find the product of two user-supplied integers and if \nthe product is equal to or lower than 5000, return the sum of the two numbers.\n")
print()
num1=int(input("First Number: "))
print()
num2=int(input("Second Number: "))

result=num1*num2
def sum_and_product():
    if result<=5000:
        print(f"The sum of two numbers are {num1+num2}")
    else:
        print(f"Product is : {result}")
        is_sum=False

sum_and_product()