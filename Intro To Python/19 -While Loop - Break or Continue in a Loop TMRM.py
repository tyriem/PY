### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - break and continue Display Odd Numbers
### VER: 1.0
### DATE: 05-XX-2020

##Declare CALLs


##Declare/Input VALs & STRINGs

#Prints out 0,1,2,3,4
count = 0
while true:
    print(count)
    count += 1
    if count <= 5:
        break

#Prints out only odd number - 1,3,5,7,9
for x in range(10):
    #Check if x is even
    if x % 2 == 0:
        continue
    print
