### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Loops, Breaks, Continues
### VER: 1.0
### DATE: 05-26-2020

##Declare CALLs


##Declare/Input VALs & STRINGs
#Range being evaluated
number_list = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544]

#COUNT OUT THE EVEN NUMBERS
count = 0
for number_even in number_list:
    if number_list == 544:
        break

    if number_even % 2 == 1:
        continue
    
    count = count + 1
    print(number_even)
    
print("The Even Count is: ", count)
    
#COUNT OUT THE ODD NUMBERS

count = 0
for number_odd in number_list:
    if number_list == 544:
        break

    if number_odd % 2 == 0:
        continue
    
    count = count + 1
    print(number_odd)
    
print ("The Odd Count is: ", count)

#COUNT OUT ALL NUMBERS
total = len(number_list)
print ("-----------------------------")
print ("The Total Count is: ", total)
