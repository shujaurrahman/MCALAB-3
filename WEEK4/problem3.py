print("\n Given a list of numbers, write a program to turn every item of the list into its square.\n")

def list_sqaured(list):
    '''returns squared list'''
    new_list=[]
    for i in list:
        n=i**2
        new_list.append(n)
    return new_list

n=int(input("Length of the list [n]: "))
list=[]

i=0
while True:
    num=int(input("Enter element of the list : ")) 
    list.append(num)
    i+=1
    if i==n:
        break

result=list_sqaured(list)
print("Squared list is : ",*result)

