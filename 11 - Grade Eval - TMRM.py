### AUTHOR: TMRM   
### PROJECT:INTRO TO PYTHON - Grade Evaluation - IF,ELSE,ELIF STATEMENT 
### VER: 1.0
### DATE: 05-21-2020

##Declare CALLs


##Declare/Input VALs & STRINGs


raw_grade = input("Input The Grade To Be Evaluated: ")
grade = int(raw_grade.replace("%",""))

##CALCs & OUTPUTS

if grade >= 90:
   print("You Have A Passing Grade Of A")

elif grade >= 80:
   print("You Have A Passing Grade Of B")

elif grade >= 70:
   print("You Have A Passing Grade Of C")

elif grade >= 65:
   print("You Have A Failing Grade Of D") 

else:
   print("You Have A Failing Grade of F")


