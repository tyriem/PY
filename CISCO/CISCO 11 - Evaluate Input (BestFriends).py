### AUTHOR: TMRM   
### PROJECT: CISCO DEVNET - Friend Eval
### VER: 1.0
### DATE: 05-05-2021

### OBJECTIVE ###
# Write a program that asks for 2 of your friend’s names
# and then states which friend is the best friend.
# Save as BestFriends.
### OBJECTIVE ###


#####################
###     CODE      ###
#####################



##Declare CALLs & DEFs

import random

# Print the program title
print('''
########################
###      Tyrie's     ###
###       Friend     ###
###     Evaluator    ###
########################
''')

## Declare/Input VALs & STRINGs ##

#Set VAR for BestFriend
stringBestFriend = "Dog"


# ACCEPT THE USER'S INPUT
stringFirstFriend = (input("GOOD DAY FRIEND,\n PLEASE ENTER YOUR NAME: "))
stringSecondFriend = (input("GOOD DAY FRIEND,\n PLEASE ENTER YOUR NAME: "))

listFriend = ['stringFirstFriend', 'stringSecondFriend']

print("-----------------------------------------------------------------------------------------------------")

## CALCs ##

# ELIF Evaluate string(X)Friend
if   stringBestFriend == "Dog":
     print("You are the Best Friend, " + stringFirstFriend + ".")

elif stringBestFriend == "Dog":
     print("You are the Best Friend, " + stringSecondFriend + ".")
   
else:
   print("Neither of you are Tyrie's Best Friend, but you are the better friend at the moment, " + random.choice(listFriend) + ".")


## OUTPUTs ##

print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
