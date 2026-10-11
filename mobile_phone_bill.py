# Daniel E Salazar Gomez
# CMP 131-86250
#Week 06
#Lab 01 
#Assigment 6
#10/01/2026
print("----------------")
print("Mobile Phone Service")
print("----------------")
print("Package A: For a monthly charge of : $39.99 it will include 450 minutes per month and for any additional minutes $0.45 per minute")
print("Package B: For a monthly charge of $59.99 it will include 900 minutes per month and for any additional minutes $0.40 per minute")
print("Package C: For a monthly charge of $69.99 per month unlimted minutes")
package=input("Enter your package (A,B, or C): ")
if package== "A":
    minutes= int(input("Enter number of minutes used: "))
    bill= 39.99
    if minutes > 450:
        extra_minutes=minutes - 450
        extra_charge = extra_minutes * 0.45
        bill = bill + extra_charge

    print("Additional minutes: ", extra_minutes)
    print("Additional minute charge $", format(extra_charge, ".2f"))
    print("Your monthly bill is $", format(bill, ".2f"))
elif package == "B":
    minutes=int(input("Enter the number of minutes used: "))
    bill = 59.99
    if minutes > 900:
        extra_minutes = minutes - 900
        extra_charge = extra_minutes * 0.40
        bill = bill + extra_charge
    print("Additional minutes: ", extra_minutes)
    print("Additional minute charge $", format(extra_charge, ".2f"))
    print ("Your monthly bill is $", format(bill, ".2f"))
elif package == "C":
    minutes= int(input("Enter number of minutes used: "))
    bill = 69.99
    print("Your month bill is $", format(bill, ".2f"))
else:
    minutes= int(input("Enter number of minutes used: "))
    print ("Invalid package selected.")


    