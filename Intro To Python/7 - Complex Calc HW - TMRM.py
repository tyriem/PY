### AUTHOR: TMRM   
### PROJECT: Complex Calculation HW
### VER: 1.0
### DATE: 05-18-2020



#Declare CALLs



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

#NIB Output
print (str("NIB Contribution"))
print (str(" $ ") + str(round(nib,2)))

#Net Output
print (str("Net Pay"))
print (str(" $ ") + str(round(net,2)))
