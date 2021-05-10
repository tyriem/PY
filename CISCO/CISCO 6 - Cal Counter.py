### AUTHOR: TMRM   
### PROJECT: CISCO DEVNET - Data Input
### VER: 1.0
### DATE: 05-05-2021

### OBJECTIVE ###
# The suggested caloric intake for females is 2000 cal./day, for males it is 2500;
# Write a program that checks how many calories someone takes in a day versus these suggestions
### OBJECTIVE ###


#####################
###     CODE      ###
#####################



##Declare CALLs & DEFs


# Print the program title
print('''
#####################
###   Calorie     ###
###   Intake      ###
###   Checker     ###
#####################
''')

## Declare/Input VALs & STRINGs ##

#Set VAR for male calorie normal
numCalMale = 2500
#Set VAR for female calorie normal
numCalFemale = 2000

# ACCEPT THE USER'S INPUT
stringFirstName = (input("GOOD DAY,\n PLEASE ENTER YOUR FIRST NAME: "))
stringLastName = (input("PLEASE ENTER YOUR LAST NAME: "))
numAge = int(input("PLEASE ENTER YOUR CURRENT AGE: "))
numCalUser = int(input("PLEASE ENTER THE AMOUNT OF CALORIES IN YOUR DIET TODAY: "))

#Eval Full Name from First & Last
stringFullName = stringFirstName + " " + stringLastName


stringRawGen = (input("PLEASE ENTER YOUR SEX (Male, Female, Other): "))

#Create stringGenLower from stringRawGen
stringGenLower = stringRawGen.lower()

#Create charGen from stringRawGen
charGen = stringGenLower[0:1]

# DEPRECATED
#if stringRawGen == "M" or stringRawGen == "m" or stringRawGen == "Male" or stringRawGen == "male":
#        charGen = 'm'
#else:
#   charGen = 'f'
# DEPRECATED



print("-----------------------------------------------------------------------------------------------------")

## CALCs ##

# ELIF Evaluate numAge against reasonable values
if numAge < 18:
   print("Thank you, kid.")
   print("You are too young to be using this calculator.")
   exit()

elif numAge >= 300:
   print("Thank you, Methuselah.")
   print("Aren't you a bit old to be using this calculator?")
   
else:
   print("Thank you, " + stringFullName + ".")
   print("You are " + str(numAge) + " years old.")



# Evaluate numCalUser against numCal values

if numCalUser <= numCalFemale:
   print("Your caloric intake of " + str(numCalUser) + " calories is within your calorie allowance for the day.")

elif numCalUser <= numCalMale and charGen == "m":
   print("Your caloric intake of " + str(numCalUser) + " calories is within your calorie allowance for the day.")

elif numCalUser <= 9000:
   print("Warning. Your caloric intake of " + str(numCalUser) + " calories is above your calorie allowance for the day.")

elif numCalUser > 9000:
   print("Your caloric intake is over 9000! Please seek medical attention immediately.")
   
else:
   print("You have entered an invalid input, please try again.")

## OUTPUTs ##
print("-----------------------------------------------------------------------------------------------------")
print("For more information on calorie intake visit:")
print("https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/#")
print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
