### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Team Evaluator
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
### OBJECTIVE ###

# Print the program title
print('''
####################
###      Team     ###
###      Eval    ### 
####################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs


##Declare/Input VALs & STRINGs

# ACCEPT USER INPUT
stringTeamRaw = input("INPUT TEAM NAME: ")

#Create stringTeam from stringTeamRaw
stringTeam = stringTeamRaw.lower()


#Create charTeam from stringTeam
charTeam = stringTeam[0:1]


##CALCs
if charTeam == 'c':
   print("BLUE")

elif charTeam == 'l':
   print("RED")

else:
   print("Team Not Registered")


