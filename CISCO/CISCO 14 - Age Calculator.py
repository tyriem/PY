### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Age Calc
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program to work out how long a user has been alive for
# to the nearest year for the moment (there are 365 days in a year)
# Get the program to ask for the user’s name and age.
# Use the age variable value to work out how many hours that is – there is 24 hours per day
# Develop the program further so that it can work out how many minutes and seconds the user
# has lived for – 60 minutes per hour / 60 seconds per minute.
# Make sure all the information is clearly displayed on the screen.
### OBJECTIVE ###

# Print the program title
print('''
######################
###       Age      ###
###   Calculator   ###
######################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs & DEFs

## Declare/Input VALs & STRINGs ##

daysPerWeek = 7
hoursPerDay = 24
minutesPerHour = 60
minutesPerWeek = (minutesPerHour * hoursPerDay * daysPerWeek)

stringName = (input("GOOD DAY,\n PLEASE ENTER YOUR NAME: "))
numAge = int(input("PLEASE ENTER YOUR CURRENT AGE: "))

## CALCs ##
numWeekAge = (numAge * 52)
numDayAge = (numAge * 365)
numMinAge = (numAge * 525600)
numSecAge = (numAge * 31536000)



## OUTPUTs ##
print ("Thank you, " + stringName + ". You have been alive for at least: ")
print ("A) " + str(numAge) + " Years.")
print ("B) " + str(numWeekAge) + " Weeks.")
print ("C) " + str(numDayAge) + " Days.")
print ("D) " + str(numMinAge) + " Minutes.")
print ("E) " + str(numSecAge) + " Seconds.")
