### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - RAND RAINBOW LIST
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Create a list that contains the seven colours in the rainbow (in their correct order).
# Generate a random number (between 0 and 6 inclusive) and use this as the list index to randomly select a colour to print it.
# e.g. if your random number was 3, your code should print the colour at index 3 (green).
### OBJECTIVE ###

### Declare CALLs & DEFs ###
import random

### Declare/Input VALs & LISTs ###

# DECLARE rainbowList
rainbowList = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Declare Index | Set it to 6 random integers
index = random.randint(0,6)

### OUTPUT ###

# PRINT a random entry in rainbowList

print(rainbowList[index])
