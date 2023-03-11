
fileh= open("mbox-short.txt") 
for linex in fileh:
    liney = linex.rstrip()
    print(liney.upper())