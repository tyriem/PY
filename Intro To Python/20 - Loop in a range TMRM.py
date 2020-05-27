### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Loops, Breaks, Continues
### VER: 1.0
### DATE: 05-XX-2020

##Declare CALLs

number = 0
##Declare/Input VALs & STRINGs
#Range being evaluated
numbers = [
951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544
]

for number in number:
    if number == 544:
        break

    if number % 2 == 0:
        continue
    
    print(number)
 
