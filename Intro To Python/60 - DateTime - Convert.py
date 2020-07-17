### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Convert Seconds / Minutes
### VER: 1.0
### DATE: 06-25-2020

##############################
### DATE / TIME - CONVERT  ###
##############################

### OBJECTIVE ###
# Convert the below code to yield minutes per week, day, hour
### OBJECTIVE ###

"""
#Python's program to convert number of days, hours, minutes and seconds to
#seconds.

#Define the constants
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400
#Read the inputs from user
days = int(input("Enter number of Days: "))
hours = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))
#Calculate the days, hours, minutes and seconds
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + ( hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + ( minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds
#Display the result
print("Total number of seconds: ","%d"%(total_seconds))
"""

### CODE ###
#Define the constants
MINUTES_PER_WEEK = 10080
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 1440
#Read the inputs from user
weeks = float(input("Enter number of Weeks: "))
days = float(input("Enter number of Days: "))
hours = float(input("Enter number of Hours: "))
minutes = float(input("Enter number of Minutes: "))

#Calculate the days, hours, minutes and seconds
total_minutes = weeks * MINUTES_PER_WEEK
total_minutes = total_minutes + (days * MINUTES_PER_DAY)
total_minutes = total_minutes + ( hours * MINUTES_PER_HOUR)
total_minutes = total_minutes + minutes
#Display the result
print("Total number of minutes: ","%d"%(total_minutes))
