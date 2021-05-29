### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - LOOPs - UNIQUE LIST
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Your task is to write a program which removes all the number repetitions from the list.
# The goal is to have a list in which all the numbers appear not more than once.
### OBJECTIVE ###

#####################
###     CODE      ###
#####################

# Print the program title
print('''
######################
###      RANGE     ###
######################
''')

### VARs & DEFs ###
# The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: 
# range(start, stop, step), where:
#
# start is an optional parameter specifying the starting number of the sequence (0 by default)
# stop is an optional parameter specifying the end of the sequence generated (it is not included),
# and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)

### EXAMPLE CODE ###
#for i in range(3):
#    print(i, end=" ")  # Outputs: 0 1 2
#
#for i in range(6, 1, -2):
#    print(i, end=" ")  # Outputs: 6, 4, 2
### EXAMPLE CODE ###  

print("OUTPUT #1:")
for i in range(15):    # PARAM END RANGE: 15
    print(i, end=" ")  # Outputs:  0 - 14 
    
    
print("\n---------------------------------------")


print("OUTPUT #2:")    
for i in range(10,200): # PARAM START PARAM: 10 | PARAM END RANGE: 200
    print(i, end=" ")   # Outputs:  10 - 199
   
    
print("\n---------------------------------------")
    
   
print("OUTPUT #3:") 
for i in range(1,4,2): # PARAM START PARAM: 1 | PARAM END RANGE: 4 | PARAM STEP: 2
   print(i, end=" ")   # Outputs: 1,3 

   
    
print("\n---------------------------------------")
    
   
print("OUTPUT #4:") 
for i in range(500,2,-5): # PARAM START PARAM: 500 | PARAM END RANGE: 2 | PARAM STEP: -5
   print(i, end=" ")      # Outputs:  500,495,490,485,480.....5   [2]
    
    
