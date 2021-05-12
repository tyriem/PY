### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - MOBILE CALC
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Create a code for an app to do the following:
# Accept the user’s name and mobile phone network
# Ask for the number of minutes they have used this month and multiply that by 0.10 per minute
# Ask for the number of texts that they have sent in a month and multiple that by 0.05 pence per text
# Display a total bill amount for the month
#Display a new total including VAT of 20%
### OBJECTIVE ###

# Print the program title
print('''
######################
###     Mobile     ###
###   Calculator   ###
######################
''')

#####################
###     CODE      ###
#####################

##INPUT
stringUser = input("Please Enter Your Name: ")
stringNetworkRaw = input("Please Enter Your Mobile Provider's Name (Ex. BTC, Aliv):" )

stringNetworkLower = stringNetworkRaw.lower()
charNetwork = stringNetworkLower[0:1]

numMinutesMonth = float(input("PLEASE ENTER THE NUMBER OF VOICE MINUTES YOU HAVE USED THIS MONTH:"))
numTextsMonth = float(input("PLEASE ENTER THE NUMBER OF TEXTS YOU HAVE SENT THIS MONTH:"))


if charNetwork == "a" or charNetwork == "b"or charNetwork == "n":
    ##CALCs
    numValMinutes = (numMinutesMonth * 0.10)
    numValTexts = (numTextsMonth * 0.05)
    subtotal = (numValMinutes + numValMinutes)
    vat = 0.20

    numValMinutesVat = numValMinutes * vat
    numValTextsVat = numValTexts * vat

    numVatTotal = numValMinutesVat + numValTextsVat
    numValMinutesVatEnd = (numValMinutesVat + numValMinutes)
    numValTextsVatEnd = (numValTextsVat + numValTexts)

    total = (numValMinutesVatEnd + numValTextsVatEnd)

    annual = (total * 12)
    ##OUTPUT


    #SPACER
    print("---------------------")
    print("---------------------")
    #PRINT USER
    print("Thank you " + stringUser + ".")
    print("---------------------")
    #PRINT NETWORK
    print("As a(n) " + stringNetworkRaw + " user your monthly bill is as follows:")
    #PRINT COST: MINUTES
    print("MONTHLY VOICE COST: $" + str(numValMinutes))
    #PRINT COST: TEXTS
    print("MONTHLY TEXT COST: $" + str(numValTexts))
    #PRINT COST: SUBTOTAL
    print("YOUR SUB-TOTAL IS: $" + str(subtotal))
    print("---------------------")
    #PRINT COST: VAT RATE
    print("The Value Added Tax (VAT) applied to your billing is: 20%")
    #PRINT COST: MINUTES (AFTER VAT)
    print("MONTHLY VOICE COST (AFTER VAT): $" + str(numValMinutesVatEnd))
    #PRINT COST: TEXTS (AFTER VAT)
    print("MONTHLY TEXT COST (AFTER VAT): $" + str(numValTextsVatEnd))
    print("---------------------")
    #PRINT COST: VAT PRICE
    print("The Value Added Tax (VAT) applied to your billing comes to: $" + str(numVatTotal))
    print("---------------------")
    #PRINT COST: TOTAL
    print("YOUR FINAL MONTHLY TOTAL IS: $" + str(total))
    #SPACER
    print ("---------------------")
    #PRINT ESTIMATE: ANNUAL
    print("AT THIS USAGE LEVEL YOUR ESTIMATED ANNUAL BILL IS: $" + str(annual))
    print ("---------------------")
    
else:
    print ("WE DO NOT DETECT A VALID NETWORK PROVIDER")
