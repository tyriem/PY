### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FOR-LOOP: NESTED FOR LOOP 
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# A) SIMULATE A COIN TOSS
# B) COUNT THE TOTAL NUMBER OF OUTCOMES FOR THE COIN
### OBJECTIVE ###


#####################
###     CODE      ###
#####################

# IMPORT FUNC RANDOM
import random

# INIT VARs
totalHeads = 0
totalTails = 0

# FOR LOOP
for count in range(10):
# SIMULATE THE TOSS OF A COIN
    coin = random.randint(0,1)
# PRINT HEADS(0) or TAILS(1)
    if coin == 0:
        print("HEADS")
        totalHeads += 1
    else:
        print("TAILS")
        totalTails += 1

# OUTPUT
print("The total amount of HEADS was:", totalHeads)
print("The total amount of TAILS was:", totalTails)
