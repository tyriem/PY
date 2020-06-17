### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - 
### VER: 1.0
### DATE: 05-XX-2020

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
#Create a simple Guessing Game program
#First the computer must choose a random number (Between 1 and 10 inclusive).
#The user must then attempt to guess the number chosen.
#If the user was correct, the program must display a nice message.
#If the user was wrong, the program must tell them if their guess was too big or too small.
#Good coding practices are expected.
### OBJECTIVE ###

##Declare CALLs & DEFs
import random

#PRINT THE GAME NAME
print ("---------------------")
print ("Guess The Number Game")
print ("---------------------")

#ACCEPT THE USER INPUT OF THEIR NAME
name = str(input("Please Enter Your Name: "))

#GREET THE USER & EXPLAIN THE GAME RULES/LOGIC
print("Good Day ", name)
print("Welcome to the guessing game.")
print("Try and guess the number between 1 & 10.")

#ACCEPT THE USER INPUT OF THEIR GUESS
guess = int(input("Please Enter Your Guess: "))

#GENERATE THE RANDOM NUMBER IN THE GIVEN RANGE
dice = random.randint(1, 10)

#PRINT SPACER
print ("---------------------")

#PRINT THE VALUE OF THE DICE ROLL
print ("The Value of The Number Was: ", dice)


#IF ELIF ELSE LOGIC

# LOGIC FOR TOO HIGH A GUESS
if (guess > dice):
    print("Sorry, your guess was too high")
# LOGIC FOR CORRECT GUESS
elif (guess == dice):
    print("Well Done. You Guessed The Number Correctly!")
# LOGIC FOR TOO LOW A GUESS
elif (guess < dice):
    print("Sorry, your guess was too low!")
# LOGIC FOR INVALID INPUT   
else:
    print("Sorry, your input was invalid")

    



##OUTPUTs
