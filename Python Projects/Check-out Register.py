#MSBA 502: Analytics Programming I
#Homework 1: Submitted Friday, Sept. 16, 2022
#Written by Kevin A. Howard


#This program handles the checkout process for The Citadel's Giftshop.  
#The program starts with a welcome message and asks the customer for their first name,
#which is used in subsequent prompts.
print("Welcome to the Citadel's Gift Shop!")
print("We offer Plumbuses, Meeseeks Boxes, and Portal Fluid.")
print("We also have bulk discount pricing available!")
print()

name = input(str("Let's start by entering your first name: "))
print()
print("Thanks,", name+".", "Let's get started with your order!")
print()

#The proceeding two 'if statements' ask if the customer wants Plumbuses or not and if yes,
#the calculation factors in a different discount price depending on the integer entered, then adds it to 'Total'. 
#Caluculating Plumbuses note: x = 0 initializes the customers shopping basket so that 'Total' will accumulate subtotals.
Plumbuses = input("Would you like to buy any Plumbuses? (yes/no): ")
plumbuses_quantity = 0
Total = 0
print()

if Plumbuses == "yes" or Plumbuses == "YES" or Plumbuses == "Yes":
    plumbuses_quantity = int(input("How many Plumbuses would you like? It's available as whole individual units. : "))
elif Plumbuses == "no" or Plumbuses == "NO" or Plumbuses == "No":
    print()
    print("Okay", name+",", "no Plumbuses.")
else:
    print()
    print("Oops, Looks like a typo. We'll treat this as a no.")

if plumbuses_quantity < 5:
    Total = 20.00*plumbuses_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()
elif plumbuses_quantity >= 5 and plumbuses_quantity < 15:
    Total = 17.50*plumbuses_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()
else:
    Total = 15.25*plumbuses_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()

#The proceeding two 'if statements' ask if the customer wants Meeseeks Boxes or not and if yes,
#it factors in a different discount price depending on the integer entered, then adds it to 'Total'.
#Caluculating Meekseeks Boxes note: mb = 0 initializes the customers shopping basket so that Total will accumulate subtotals.
Meeseeks_Boxes = input("Would you like to buy any Meeseeks Boxes? (yes/no): ")
mb_quantity = 0
print()

if Meeseeks_Boxes == "yes" or Meeseeks_Boxes == "YES" or Meeseeks_Boxes == "Yes":
    mb_quantity = int(input("How many Meeseeks Boxes would you like? It's available as whole boxes. : "))
elif Meeseeks_Boxes == "no" or Meeseeks_Boxes == "NO" or Meeseeks_Boxes == "No":
    print()
    print("Okay", name+",", "no Meeseeks Boxes.")
else:
    print()
    print("Oops, Looks like a typo. We'll treat this as a no.")

if mb_quantity < 10:
    Total += 1.75*mb_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()
elif mb_quantity >= 10 and mb_quantity < 18:
    Total += 1.50*mb_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()
else:
    Total += 1.25*mb_quantity
    print()
    print("Your subtotal is: ")
    print("$", Total)
    print()

#The proceeding two 'if statements' ask if the customer wants Portal Fluid or not and if yes,
#it factors in a different discount price depending on the integer entered, then adds it to 'Total'.  
#Caluculating Portal Fluid note: pf = 0 initializes the customers shopping basket so that Total will accumulate subtotals.
Portal_Fluid = input("Would you like to buy any gallons of Portal Fluid? (yes/no): ")
pf_quantity = 0
print()

if Portal_Fluid == "yes" or Portal_Fluid == "YES" or Portal_Fluid == "Yes":
    pf_quantity = float(input("How many gallons of Portal Fluid would you like? You can buy whole and partial gallons. : "))
    print()
elif Portal_Fluid == "no" or Portal_Fluid == "YES" or Portal_Fluid == "Yes":
    print()
    print("Okay", name+",", "no Portal Fluid.")
    print()
else:
    print()
    print("Oops, look like a typo. We'll treat that as a no.")
    print()

if pf_quantity < 3:
    Total += 8.00*pf_quantity  
elif pf_quantity >= 3 and pf_quantity < 7:
    Total += 7.00*pf_quantity
else:
    Total += 6.00*pf_quantity

#This final print block adds up the customer's total rounded to 2 decimals
#and presents a final thank you for shopping message.
print()
print("THANK YOU for shopping at the Citadel's Gift Shop,", name+"!")
print("Your final total today is","$", str(round(Total, 2)))
print()
print("We appreciate your patronage and look forward to seeing you again soon!")
