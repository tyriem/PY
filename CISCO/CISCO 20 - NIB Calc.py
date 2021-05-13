### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - NIB CALC
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program to prompt the user for hours worked, rate per hour, and NIB contribution.
# Thereafter, input the codes to compute net pay, remember to display proper labeling.
# Example segment to assist:
# Input the number of hours work:  30
# Input the rate: 40.0
# gross pay = hours work * rate
# NIB = .03 (that is 3% of gross pay)
# net pay = gross pay – NIB
# print net pay.
### OBJECTIVE ###

# Print the program title
print('''
######################
###       NIB      ###
###   Calculator   ###
######################
''')

#####################
###     CODE      ###
#####################

##INPUT
hours = int(input("Input The Number of Hours Worked = "))
raw_rate = input("Input The Rate Per Hour = ")
rate = float(raw_rate.replace("$",""))

##CALC
gross = float(hours * rate)
nib = float(gross * 0.03)
net = float(gross - nib)


##OUTPUT

#SPACER
print ("---------------------")

#Gross Output
print (str("Gross Pay"))
print (str(" $ ") + str(round(gross,2)))

#SPACER
print ("---------------------")

#NIB Output
print (str("NIB Contribution"))
print (str(" $ ") + str(round(nib,2)))

#SPACER
print ("---------------------")

#Net Output
print (str("Net Pay"))
print (str(" $ ") + str(round(net,2)))


#SPACER
print ("---------------------")
#SPACER
print ("---------------------")
