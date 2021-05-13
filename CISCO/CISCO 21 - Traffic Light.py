### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - NIB CALC
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Ask the user to input traffic light colour.
# If the answer is red, display “STOP”
# Else if answer is yellow, display “Get set”
# Else if answer is green, display “GO”
# Else, display “Wrong colour”
### OBJECTIVE ###

# Print the program title
print('''
######################
###    Traffic     ###
###     Light      ###
######################
''')

#####################
###     CODE      ###
#####################

### Declare CALLs ###


### Declare/Input VALs & STRINGs ###

# ACCEPT USER INPUT
stringTrafficRaw = input("INPUT TRAFFIC LIGHT COLOR: ")

#Create stringTraffic from stringTrafficRaw
stringTraffic = stringTrafficRaw.lower()


#Create charTraffice from stringTraffic
charTraffic = stringTraffic[0:1]


##CALCs
if charTraffic == 'r':
   print("STOP")

elif charTraffic == "y":
   print("GET SET")

elif charTraffic == "g":
   print("GO")

else:
   print("Wrong Colour")
