### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Casting
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Create a variable called number and allow the user to assign a value to it.
# Now add this line:
# print (number + number)
# Run the program. Did it work?
# Try converting/casting the data type:
# number = int(number)
#
### OBJECTIVE ###


### V1 ###
#
# number = float(input("ENTER NUMBER TO BE SUMMED TOGETHER: "))
# print (number + number)
### V1 ###


### V2 ###
number = float(input("ENTER NUMBER TO BE SUMMED TOGETHER: "))
number = int(number)
print (number + number)
