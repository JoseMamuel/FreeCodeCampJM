number = 0
total = 0.0
while True:
    value = input("Enter a number : ")
    if value == "END" :
        break
    try :
        fvalue = float(value)
    except :
        print("Invalid Input")
        continue

    number = number + 1
    total = total + fvalue

print(total ,"-" ,number, "--" ,total/number)     
