### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - FUNCTIONS - COMPUTE PAY WITH OVERTIME
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# Write your pay computation program with time-and-a-half
# for overtime and create a function called computepay
# which takes two parameters (hours and wage).
### OBJECTIVE ###

# Print the program title
print('''
##########################
###      FUNCTIONS     ###
###         PAY        ###
##########################
''')



### DEPRECATED ###
### Declare CALLs & DEFs ###
#
#Define the compute_pay function and pass it hours & rate
#def compute_pay(hours,rate):
#    return hours * rate
#
#Define the ot_pay function and pass it hours & rate and factor in the Time-and-a-Half (1.5 X)
#def ot_pay(othours,rate):
#    return (othours * (rate * 1.5))
#
#
### INPUTs & OUTPUTs ###
#
# ACCEPT USER INPUT
#x = float((input("ENTER YOUR HOURLY WAGE: ")))
#y = float((input("ENTER HOW MANY (REGULAR) HOURS YOU WORKED THIS WEEK: ")))
#z = float((input("ENTER HOW MANY (OVERTIME) HOURS YOU WORKED THIS WEEK: ")))
#
# PRINT FUNCTION OUTPUT
#
#OUTPUT REGULAR PAY
#print("You earned this much REGULAR PAY this week: $",(compute_pay(x,y)))
#OUTPUT OVERTIME PAY
#print("You earned this much OVERTIME PAY this week: $",(ot_pay(z,y)))
#OUTPUT TOTAL EARNINGS PAY
#print("Your total earnings for the week are: $",((compute_pay(x,y)) + (ot_pay(z,y))))
### DEPRECATED ###



### Declare CALLs & DEFs ###

#Define the compute_pay function and pass it numHours & numWage
def compute_pay(numHours,numWage):
    if numHours <= 40:
        return numHours * numWage
    else:
        return (40 * numWage) + ((numHours - 40) * (numWage * 1.5))



### INPUTs & OUTPUTs ###

## ACCEPT USER INPUT

rawNumWage = input("ENTER YOUR HOURLY WAGE: ")
# STRIP CASHINO SYMBOL
stringWage = rawNumWage.replace("$","")
# CONVERT TO FLOAT
numWage = float(stringWage)

numHours = float((input("ENTER HOW MANY HOURS YOU WORKED THIS WEEK: ")))


## PRINT FUNCTION OUTPUT

#OUTPUT PAY 
print("You earned this much this week: $",(compute_pay(numHours,numWage)))
