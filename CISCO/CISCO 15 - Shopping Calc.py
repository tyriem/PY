### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Shop Calc
### VER: 1.5
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that monitors a user’s shopping trip and calculates how much they spent
# Get the program to ask for the firstItem bought so that the computer can remember this
# Develop the program to ask for and remember the costofthefirstItem bought, what the secondItem bought was, and the costofthesecondItem.
# Develop the program further so that it calculates the total cost of the items bought and then displays what was bought and the total amount spent.
### OBJECTIVE ###

# Print the program title
print('''
######################
###       Shop     ###
###   Calculator   ###
######################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs & DEFs

## Declare/Input VALs & STRINGs ##

#COUNTERs
itemCount = 1
total = 0

#LISTs
groceryList = []
groceryPriceList = []
groceryPriceVatList = []


#WHILE LOOP TO MOVE THROUGH ITEM ADDITIONS
while itemCount < 999:
    #INPUT: TYPE OF ITEM
    typeItem = input("Name of Item # " + str(itemCount) + ": ")
    #ADD TYPE OF ITEM TO LIST "typeItem"
    groceryList.append(typeItem)
    #INPUT: QUANTITY OF ITEM
    quantity = int(input("Item # " + str(itemCount) + " Quantity = "))
    #INPUT: RAW PRICE OF ITEM
    rawPrice = input("Item #" + str(itemCount) + " Price = ")
    #DATA-VAL: PRICE WITHOUT CASHINO SYMBOL ($)
    price = float(rawPrice.strip("$"))

    #CALC: TOTAL PRICE OF ITEM(S)
    total = (total + (quantity * price))
    #VAT PERCENTAGE (12.5%)
    vat_AB = float(0.125)
    #CALC: VAT ON ITEM
    vat = total * vat_AB
    #CALC: FINAL PRICE WITH VAT
    final = total + vat
    #ADD TYPE OF ITEM TO LIST "typeItem"
    groceryPriceVatList.append(final)

### OUTPUTs ###
    print (str("[Receipt]"))
    #TALLY
    print (str("ITEM #" + str(itemCount) + " Price:"))
    print ("$" + str(quantity * price))
    groceryPriceList.append(quantity * price)
    #SPACER
    print ("---------------------")

    #BEFORE VAT
    print (str("Cart Price Before VAT: "))
    print (str(" $ ") + str(total))

    #SPACER
    print ("---------------------")
    
    #VAT
    print (str("Cart VAT: "))
    print (str(" $ ") + str(vat))

    #SPACER
    print ("---------------------")
    
    #AFTER VAT
    print (str("Cart Price With VAT: "))
    print (str(" $ ") + str(final))

    #COUNTERs
    itemCount = itemCount + 1

    #SPACER
    print ("---------------------")
    # GROCERY LIST
    #Prints the amount of items in the list
    print("You now have " + str(len(groceryList)) + " item(s) in your cart.")
    #Prints the lists
    print("You have the following item(s) in your cart: " + str(groceryList))
    print("Their price before VAT is/are: " + str(groceryPriceList))
    print("Their price after VAT is/are: " + str(groceryPriceVatList))
    print ("---------------------")
    print ("---------------------")
