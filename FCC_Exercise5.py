def computepay(hours, rates):
    #print("In Computepay", hours, rates)
    if fhour > 40:
        regular_pay = fhour *frate
        overtime_pay = (fhour - 40) * (fhour*0.5)
        pay = regular_pay + overtime_pay
    else:
        pay = fhour*frate
    return pay    
      
hour = input("Enter Hours : ")
rate = input("Enter Rate $ ")
try :
    fhour = float(hour)
    frate = float(rate)
except :
    print("Error, please enter numeric input") 
    quit()
        
pay = computepay(hour, rate)   
        
print("Pay : $",pay)
