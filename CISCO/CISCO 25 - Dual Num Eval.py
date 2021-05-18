### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Dual Number Evaluator
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
### OBJECTIVE ###

# Print the program title
print('''
#####################
###     Dual      ###
###      Num      ###
###      Eval     ### 
#####################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs


##Declare/Input VALs & STRINGs


numFirst = float(input("Input the first number to be evaluated: "))
numSecond = float(input("Input the second number to be evaluated: "))
numSum = numFirst + numSecond
numPro = numFirst * numSecond

##CALCs & OUTPUTS

if numFirst > 10:
   print("You have entered the numbers " + numFirst + " and " + numSecond + ", their sum is: " + numSum)

else:
   print("You have entered the numbers " + numFirst + " and " + numSecond + ", their product is: " + numPro)


