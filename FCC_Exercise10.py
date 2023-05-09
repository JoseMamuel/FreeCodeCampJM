file_name = input("Enter File : ")
if len(file_name) < 1 : 
    file_name = "clown.txt"
hand = open(file_name)

dic = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    for w in wds:
        #if w in dic:
        dic[w] = dic[w] + 1
        #else:
            #dic[w] = 1
            #print("--NEW--")
        #print(w,dic[w])
largest = -1
theword = None
for k,v in dic.items():
    if v > largest:
        largest = v
        theword = k
    
print("Done", theword, largest)