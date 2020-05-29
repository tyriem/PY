### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Practical: Calculating Weekly Pay With Overtime
### VER: 1.0
### DATE: 05-27-2020

# OBJECTIVE #
## Total Weekly Pay = hourly wage X total number of regular hours + any overtime pay
## Overtime pay = total overtime hours X 1.5 hourly wage

##Declare CALLs


##Declare/Input VALs & STRINGs

# ACCEPT THE USER'S WAGES AND HOURS #
raw_hourly_wage = (input("ENTER YOUR HOURLY WAGE: "))
raw_hours_worked = (input("ENTER HOW MANY (REGULAR) HOURS YOU WORKED THIS WEEK: "))
raw_hours_overtime = (input("ENTER HOW MANY (OVERTIME) HOURS YOU WORKED THIS WEEK: "))


# CLEAN THE USER INPUT # 
hourly_wage = float(raw_hourly_wage.replace("$",""))
hours_worked = int(raw_hours_worked.replace(" hours",""))
hours_overtime = int(raw_hours_overtime.replace(" hours",""))

##CALCs
# CALCULATE THE PAY # 
overtime_pay = (hours_overtime * (1.5 * hourly_wage))
regular_pay = (hourly_wage * hours_worked)
weekly_pay = (regular_pay + overtime_pay )

##OUTPUTs
# OUTPUT THE PAY #
print("---------------------------------------------")
print("Your Regular Pay for this week is: $", regular_pay )
print("Your Overtime Pay for this week is: $", overtime_pay )
print("---------------------------------------------")
print("Your Total Pay for this week is: $", weekly_pay)
