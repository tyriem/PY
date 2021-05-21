### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FOR-LOOP: NESTED FOR LOOP 
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# FOR LOOP EXAMPLES
### OBJECTIVE ###


#####################
###     CODE      ###
#####################


# PRINT TIMES TABLE - ENHANCED ###
for i in range(1,13):
    print(i, end="\t")
print("")
print("___________________________________________________________________________________________")

for j in range(1,13):
    for k in range(1,13): #NESTED LOOP
        print(j * k, end="\t")
    print("\n")
