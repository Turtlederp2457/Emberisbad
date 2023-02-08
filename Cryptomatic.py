plaintxtFile = open("/home/dakota/Documents/Ember_is_bad/Lincoln.txt", "r")
charList = []

for line in plaintxtFile:
    for char in line:
        charList.append(char)
    
for character in charList:
    print(bin(ord(character))[2:])

key = "MU"

