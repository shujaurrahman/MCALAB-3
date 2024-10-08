def calcSum(number):
    if 1000<=number<=9999:
        num=str(number)

        firstTwo=int(num[:2])
        lastTwo=int(num[2:])

        squareFirst=firstTwo ** 2
        squareLast=lastTwo ** 2

        result=squareFirst+squareLast

        print(f"The sum of squares of {firstTwo} and {lastTwo} is {result}")

    else:
        print("Enter a 4 digit number")

number=int(input("Enter a 4 digit number : "))

print()

calcSum(number)