print("\nWrite a function to return True if the first and last number of a given list are the same. Otherwise, return False.\n")

def match_number(list):
    '''return true if first and last number of is equal ''' 
    if list[0]==list[-1]:
        return True
    

n=int(input("Length of the list [n]: "))
list=[]

i=0
while True:
    num=int(input("Enter element of the list : ")) 
    list.append(num)
    i+=1
    if i==n:
        break
    
print(*list)
if match_number(list):
    print(f"First and last number of the list  are same")
else:
    print(f"First and last number of the list  are not same")