### AUTHOR: TMRM
### CONTRIBUTORS:  
### PROJECT: CISCO DevNet - FUNCTIONS - CHALLENGE
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# CHALLENGE
### OBJECTIVE ###

# Print the program title
print('''
##########################
###      CHALLENGE     ###
##########################
''')



### Declare CALLs & DEFs ###

#Define the x function to: 
def x_func(hours,rate):
    return hours * rate

#Define the y function to:
def y_func(othours,rate):
    return (othours * (rate * 1.5))


### INPUTs & OUTPUTs ###

# ACCEPT USER INPUT
x = int((input("ENTER YOUR HOURLY WAGE: ")))
y = int((input("ENTER HOW MANY (REGULAR) HOURS YOU WORKED THIS WEEK: ")))
z = int((input("ENTER HOW MANY (OVERTIME) HOURS YOU WORKED THIS WEEK: ")))

# PRINT FUNCTION OUTPUT
print("You earned this much REGULAR PAY this week: $",(x_func(x,y)))
print("You earned this much OVERTIME PAY this week: $",(y_func(z,y)))
print("Your total earnings for the week are: $",((x_func(x,y)) + (y_func(z,y))))
