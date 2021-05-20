### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Number Guess Eval
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same
# as the number picked by the magician. If the number chosen by the user
# is different than the magician's secret number, the user should see the message
# "Ha ha! You're stuck in my loop!" and be prompted to enter a number again.
# If the number entered by the user matches the number picked by the magician,
# the number should be printed to the screen,
# and the magician should say the following words:
# "Well done, muggle! You are free now."
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
   # ACCEPT USER INPUT AS INTEGER
   password = int(input("What is the secret number?"))
   # NESTED IF-ELSE TO EVALUATE INPUT
   if password == secret_number:
      print("You selected the number: " + secret_number + ".")
      print("Well done, muggle! You are free now.")
      break
   else:
        print("Ha ha! You're stuck in my loop!")
