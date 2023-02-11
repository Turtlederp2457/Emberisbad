#Author:Dakota Pruett 
#Date:2/8/2023
#For a class
"""
To Do:
Load more into the information in the bruteforce decryption.

Encryption
    Read txt from a file and obtain a key from the user
    Convert txt to binary and key to binary both in list form
        put txt in a char by char list then convert each char to binary
    XOR the binary using the key binary
    Convert XORed binary back to text 
    Write txt to file
Decryption
Brute Force Decyption
    Load information
        all Binary key values
        Word lists 
    
"""

import string

def binaryToAscii(binary):
    decimal = int(binary, 2)
    return chr(decimal)

def charToBinary(a):
    return format(ord(a), "#010b")[2:]

def XOR (a,b):
    if a==0 and b==0: return 0
    if a==1 and b==0: return 1
    if a==0 and b==1: return 1
    if a==1 and b==1: return 0

def charXOR(char, key):
    """Takes 2 strings symbolizing binary and XOR encrypts them.

    Args:
        char (String): Text
        key (String): Key value

    Returns:
        String: XORed text 
    """
    out = ""
    for i in range(len(char)):
        out += str(XOR(int(char[i]),int(key[i])))
    return out
        

def encryptionOption():
    #Getting information for encryption
    fileName = input("What is the name of the file you want to encrypt:")
    plaintxtFile = open(fileName, "r")
    key = input("What is your key(Two letters):")
    if len(key) != 2: 
        print("Error your key is incompatible.")
        main()
        
    #converting to binary
    biKey = []
    for a in key:
        biKey.append(charToBinary(a))
    biPlainTxtList = []
    for line in plaintxtFile:
        for i in line:
            biPlainTxtList.append(charToBinary(i))
    print(biPlainTxtList)
    print(biKey[0])
    
    #XOR of binary
    biEncryptedTxtList = []
    keyIndex = 0
    for i in biPlainTxtList:
        biEncryptedTxtList.append(charXOR(i, biKey[keyIndex]))
        if keyIndex==0: keyIndex=1
        else: keyIndex=0
        
    #XORed binary to ascii
    encryptedTxtList = []
    for i in biEncryptedTxtList:
        encryptedTxtList.append(binaryToAscii(i))
    outFile = open("outFile.txt", "a")
    for i in encryptedTxtList:
        outFile.write(i)
        
        
def decryptionOption():
    #Getting information for decryption
    fileName = input("What is the name of the file you want to decrypt:")
    plaintxtFile = open(fileName, "r")
    key = input("What is your key(Two letters):")
    if len(key) != 2: 
        print("Error your key is incompatible.")
        main()
        
    #converting to binary
    biKey = []
    for a in key:
        biKey.append(charToBinary(a))
    biPlainTxtList = []
    for line in plaintxtFile:
        for i in line:
            biPlainTxtList.append(charToBinary(i))
            
    #XOR of binary
    biEncryptedTxtList = []
    keyIndex = 0
    for i in biPlainTxtList:
        biEncryptedTxtList.append(charXOR(i, biKey[keyIndex]))
        if keyIndex==0: keyIndex=1
        else: keyIndex=0
        
    #XORed binary to ascii
    encryptedTxtList = []
    for i in biEncryptedTxtList:
        encryptedTxtList.append(binaryToAscii(i))
    outFile = open("outFile.txt", "a")
    for i in encryptedTxtList:
        outFile.write(i)
    
def bruteForceOption():
    #Load Infomation
    possibleKeys = []
    for i in string.printable:
        for n in string.printable:
            possibleKeys.append([i,n])
    for i in possibleKeys:
        possibleKeys[i] = [charToBinary(possibleKeys[i,0]), charToBinary(possibleKeys[i,1])]
    
    #Getting information for decryption
    fileName = input("What is the name of the file you want to decrypt:")
    plaintxtFile = open(fileName, "r")
    #converting to binary
    biPlainTxtList = []
    for line in plaintxtFile:
        for i in line:
            biPlainTxtList.append(charToBinary(i))
    


#========================Start of logic=======================

def main():
    print("=============================================================")
    print("===============Welcome to Cryptomatic========================")
    print("1. Enter a file to encrypt using a given key. \n2. Enter a file to decrypt using a given key. \n3. Enter a file to decrypt using a brute force method.")
    choice = input("What would you like to to do:")
    choice = int(choice)
    print("\n\n")
        
    if choice==1: encryptionOption()
    if choice==2: decryptionOption()
    if choice==3: bruteForceOption()
    else: main()
    
    
main()