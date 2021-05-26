### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - RAND NUMBER LIST
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Ask the user to enter three foods (one at a time)
# Store these in a list
# Print the list in alphabetical order
### OBJECTIVE ###

### Declare CALLs & DEFs ###

import random

myList = []


### Declare/Input VALs & STRINGs ###

total = 0


for count in range(10):
    number = random.randint(1,10)
    myList.append(number)
    total += number



### CALCs ###


### OUTPUTs ###

print(myList)
print("the total is", total)
