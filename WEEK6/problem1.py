def concatinate_tuple(t1,t2):
    '''return concatinated 2 tuples in a single tuple'''
    t=t1+t2
    return t

input1=input("Enter element of tuple separated by comma: ")
input2=input("Enter element of tuple separated by comma: ")

e1=input1.split(",")
e1=[x.strip() for x in e1]

tuple1=tuple(e1)

e2=input2.split(",")
e2=[x.strip() for x in e2]

tuple2=tuple(e2)


result=concatinate_tuple(tuple1,tuple2)

print(f"The concatinated tuple is", result)