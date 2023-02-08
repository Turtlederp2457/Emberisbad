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
        encryptList.append(XORnum(plainList[num], keyPair[keyIndex]))
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
    return "working"

def XOR (a,b):
    if a==0 and b==0: return 0
    if a==1 and b==0: return 1
    if a==0 and b==1: return 1
    if a==1 and b==1: return 0
    
def XORnum (a,b):
    outList = []
    for i in a:
        outList.append(XOR(a[i], b[i]))
    return outList
        
#========================Start of logic=======================
plaintxtFile = open("Lincoln.txt", "r")
key = "MU"
plainChars = []
for line in plaintxtFile:
    for achar in line:
        plainChars.append(achar)

