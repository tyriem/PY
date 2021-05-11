### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Sleep Calc 
### VER: 2.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Create a program to calculate how many hours per week you sleep
# Name
# When they went to bed
# When they woke up
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
numBed = float(input("When did you get to bed " + stringName + "?"))

stringRawAMPM = (input("In the AM or the PM?"))
stringAMPMLower = stringRawAMPM.lower()
charAMPM = stringAMPMLower[0:1]

numWake = float(input("When did you wake up? " + stringName + "?"))
stringRawAMPMWake = (input("In the AM or the PM?"))
stringAMPMLowerWake = stringRawAMPMWake.lower()
charAMPMWake = stringAMPMLowerWake[0:1]


# ELIF TO EVAL SLEEP
if charAMPM == 'p' and charAMPMWake == 'a':
    numSleep = ((12 - numBed) + numWake)
    print("You slept " + str(numSleep) + " hours yesterday.")

elif charAMPM == 'a' and charAMPMWake == 'p':
    numSleep = (numBed + (12 - numWake))
    print("You slept " + str(numSleep) + " hours yesterday.")

elif charAMPM == 'a' and charAMPMWake == 'a':
    numSleep = (numWake - numBed)
    print("You slept " + str(numSleep) + " hours yesterday.")

elif charAMPM == 'p' and charAMPMWake == 'p':
    numSleep = (numWake - numBed)
    print("You slept " + str(numSleep) + " hours yesterday.")
   
else:
    print("You have entered an invalid input, please try again.")

### CALCs ###

numWeekSleep = (numSleep * 7)

### LISTs ###

### OUTPUT ###
print ("Thank you, " + stringName + ". You sleep approximately " + str(numWeekSleep) + " hours per week.")
