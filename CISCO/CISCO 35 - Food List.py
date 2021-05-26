### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FOOD LIST
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


### Declare/Input VALs & STRINGs ###
foodList = []

### DEPRECATED
#print("PLEASE ENTER THREE FOODS (ONE AT A TIME):")
#foodList.append(input())
#foodList.append(input())
#foodList.append(input())
### DEPRECATED


# FOR LOOP TO ACCEPT USER INPUT
for count in range(3):
    print("PLEASE ENTER THREE FOODS (ONE AT A TIME):")
    foodList.append(input())

# SORT FOOD LIST ALPHABETICALLY
foodList.sort()


# PRINT FOOD LIST
print(foodList)



### CALCs ###


### OUTPUTs ###
