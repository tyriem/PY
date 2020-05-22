### AUTHOR: TMRM   
### PROJECT: Customer CALCULATION
### VER: 1.0
### DATE: 05-18-2020

### Vat Calculation
quantity_A = int(input("Item #1 Quantity = "))
price_A = float(input("Item #1 Price = "))
quantity_B = int(input("Item #2 Quantity = "))
price_B = float(input("Item #2 Price = "))
total = ((quantity_A * price_A) + (quantity_B * price_B))
vat_AB = float(input("VAT = "))
vat = total * vat_AB
final = total + vat
print (str("[Receipt]"))
#TALLY
print (str("ITEM 1"))
print (quantity_A * price_A)
print (str("ITEM 2"))
print (quantity_B * price_B)

#SPACER
print ("---------------------")

#BEFORE VAT
print (str("Cart Price Before VAT"))
print (str(" $ ") + str(total))
#VAT
print (str("Cart VAT"))
print (str(" $ ") + str(vat))
#AFTER VAT
print (str("Cart Price With VAT"))
print (str(" $ ") + str(final))
