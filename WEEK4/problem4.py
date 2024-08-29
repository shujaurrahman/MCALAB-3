print("\nGiven two Python lists, write a program to iterate through both lists \nsimultaneously and display items from the first list in the original order and items from the second list in reverse order.\n")

def iterate_lists(list1,list2):
    rev_list2=list2[::-1]
    for i,j in zip(list1,rev_list2):
        print(f"from list1 {i} , from list2 {j}")
    

list1=input("Enter the first list (comma-sep values): ").split(',')
list2=input("Enter the first list (comma-sep values): ").split(',')

list1=[item.strip() for item in list1]
list2=[item.strip() for item in list2]


print("Display items from the first list in original order and items from the second list in reverse order: ")
iterate_lists(list1,list2)

    