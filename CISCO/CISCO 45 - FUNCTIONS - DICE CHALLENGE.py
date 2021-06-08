### AUTHOR: TMRM
### CONTRIBUTORS:  
### PROJECT: CISCO DevNet - FUNCTIONS - CHALLENGE
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# CHALLENGE - Use Python to create a simple Dice Game.
# Using two dice the game should create two numbers randomly,
# then print a message that says "You won" if you get a 7 or 11.
# If dice 1 and dice 2 are the same numbers, print a message that says "Wow you got double".
# If you roll a number that is not 7, 11 or double print a message that says "You lose"
### OBJECTIVE ###

### PRINT Program Title ###
print('''
###################
###     DICE    ###
###     ROLL    ###  
###     FUNC    ###
###################
''')

### IMPORTs & DEFs ###

# IMPORT the random module
import random

# DEFine the func_rules function
def func_rules():
    # PRINT Spacer
    print("-----------------")

    # PRINT Rules
    print("To Win You Must: \n A) Roll a 7 or 11 \n B) Roll a Double")

    # PRINT Spacer
    print("-----------------")

# DEFine the func_switch_dice_img switch function and pass it WILDCARD(*) ARGUMENTS
def func_switch_dice_img(*args):
    #SWITCH STATEMENT switcher
    switcher = {
        1: "+-----+\n|     |\n|  o  |\n|     |\n+-----+",
        2: "+-----+\n| o   |\n|     |\n|   o |\n+-----+",
        3: "+-----+\n| o   |\n|  o  |\n|   o |\n+-----+",
        4: "+-----+\n| o o |\n|     |\n| o o |\n+-----+",
        5: "+-----+\n| o o |\n|  o  |\n| o o |\n+-----+",
        6: "+-----+\n| o o |\n| o o |\n| o o |\n+-----+"
    }
    #PRINT SWITCH STATEMENT VALUE
    print(switcher.get(*args))

    
# DEFine the func_roll function and pass it dice_one & dice_two
def func_roll(dice_one,dice_two):
    # PRINT Inform the user of their first roll
    print("Dice One was a: " + str(dice_one))

    # CALL func_switch_dice_img | dice_one
    func_switch_dice_img(dice_one)

    # PRINT Inform the user of their second roll
    print("Dice Two was a: " + str(dice_two))

    # CALL func_switch_dice_img | dice_two
    func_switch_dice_img(dice_two)

    ### CALCs & LOOPs ###

    # Combine the rolls to the overall roll
    dice = (dice_one + dice_two)

    # Inform the user of their overall roll
    print("Your Roll Was: ",dice)

    # Spacer
    print("-----------------")
    # IF ELIF ELSE statement to evaluate their roll and inform user of their results
    if dice_one == dice_two:
        print("Wow, You Got A Double!")
    elif dice == 7:
        print("You Won!")
    elif dice == 11:
        print("You Won!")
    else:
        print("You Lose...")
        
    # Spacer
    print("-----------------")


### CALLs / INPUTs ###

# CALL func_rules
func_rules()


# INPUT User's Keystroke
key_input = input("Press Enter Key to Roll The Dice.")

# PRINT Spacer
print("-----------------")

# CALL random to roll dice_one
dice_one = random.randint(1,6)
# CALL random to roll dice_two
dice_two = random.randint(1,6)



#CALL func_roll | dice_one , dice_two
func_roll(dice_one,dice_two)

