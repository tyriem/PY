### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Practical: Dice Rolling Evaluation
### VER: 1.0
### DATE: 05-XX-2020

# OBJECTIVE #
# Use Python to create a simple Dice Game.  Using two dice the game should create two numbers randomly, then print a message that says "You won" if you get a 7 or 11.  If dice 1 and dice 2 are the same numbers, print a message that says "Wow you got double".  If you roll a number that is not 7, 11 or double print a message that says "You lose".

##Declare CALLs

# Import the random module
import random

##Declare/Input VALs & STRINGs


# Accept the user's input to start program 
key_input = input("Press Enter Key to Roll The Dice.")

# Use random to roll the dice
dice_one = random.randint(1,6)
dice_two = random.randint(1,6)

# Inform the user of their roll
print("Dice One was a: " + str(dice_one) + " | " "Dice Two was a: " + str(dice_two))


##CALCs & LOOPs

# Combine the rolls to the overall roll
dice = (dice_one + dice_two)

# Inform the user of their overall roll
print("Your Roll Was: ",dice)

# Spacer
print("-------------------------------------------------")
# IF ELIF ELSE statement to evaluate their roll and inform user of their results
if dice_one == dice_two:
    print("Wow You Got A Double!")
elif dice >= 7:
    print("You Won!")
else:
    print("You Lose...")
    
# Spacer
print("-------------------------------------------------")