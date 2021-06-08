### AUTHOR: TMRM
### CONTRIBUTORS: SNOR  
### PROJECT: CISCO DevNet - FUNCTIONS - CHALLENGE - PARA
### VER: 2.0B
### DATE: 06-XX-2021


### OBJECTIVE ###
# CHALLENGE - Use Python to create a simple Dice Game.
# Using two dice the game should create two numbers randomly,
# then print a message that says "You won" if you get a 7 or 11.
# If dice 1 and dice 2 are the same numbers, print a message that says "Wow you got double".
# If you roll a number that is not 7, 11 or double print a message that says "You lose"
### OBJECTIVE ###

print('''
###################
###     DICE    ###
###     ROLL    ###  
###     FUNC    ###
###################
''')

### IMPORTs & DEFs ###

import random

# What does this function do?
def games_rules():
    print("-----------------")
    print("To Win You Must: \n A) Roll a 7, 11 \n B) Roll a Double")
    print("-----------------")

# What does this function do?
def dice_ascii_img(dice_number):
    switcher = {
        1: "+-----+\n|     |\n|  o  |\n|     |\n+-----+",
        2: "+-----+\n| o   |\n|     |\n|   o |\n+-----+",
        3: "+-----+\n| o   |\n|  o  |\n|   o |\n+-----+",
        4: "+-----+\n| o o |\n|     |\n| o o |\n+-----+",
        5: "+-----+\n| o o |\n|  o  |\n| o o |\n+-----+",
        6: "+-----+\n| o o |\n| o o |\n| o o |\n+-----+"
    }
    return switcher.get(dice_number)

    
# What does this function do?
def roll_result(dice_one,dice_two):
    # Dice one
    print("Dice One was a: " + str(dice_one) + " and Dice Two was a: " + str(dice_two))
    dice_one_img = dice_ascii_img(dice_one)

    dice_two_img = dice_ascii_img(dice_two)
    dice_one_split = dice_one_img.splitlines()
    dice_two_split = dice_two_img.splitlines()
    
    for index in range(0, 5):
        print(dice_one_split[index]+ " " +dice_two_split[index])

    dice = (dice_one + dice_two)
    print("Your Roll Was: ",dice)

    print("-----------------")
    
    # Validate roll
    if dice_one == dice_two:
        print("Wow, You Got A Double!")
    elif dice == 7:
        print("You Won!")
    elif dice == 11:
        print("You Won!")
    else:
        print("You Lose...")
        
    print("-----------------")

# State game rules
games_rules()

# Await enter key
key_input = input("Press Enter Key to Roll The Dice.")

print("-----------------")

dice_one = random.randint(1,6)
dice_two = random.randint(1,6)

roll_result(dice_one,dice_two)
