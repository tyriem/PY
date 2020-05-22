### AUTHOR: TMRM   
### PROJECT: VAT CALCULATION
### VER: 1.0
### DATE: 05-14-2020

### Vat Calculation
quantityA = 12
quantityB = 45
quantityC = 3
priceA = 30.00
priceB = 21.50
priceC = 3.25
total = (quantityA * priceA) + (quantityB * priceB) + (quantityC * priceC)
vat = total*0.125
final = total + vat
print (str("[Receipt]"))
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
