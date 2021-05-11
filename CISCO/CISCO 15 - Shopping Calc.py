### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Shop Calc
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that monitors a user’s shopping trip and calculates how much the spent
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
itemCount = 1
total = 0

while itemCount < 999:
    quantity = int(input("Item # " + str(itemCount) + " Quantity = "))
    price = float(input("Item #" + str(itemCount) + " Price = "))
    total = (total + (quantity * price))
    vat_AB = float(0.125)
    vat = total * vat_AB
    final = total + vat
    print (str("[Receipt]"))
    #TALLY
    print (str("ITEM #" + str(itemCount) + " Price:"))
    print ("$" + str(quantity * price))

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
    print ("---------------------")
    print ("---------------------")
