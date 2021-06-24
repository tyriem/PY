### AUTHOR: TMRM
### CONTRIBUTORS:   
### PROJECT: CISCO DevNet - CONDITIONAL OPERATORS - CINEMA RATINGS
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# According to the British Board of Film Classification, movies shown at the cinema in the UK should have one of the following age certificate ratings:
# Using your knowledge of selection, comparative operators and Boolean operators, write a Python program that will do the following:
# 1. Ask the user to enter their age.
# 2. Output a list of film age certificates which the user can watch
# (i.e. U, PG, 12A, 12, 15 or 18).
# 3. When you have finished: Test your program several times to make sure that it works. Then test someone else’s program.
### OBJECTIVE ###

print('''
#####################
###     CINEMA    ###
###    SELECTOR   ###  
#####################
''')

### IMPORTs & DEFs ###


### VARs & CALCs ###
age = int(input("How old are you?"))

# EVAL Selection
if age >= 18:
    print("U, PG, 12, 12A, 15, 18")

elif age >= 15 and age < 18:
    print("U, PG, 12, 12A, 15")

elif age >= 12 and age < 15:
    adult = input("Are you with an adult? (YES OR NO)")
    if adult == "yes" or adult == "Yes" or adult == "YES" or adult == "y":
        print("YOU CAN VIEW THE FOLLOWING RATED FILMS: U, PG, 12, 12A")
    else:
        print("YOU CAN VIEW THE FOLLOWING RATED FILMS: U, PG, 12")

elif age >= 8  and age < 12:
    adult = input("Are you with an adult? (YES OR NO)")
    if adult == "yes" or adult == "Yes" or adult == "YES" or adult == "y":
        print("YOU CAN VIEW THE FOLLOWING RATED FILMS: U, PG")
    else:
        print("YOU SHOULDN'T BE HERE UNATTENDED")

elif age >= 4  and age < 8:
    adult = input("Are you with an adult? (YES OR NO)")
    if adult == "yes" or adult == "Yes" or adult == "YES" or adult == "y":
        print("YOU CAN VIEW THE FOLLOWING RATED FILMS: U")
    else:
        print("YOU SHOULDN'T BE HERE UNATTENDED")


elif age >= 0  and age < 3:
    print("GOO GOO GA GA!")

else:
    print("INVALID AGE, PLEASE ENTER AGAIN")

        
