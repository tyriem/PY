### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FUNCTIONS - SHUTDOWN
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# First, def a function, shut_down, that takes one argument s.
# Then, if the shut_down function receives an s equal to "yes",
# it should return "Shutting down" Alternatively, elif s is equal to "no",
# then the function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs,
# the function should return "Sorry".  The line numbers are for references only.
### OBJECTIVE ###

# Print the program title
print('''
##########################
###      FUNCTIONS     ###
###      SHUTDOWN      ###
##########################
''')



### Declare CALLs & DEFs ###

#Define the shutdown function and pass it as s
def shut_down(s):
#Set the IF_ELIF_ELSE statement for outcomes of the function   
    if s == 'y':
        print("Shutting Down")
    elif s == 'n':
        print("Shutdown Aborted")
    else:
        print("Sorry")


### INPUTs & OUTPUTs ###
        

# ACCEPT USER INPUT
stringSRaw = input("Computer Is About To Shut Down: Y̲es OR N̲o ")

#Create stringS from stringSRaw
stringS = stringSRaw.lower()


#Create charS from stringS
s = stringS[0:1]

#USE THE FUNCTION
shut_down(s)
