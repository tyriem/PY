### AUTHOR: TMRM
### CONTRIBUTORS:  
### PROJECT: CISCO DevNet - RANDOM NUMBER GUESSER EDIT
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# EDIT THE BELOW CODE FOR A RANDOM NUMBER GUESSING GAME
### OBJECTIVE ###

print('''
#####################
###     RANDOM    ###
###     NUMBER    ###  
###     GUESS     ###
#####################
''')

### IMPORTs, INITs & DEFs ###

#IMPORT random
import random

 
# INIT VAR attempts
attempts = 1

# INIT GLOBAL VAR count_Guess
global count_Guess # DIFF

# SET VAR count_Guess
count_Guess = 5 # DIFF

# SET VAR secret_number to RAND number up to: 100
secret_number = random.randint(1,100)

# SET VAR isCorrect to FALSE
#isCorrect = False


### USER INPUT ###

# SET VAR guess to Input from User
guess = int(input("Guess the Counting Number That Has Been Generated. (You Have " + str(count_Guess) + " Guesses):")) ### DIFF

 
### LOOPS ###

# WHILE LOOP DECLARATION
while secret_number != guess and attempts < (count_Guess):

 
# LOGIC TO EVALUATE USER INPUT
    if guess < secret_number:

        print("Higher...")

    elif guess > secret_number:

        print("Lower...")

    guess = int(input("Take a guess: "))

    attempts += 1

 

if attempts == 5: ### DIFF

    print("\nSorry you reached the maximum number of tries")

    print("The secret number was ",secret_number)

 

else:

    print("\nYou guessed it! The number was " ,secret_number)

    print("You guessed it in ", attempts,"attempts")


 
# PROMPT FOR USER INPUT TO EXIT
input("\n\n Press the enter key to exit") 
