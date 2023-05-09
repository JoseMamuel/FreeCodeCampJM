file_name = input("Enter File : ")
if len(file_name) < 1 : 
    file_name = "clown.txt"
hand = open(file_name)

dic = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        dic[w] = dic.get(w,0) + 1
print(dic)

tmp = list()
for k,v in dic.items():
    newt = (v,k)
    tmp.append(newt)
    
print("Flipped", tmp)

tmp = sorted(tmp, reverse=True)
print("Sorted", tmp[:5])

for v,k in tmp[:5] :
    print(k,v)
    