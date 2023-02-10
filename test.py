def charToBinary(a):
    return format(ord(a), "#010b")[2:]


print(charToBinary("M"))