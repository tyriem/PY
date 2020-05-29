### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Function Assignment #2: Compute Pay
### VER: 1.0
### DATE: 05-XX-2020

##Declare CALLs & DEFs

#Define the compute_pay function and pass it hours & rate
def compute_pay(hours,rate):
    return hours * rate

def ot_pay(othours,rate):
    return (othours * (rate * 1.5))

x = int((input("ENTER YOUR HOURLY WAGE: ")))
y = int((input("ENTER HOW MANY (REGULAR) HOURS YOU WORKED THIS WEEK: ")))
z = int((input("ENTER HOW MANY (OVERTIME) HOURS YOU WORKED THIS WEEK: ")))
print("You earned this much REGULAR PAY this week: $",(compute_pay(x,y)))
print("You earned this much OVERTIME PAY this week: $",(ot_pay(z,y)))
print("Your total earnings for the week are: $",((compute_pay(x,y)) + (ot_pay(z,y))))

















