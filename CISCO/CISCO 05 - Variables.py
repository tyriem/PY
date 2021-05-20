### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - All About Me - Variables
### VER: 1.0
### DATE: 05-04-2021

### OBJECTIVE ###
# Create a program that does the following
# 1-Write your own name and store it into a variable.
# 2- Write your own age and store it into a variable.
# 3- Print your age and name out into the screen.
# Challenge Add 2 moe details about yourself byusing variables.
### OBJECTIVE ###

#####################
###     CODE      ###
#####################

##Declare CALLs & DEFs

#Declare VARs

stringFirstName = "Tyrie "
stringLastName = "Moss"
stringFullName = stringFirstName + stringLastName
intAge = 31
stringShow = "Serial Experiments: Lain"
stringColor = 'Emerald'

#OUTPUTs
print ("My name is " + stringFullName + ". " + "My age is " + str(intAge) + ". ")
print ("My favorite television show is " + stringShow + ". " + "My favorite color is " + stringColor + ". ")



