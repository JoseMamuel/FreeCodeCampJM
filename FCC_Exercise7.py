str = "X-OSPAN-Confidence: 0.8475"

iposition = str.find("i")
#print(iposition)
piece = str[iposition+8:]
#print(piece)
#print(piece+42.0) #eill fait
value = float(piece)
print(value)
#print(value+42.0)
