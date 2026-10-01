# Daniel E Salazar Gomez
# CMP 131-86250
#Week 06
#Lab 01 
#Assigment 6
#10/01/2026
Software= int(input("How many software units were purchased?"))
if Software > 0:
    print("Quatity purchased: " , Software)
else:
    print("ERROR")
Original_Cost = Software * 99
print("Cost: ${:.2f}". format(Original_Cost))
if Software >= 10 and Software <=19:
    discount_20= (Original_Cost * 0.20) 
    saved= Original_Cost - discount_20
    twenty_off = Original_Cost-saved
    print("Saved: ${:.2f}".format(twenty_off))
    saved= Original_Cost - discount_20
    print("Final Cost: ${:.2f}". format(saved))
elif Software >= 20 and Software <= 49:
    discount_30= Original_Cost * 0.30
    saved= Original_Cost - discount_30
    thirty_off= Original_Cost-saved
    print("Saved: ${:.2f}".format(thirty_off))
    saved= Original_Cost - discount_30
    print("Final Cost: ${:.2f}". format(saved))
elif Software >= 50 and Software<= 99:
    discount_40= Original_Cost * 0.40
    saved= Original_Cost - discount_40
    forty_off=Original_Cost - saved
    print("Saved: ${:.2f}".format(forty_off))
    saved= Original_Cost - discount_40
    print("Final Cost: ${:.2f}". format(saved))
elif Software >= 100:
    discount_50 = Original_Cost * 0.50
    saved= Original_Cost - discount_50
    fifty_off= Original_Cost - saved
    print("Saved: ${:.2f}".format(fifty_off))
    saved= Original_Cost - discount_50
    print("Final Cost: ${:.2f}". format(saved))
else:
    print("Final Cost: ${:.2f}".format(Original_Cost))
    print("Saved: $0.00")

if Software >= 10 and Software <=19:
    print("Discount: 20%")
elif Software >= 20 and Software <= 49:
    print("Discount: 30%")
elif Software >= 50 and Software<= 99:
    print("Discount: 40% ")
elif Software >= 100:
    print("Discount: 50%")
else:
    print("No discount")
                





