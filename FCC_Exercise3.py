def main():
    hour = input("Enter Hours : ")
    rate = input("Enter Rate $ ")
    #Float
    fhour = float(hour)
    frate = float(rate)

    if fhour > 40:
        print("Overtime")
        regular_pay = fhour *frate
        overtime_pay = (fhour - 40) * (fhour*0.5)
        #print(regular_pay, overtime_pay)
        pay = regular_pay + overtime_pay
    else:
        print("Regular")
        pay = fhour*frate
        
    print("Pay : $",pay)
if __name__ == "__main__":
    main()  
        