### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FRIEND LIST
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Ask a user to enter the names of 5 of their friends.
# Add the names to a list and then print them in alphabetical order.
### OBJECTIVE ###

### Declare CALLs & DEFs ###


### Declare/Input VALs & STRINGs ###
friendList = []

### DEPRECATED
#print("PLEASE ENTER THE NAME OF FIVE (5) OF YOUR FRIENDS:")
#friendList.append(input())
#friendList.append(input())
#friendList.append(input())
### DEPRECATED


# FOR LOOP TO ACCEPT USER INPUT
for count in range(5):
    print("PLEASE ENTER THE NAME OF FIVE (5) OF YOUR FRIENDS:")
    friendList.append(input())

# SORT FOOD LIST ALPHABETICALLY
friendList.sort()


### CALCs ###


### OUTPUTs ###

# PRINT FOOD LIST
print(friendList)

