### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - While Loop Password 
### VER: 1.0
### DATE: 05-25-2020

##Declare CALLs

import random

##LOOPs and VARs

dice_roll = random.randint(1,6)
k=10
while k > 0:
      guess = int(input("Please Enter Your Guess: \n"))
      if guess != dice_roll:
         print("Guess Again")
         k = k - 1
      else:
           print("This Is Correct")
else:
           print("You Are Out Of Guesses")

