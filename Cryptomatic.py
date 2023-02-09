#Author:Dakota Pruett 
#Date:2/8/2023
#For a class

def encrypt(plainList, keyPair, encryptList):
    """
    Only accepts Binary text
    @plainList This is the binary text to be encrypted
    @keyPair This is the binary key values in a list
    @encryptList This is the list you wish for the output to be added to
    """
    keyIndex = 0
    for num in plainList:
        encryptList.append(XORnum(int(num), keyPair[keyIndex]))
        if keyIndex==0: keyIndex=1
        else: keyIndex=0
    return 0

def decrypt():
    return 0

def toBinary(inputChar):
    return (bin(ord(inputChar))[2:])

def toList(inputString, outputList):
    for symbol in inputString:
        outputList.append(symbol)

def toString(list):
    out = ""
    for i in list:
        out += str(i)
    return out

def XOR (a,b):
    if a==0 and b==0: return 0
    if a==1 and b==0: return 1
    if a==0 and b==1: return 1
    if a==1 and b==1: return 0
    
def XORnum (a,b):
    """Shut up

    Args:
        a (int): Binary Value
        b (int): Binary Key value

    Returns:
        _type_: _description_
    """
    outList = []
    for i in range(len(str(a))):
        outList.append(XOR(int(str(a)[i]), int(str(b)[i])))
    return outList

def encryptionOption():
    fileName = input("What is the name of the file you want to encrypt:")
    plaintxtFile = open(fileName, "r")
    key = input("What is your key(Two letters):")
    biKey= []
    biKey.append(toBinary(key[0]))
    biKey.append(toBinary(key[1]))
    #Formatting for processing
    for line in plaintxtFile:
        for achar in line:
            plainChars.append(achar)
    #Conversion to binary text
    plainBinaryText = []
    for achar in plainChars:
        plainBinaryText.append(toBinary(achar))
    #Conversion to encrypted text
    encryptList = []
    encrypt(plainBinaryText, biKey, encryptList)
    #Output File writing
    outputFile = open("OutFile.txt", "a")
    for i in encryptList:
        outputFile.write(toString(i))
    print("Thank you for using Cryptomatic")

def decryptionOption():
    fileName = input("What is the name of the file you want to decrypt:")
    encryptedTxtFile = open(fileName, "r")
    key = input("What is your key(Two letters):")
    biKey= []
    biKey.append(toBinary(key[0]))
    biKey.append(toBinary(key[1]))
    encryptedBinary = []
    for line in encryptedTxtFile:
        toList(line, encryptedBinary)
    
    

def bruteForceOption():
    return 0 
        
#========================Start of logic=======================

def main():
    print("=============================================================")
    print("===============Welcome to Cryptomatic========================")
    print("1. Enter a file to decrypt using a given key. \n 2. Enter a file to decrypt using a given key. \n Enter a file to decrypt using a brute force method.")
    choice = input("What would you like to to do:")
    print("\n\n")
        
    if choice==1: encryptionOption()
    if choice==2: decryptionOption()
    if choice==3: bruteForceOption()
    else: main()