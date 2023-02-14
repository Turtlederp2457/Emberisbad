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

def encrypt(key, fileName):
    """Takes a key and a file name and XOR encrypts them returning a string representing the encrypted text

    Args:
        key (List): List of the form ["",""] where each entry represents a part of the key
        fileName (String): name of the file you wish to be encrypted

    Returns:
        String: encrypted string
    """
    plainTxtFile = open(fileName, "r")
    #converting key and file to binary
    biKey = []
    for a in key:
        biKey.append(charToBinary(a))
    biPlainTxtList = []
    for line in plainTxtFile:
        for i in line:
            biPlainTxtList.append(charToBinary(i))
    plainTxtFile.close()
    
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
    outString = ""
    for i in encryptedTxtList:
        outString += i
    return outString
        

#========================Start of logic=======================

def main():
    print("=============================================================")
    print("===============Welcome to Cryptomatic========================")
    print("1. Enter a file to encrypt using a given key. \n2. Enter a file to decrypt using a given key. \n3. Enter a file to decrypt using a brute force method.")
    choice = input("What would you like to to do:")
    choice = int(choice)
    print("\n")
        
    if choice==1:
        #Getting information for encryption
        fileName = input("What is the name of the file you want to encrypt:")
        key = input("What is your key(Two letters):")
        #key validation
        if len(key) != 2: 
            print("Error your key is incompatible.")
            main()
        #File Encryption
        encryptedString = encrypt(key, fileName)
        outFile = open("outFile.txt", "a")
        outFile.write(encryptedString)
            
    elif choice==2: 
        #Getting information for decryption
        fileName = input("What is the name of the file you want to decrypt:")
        key = input("What is your key(Two letters):")
        if len(key) != 2: 
            print("Error your key is incompatible.")
            main()
        #File decryption 
        decryptedString = encrypt(key, fileName)
        outFile = open("outFile.txt", "a")
        outFile.write(decryptedString)
        outFile.close()
    
    elif choice==3:
        #Load Infomation
        possibleKeys = []
        for i in string.printable:
            for n in string.printable:
                possibleKeys.append([i,n])
        words = []
        wordFile = open("wordList.txt", "r")
        for word in wordFile:
            if word == "a":
                words.append(" a ")
            words.append(word.strip())
        #Getting information for decryption
        fileName = input("What is the name of the file you want to decrypt:")
        #decryption determining key value on a short list
        bestKeys = []
        for key in possibleKeys:
            bigCount = 0
            possibleString = encrypt(key, fileName)
            lPossibleString = possibleString.lower()
            for word in words:
                count = lPossibleString.count(word)
                bigCount += count
            bestKeys.append([bigCount,key])
        #Finds the highest scored Key
        max = 0
        for i in bestKeys:
            if i[0] > max: 
                max = i[0]
                bestKey = i[1]
                #prints out each max just in case the answer is close but not exact Often capitalization issues
                print(i)
        #output of key information
        print("The key is " + bestKey[0] + bestKey[1])
        outString = encrypt(bestKey, fileName)
        outFile = open("outFile.txt", "a")
        outFile.write(outString)
        print("Finsihed. Your text was written to outFile.txt")
    else: main()
    
main()