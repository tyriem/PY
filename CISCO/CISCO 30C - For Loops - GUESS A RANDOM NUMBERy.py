### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FOR-LOOP - GUESS A RANDOM NUMBER
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# A) SIMULATE A COIN TOSS
# B) COUNT THE TOTAL NUMBER OF OUTCOMES FOR THE COIN
### OBJECTIVE ###


#####################
###     CODE      ###
#####################

import random
guess =""
print("I've thought of a number between 1 and 10. Try to guess it.")
randomNumber = random.randrange(1,10)
while guess != randomNumber:
    guess = int(input("Guess the number: "))
    print("You got it wrong")
input ("Well done. Press any key to exit.")
