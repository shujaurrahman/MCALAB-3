import random
import string

def generateRandomSymbol(length):
    symbol=string.punctuation
    return ''.join(random.choice(symbol) for _ in range(length))

def encryption(mainString):
    encryptedString=""

    for char in mainString:
        randomSymbol=generateRandomSymbol(2)
        encryptedString+=char+randomSymbol

    return encryptedString

def decryption(encryptedString):
    decryptedString = ""
    i=0
    while i<len(encryptedString):
        decryptedString+=encryptedString[i]
        i+=3

    return decryptedString

mainString=input("Enter the main string : ")

print()

encryptedString=encryption(mainString)
print("Encrypted String : ", encryptedString)

print()

decryptedString=decryption(encryptedString)
print("Decrypted String : ", decryptedString)