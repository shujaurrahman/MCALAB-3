print("\nWrite a program to iterate through a supplied list of 20 numbers \nand print only those numbers which are divisible by 5.\n")

def is_divisible(list):
    '''takes list as arg to check if items are divisible by 5 or not return list of all divisible items.'''
    arr=[]
    
    for n in list:
        if n%5==0:
            arr.append(n)

    return arr


numbers=[]
end=int(input("how many number will you enter : "))
for num in range(end):
    num=int(input(f"Enter number {num+1} : "))
    numbers.append(num)

result=is_divisible(numbers)
 

print()
for num in result:
    print(f"{num} is divisble. \n")
    