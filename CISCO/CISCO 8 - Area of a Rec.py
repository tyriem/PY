### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Area of a Rectangle
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Asks for the width of a rectangle. Asks for the length of arectangle.
# Calculates the area of a rectangle. Print the area of arectangle.
# To multiply numbers use
# width = int(input("________")) ______ = int(input("Enter a height"))area = _____*_____ print("The area of the rectangle is", _____)
### OBJECTIVE ###

### Declare CALLs & DEFs ###

# Print the program title
print('''
#########################
###    Area of a      ###
###    Rectangle      ###
###    CALCULATOR     ###
#########################
''')

### Declare/Input VALs & STRINGs ###

# Accept user input
stringUnit = input("PLEASE ENTER THE UNIT OF MEASURE FOR THE RECTANGLE (EX. CM): ")
numLen = float(input("PLEASE ENTER THE LENGTH OF THE RECTANGLE: "))
numWid = float(input("PLEASE ENTER THE WIDTH OF THE RECTANGLE: "))


### CALCs ###
numArea = (numLen * numWid)


### OUTPUTs ###
("----------------------------------------------------")
print("Thank You.")
print("You have entered " + str(numLen) + " as the length of the rectangle.")
print("You have entered " + str(numWid) + " as the width of the rectangle.")
print("The area of a rectangle of length " + str(numLen) + " " + stringUnit + " and width " + str(numWid) + " " + stringUnit + " equals: " + str(numArea) + " " + stringUnit + "^2.")
("----------------------------------------------------")
