def split_list(original_list):
    original_list.sort()

    midpoint=len(original_list) // 2

    list1=original_list[:midpoint]
    list2=original_list[midpoint:]

    return list1, list2

input_list=list(map(int, input("Enter an even number of distinct integers (separated by spaces) : ").split()))

if len(input_list) % 2 !=0:
    print("Try again, number of elements is not even.")

else:
    list1, list2 = split_list(input_list)
    print("First List (SMALLER ELEMENTS) : ", list1)
    print("Second List (LARGER ELEMENTS) : ", list2)