### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - For Loop Counter
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that uses a for loop to "count mississippily" to five.
# Having counted to five, the program should print to the screen the final message
# "Ready or not, here I come!"
### OBJECTIVE ###


#####################
###     CODE      ###
#####################

### CALLs & DEFs ###

# Import TIME
import time

# Program to find the sum of all numbers stored in a list

# List of numbers
listNumbers = [1, 2, 3, 4, 5]


# iterate over the list
for i in listNumbers:
   time.sleep(1)
   print(str(i) + " Mississippi")

print("Ready or not, here I come!")
