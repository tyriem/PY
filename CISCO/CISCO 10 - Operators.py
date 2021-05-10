### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Operators
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Alex has £10.
# Present from father: £20
# How much does he have now?
# Demonstrate this example using 3 variables and arithmetic operators.
#
### OBJECTIVE ###

##Declare CALLs & DEFs ###

# Print the program title
print('''
#########################
###     OPERATOR      ###
###    CALCULATOR     ###
#########################
''')

### Declare/Input VALs & STRINGs ###

numWallet = 10
numDeposit = 20

### CALCs ###
#NB: / -> Floating Point Division | // -> Floor Division
numBalance = (numWallet + numDeposit)

### OUTPUTs ###
print("----------------------------------------------------")
print("Alex had: £" + str(numWallet))
print("Alex receives a present from his father of: £" + str(numDeposit))
print("Alex now has: £" + str(numBalance))
