### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Greetings
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Write a program that:-
# Ask user to enter a grade.
# If grade is >= 90, display +, else if grade >= 80, display A,
# else if grade >= 70, display B, else if grade >= 60, display C, else display fail.
### OBJECTIVE ###

# Print the program title
print('''
#####################
###     Grade     ###
###      Eval     ### 
#####################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs


##Declare/Input VALs & STRINGs


raw_grade = input("Input The Grade To Be Evaluated: ")
grade = int(raw_grade.replace("%",""))

##CALCs & OUTPUTS

if grade >= 90:
   print("You Have A Passing Grade Of A+")

elif grade >= 80:
   print("You Have A Passing Grade Of A")

elif grade >= 70:
   print("You Have A Passing Grade Of B")

elif grade >= 60:
   print("You Have A Failing Grade Of C") 

else:
   print("You Have A Failing Grade of F")


