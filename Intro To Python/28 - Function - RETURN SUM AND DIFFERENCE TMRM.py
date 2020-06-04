### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Function Return SUM AND DIFFERENCE
### VER: 1.0
### DATE: 05-XX-2020

#####################
### RETURN VALUES ###
#####################

### OBJECTIVE ###
# USE FUNCTIONS TO FIND THE SUM OF TWO NUMBERS AND THEN THE DIFFERENCE OF TWO OTHER NUMBERS
### OBJECTIVE ###

##DECLARE Functions & Relationships

# To let a function return a value, use the return statement

def add_function(a,b):
    return a + b

def sub_function(a,b):
    return a - b

def neg_sub_function(a,b):
    return b - a

##USER INPUT, VAR ASSIGNMENT, CALC

# SUM #
a = int((input("ENTER THE FIRST NUMBER: ")))
b = int((input("ENTER THE SECOND NUMBER: ")))
print("THE SUM OF THE FIRST AND SECOND NUMBER IS: ",(add_function(a,b)))

# DIFFERENCE #
if a >= b:
   print("THE DIFFERENCE OF THE FIRST AND SECOND NUMBER IS: ",(sub_function(a,b)))
else:
   print("THE DIFFERENCE OF THE FIRST AND SECOND NUMBER IS: ",(neg_sub_function(a,b)))



