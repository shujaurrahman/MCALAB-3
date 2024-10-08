phoneDictionary={}

phoneDictionary['Saud']='7770099911'
phoneDictionary['shuja']='1222333344'
phoneDictionary['azam']='44444444444'

name=input("Enter a name to get the phone number : ")

print()

if name in phoneDictionary:
    print(f"The phone number of {name} is {phoneDictionary[name]}")

else :
    print(f"The data for {name} is not available")