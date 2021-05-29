### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - IF-ELSE + MODULUS - LEAP YEAR
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
# It would be good to verify if the entered year falls into the Gregorian era,
# and output a warning otherwise: Not within the Gregorian calendar period.
#Tip: use the != and % operators.
### OBJECTIVE ###

#####################
###     CODE      ###
#####################

# Print the program title
print('''
####################
###      LEAP    ###
###      YEAR    ###
###      EVAL    ### 
####################
''')

### VARs ###

# ACCEPT USER INPUT
numYear = int(input("ENTER A YEAR TO BE EVALUATED: "))

### CALCs ###

# CALCULATE MODULO OF numYear
numYearMod = numYear % 4

# IF STATEMENT TO EVALUATE USER INPUT
if numYearMod == 0 and numYear >= 1582:
   print("THE YEAR: " + str(numYear) + " IS/WAS A LEAP YEAR")
elif numYearMod != 0 and numYear >= 1582:
   print("THE YEAR: " + str(numYear) + " IS/WAS A COMMON YEAR")
else:
   print("INVALID DATE DETECTED")
