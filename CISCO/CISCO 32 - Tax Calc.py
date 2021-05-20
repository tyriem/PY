### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Tax Calc
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Your task is to write a tax calculator.
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full dollars. There's a function named round() which will do the rounding for you -
# you'll find it in the skeleton code in the editor.
# Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero).
# Take this into consideration during your calculations.
### OBJECTIVE ###


#####################
###     CODE      ###
#####################

### DEPRECATED ###
#floatIncome = float(input("What was your income in thalers, citizen?"))
#if  floatIncome < 3088.8:
#    print("On your income of: " + str(floatIncome) + ". The tax is: 0 thalers.")
#elif  floatIncome < 85528:
#    floatRawTax = ((floatIncome * 0.18) - 556.02)
#    floatTax = round(floatRawTax, 1)
#    print("On your income of: " + str(floatIncome) + ". The tax is: " + str(floatTax) + " thalers.")
#else:
#    floatRawTax = (14839.02 + (0.32 * (floatIncome - 85528)))
#    floatTax = round(floatRawTax, 0)
#    print("On your income of: " + str(floatIncome) + ". The tax is: " + str(floatTax) + " thalers.")
### DEPRECATED ###

# ACCEPT USER INPUT AS FLOAT
floatIncome = float(input("What was your income in thalers, citizen?"))
# IF-ELSE STATEMENT TO EVALUATE INCOME VERSUS TAX BRACKET
if  floatIncome < 85528:
    floatRawTax = ((floatIncome * 0.18) - 556.02)
    floatTax = round(floatRawTax, 1)
# NESTED IF-ELSE STATEMENT TO EVALUATE TAX BURDEN FOR LOWER TAX BRACKET
    if floatTax < 0:
        print("On your income of: " + str(floatIncome) + ". The tax is: 0 thalers.")
    else:
        print("On your income of: " + str(floatIncome) + ". The tax is: " + str(floatTax) + " thalers.")
# ELSE STATEMENT TO EVALUATE TAX BURDEN FOR HIGHER TAX BRACKET
else:
    floatRawTax = (14839.02 + (0.32 * (floatIncome - 85528)))
    floatTax = round(floatRawTax, 0)
    print("On your income of: " + str(floatIncome) + ". The tax is: " + str(floatTax) + " thalers.")




