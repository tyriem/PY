### AUTHOR: TMRM   
### PROJECT: Performing Calculations
### VER: 1.0
### DATE: X-X-2020



###Declare CALLs



###Declare VARSs/STRINGs
a = 15
b = 3


###OUTPUT
print(a+b)
print(a-b)
print(a*b)
print(b**2)
#Print float with decimal point
print(a/b)
#Print only the whole number
print(a//b)
#Print with no remainder
print(a%b)

#Python uses the BOMDAS/PEMDAS Method
print(a+b/3-4*12)
#This will yield -32 as it goes in this order: Brackets -> Division -> Multiplication -> Addition -> Subtraction
print(8/2*3)



### Client with a budget of $15 wants to buy as much buns as possible at $1.20 and will only accept whole units
varBun = float(1.20)
varBudget = float(15)
print (str("AMOUNT OF BUNS CLIENT CAN BUY"))
print (int(varBudget/varBun))



### Calculate this value in a BOMDAS calculation
x = 45
y = 15
z = 3
print (str("BOMDAS CALCULATION ="))
print(x-y+y/z)



### Vat Calculation
quantityA = 12
quantityB = 45
quantityC = 3
priceA = 30.50
priceB = 21.50
priceC = 3.50
total = (quantityA * priceA) + (quantityB * priceB) + (quantityC * priceC)
vat = total*0.125
final = total + vat
print (str("_Receipt_"))
#TALLY
print (str("ITEM 1"))
print (quantityA * priceA)
print (str("ITEM 2"))
print (quantityB * priceB)
print (str("ITEM 3"))
print (quantityC * priceC)
#BEFORE VAT
print (str("Price Before VAT"))
print (total)
#VAT
print (str("VAT"))
print (vat)
#AFTER VAT
print (str("Price With VAT"))
print (final)








