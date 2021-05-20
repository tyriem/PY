### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - String Guess Eval
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
# prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
# Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!
### OBJECTIVE ###


#####################
###     CODE      ###
#####################




### CALLs & DEFs ###

# Import TIME
import time

### VARs ###

# INIT VAR: secret_number
secret_number = 10

# WHILE LOOP - True, to continue to loop infinitely as long as true = true
while True:
# ACCEPT USER INPUT AS STRING
   stringFlower = input("What is my favorite flower?")
# NESTED IF-ELSE TO EVALUATE INPUT
   if stringFlower == "Spathiphyllum":
      print("Yes - Spathiphyllum is the best plant ever!")
      break
   elif stringFlower == "spathiphyllum":
      print("No, I want a big Spathiphyllum!")
   else:
      print("Spathiphyllum! Not " + stringFlower + "!")
