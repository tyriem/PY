### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Function Assignment #1: Shut Down 
### VER: 1.0
### DATE: 05-XX-2020

##Declare CALLs & DEFs

#Define the shutdown function and pass it s
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
