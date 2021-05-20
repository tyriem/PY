### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Let's Divide
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Ask the user for 2 numbers then divide the first number by thesecond number.
# Display the answer. To divide numbers use
#
### OBJECTIVE ###

##Declare CALLs & DEFs ###

# Print the program title
print('''
#########################
###     DIVISION      ###
###    CALCULATOR     ###
#########################
''')

### Declare/Input VALs & STRINGs ###

# Accept User Input
numNumer = float(input("PLEASE ENTER THE FIRST VALUE FOR DIVISION (Numerator): "))
numDenom = float(input("PLEASE ENTER THE SECOND VALUE FOR DIVISION (Denominator): "))


### CALCs ###
#NB: / -> Floating Point Division | // -> Floor Division
numProduct = (numNumer / numDenom)

### OUTPUTs ###
print("----------------------------------------------------")
print("Thank You.")
print("You have entered " + str(numNumer) + " as your numerator.")
print("You have entered " + str(numDenom) + " as your denominator.")
print("The product of  " + str(numNumer) + " / " + str(numDenom) + " equals: " + str(numProduct))
