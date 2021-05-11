### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Calorie Counter
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# We are going to write a simple program to ask someone how many calories
# they have eaten today and return the calories they have left to eat.
# Below is a table that shows how many calories a boy and girl should eat daily.
# Female: 2000
# Male: 2500
### OBJECTIVE ###

# Print the program title


print('''
#####################
###   Calorie     ###
###   Counter     ###
#####################
''')

### Declare CALLs & DEFs ###

#Set VAR for male calorie normal
numCalMale = 2500
#Set VAR for female calorie normal
numCalFemale = 2000


### Declare/Input VALs & STRINGs ###

# ACCEPT USER INPUT
numCalUser = int(input("HOW MANY CALORIES HAVE YOU EATEN TODAY?"))

stringRawGen = (input("PLEASE ENTER YOUR SEX (Male, Female, Other): "))

#Create stringGenLower from stringRawGen
stringGenLower = stringRawGen.lower()

#Create charGen from stringRawGen
charGen = stringGenLower[0:1]



# Evaluate numCalUser against numCal values

if numCalUser <= numCalFemale:
   print("You can eat" + str(int(2000) - numCalUser) + " more calories today.")

elif numCalUser <= numCalMale and charGen == "m":
   print("You can eat" + str(int(2500) - numCalUser) + " more calories today.")

elif numCalUser > numCalFemale and charGen != "m":
   print("Warning. Your caloric intake of " + str(numCalUser) + " calories is above your calorie allowance for the day by " + str(numCalUser - int(2000)) + " calories.")

elif numCalUser > numCalMale and charGen == "m":
   print("Warning. Your caloric intake of " + str(numCalUser) + " calories is above your calorie allowance for the day by " + str(numCalUser - int(2500)) + " calories.")
   
else:
   print("You have entered an invalid input, please try again.")

## OUTPUTs ##
print("-----------------------------------------------------------------------------------------------------")
print("For more information on calorie intake visit:")
print("https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/#")
print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
