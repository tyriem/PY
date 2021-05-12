### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - INTERESTING STORY
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# The idea is that the program asks the user for their name and various other details, and the program then fills in the gaps in the story. 
### OBJECTIVE ###

# Print the program title
print('''
######################
###  Interesting   ###
###     Story      ###
######################
''')

#####################
###     CODE      ###
#####################

### INPUTs ###
NAME = input("Please enter your name: ") 

AGE = input("Please enter your age: ") 

HEROINE = input("Please enter the name of your favourite female: ") 

WISH = input("What super-power would you wish for? ") 

RANDOM = input("Please enter a random word, the weirder the better: ") 

FAMOUS = input("Please enter the name of your favourite famous person: ") 

print("Once upon a time there was a handsome prince called", NAME) 

print(NAME, " was only ", AGE, " years old when he fell down a well.")

print("He would have stayed there forever, if it wasn’t for", HEROINE) 

print(HEROINE, " wanted to wish for", WISH, " and so she decided to visit the wishing well.") 

print("She threw a coin into the well, and it landed on ", NAME, "’s head!")

print(NAME, " shouted out the word ", RANDOM, " in pain.") 

print(HEROINE, " heard his shout, and ran to fetch ", FAMOUS) 

print(FAMOUS, " then came and rescued ", NAME)

print("Prince ", NAME, " was so happy and fell in love with ", HEROINE) 

print("So they got married, and ", FAMOUS, " was the special guest at the wedding.") 
