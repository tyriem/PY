### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Variable Calc
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that uses the following variable to calculate
# the number of minutes in a week:
# DaysPerWeek
# HoursPerDay
# MinutesPerHour
### OBJECTIVE ###

# Print the program title
print('''
#######################
###   Mintutes In   ###
###      A Week     ###
#######################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs & DEFs

#Declare VARs

daysPerWeek = 7
hoursPerDay = 24
minutesPerHour = 60
minutesPerWeek = (minutesPerHour * hoursPerDay * daysPerWeek)

#OUTPUTs
print ("The amount of minutes in a week equals " + str(minutesPerWeek) + ". ")
