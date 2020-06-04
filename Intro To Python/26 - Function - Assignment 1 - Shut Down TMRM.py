### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Function Assignment #1: Shut Down 
### VER: 1.0
### DATE: 05-29-2020

### OBJECTIVE ###
#First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".  The line numbers are for references only.
### OBJECTIVE ###

##Declare CALLs & DEFs

#Define the shutdown function and pass it as s
def shut_down(s):
#Set the IF_ELIF_ELSE statement for outcomes of the function   
    if s == 'yes':
        print("Shutting Down")
    elif s == 'no':
        print("Shutdown Aborted")
    else:
        print("Sorry")


##INPUTs & OUTPUTs
        
#ACCEPT THE USER'S INPUT AS s
s = (input("Computer Is About To Shut Down: yes OR no "))
#USE THE FUNCTION
shut_down(s)
