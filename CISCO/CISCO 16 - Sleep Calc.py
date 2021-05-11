### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Sleep Calc
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Create a program to calculate how many hours per week you sleep
# Name
# Hours do you sleep each night
### OBJECTIVE ###

# Print the program title
print('''
######################
###     Sleep      ###
###   Calculator   ###
######################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs & DEFs

## Declare/Input VALs & STRINGs ##

#ACCEPT USER INPUT
stringName = (input("GOOD DAY,\n PLEASE ENTER YOUR NAME: "))
numSleep = float(input("How many hours do you sleep per night " + stringName + "?"))

### CALCs ###

numWeekSleep = (numSleep * 7)

### LISTs ###

### OUTPUT ###
print ("Thank you, " + stringName + ". You sleep approximately " + str(numWeekSleep) + " hours per week.")
