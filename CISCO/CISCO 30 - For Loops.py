### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - For Loop Counter
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# FOR LOOP EXAMPLES
### OBJECTIVE ###


#####################
###     CODE      ###
#####################

### PRINT TIMES TABLE ###
for i in range (1,13):
   print(1*i, 2*i, 3*i, 4*i, 5*i, 6*i, 7*i, 8*i, 9*i, 10*i, 11*i, 12*i)

# PRINT TIMES TABLE - ENHANCED ###
for i in range(1,13):
    print(i, end="\t")
print("")
print("___________________________________________________________________________________________")

for j in range(1,13):
    for k in range(1,13): #NESTED LOOP
        print(j * k, end="\t")
    print("\n")

### PRINT THREE TIMES TABLE - STRING ###
for i in range (1, 15):
  print("3 times " + str(i) + " equals:", str(3*i))


# Print THREE TIMES TABLE
for i in range (1, 15):
   print(3*i)

# PRINT HELLO 11 TIMES
for i in range (10):
    print("Hello")

# PRINT USER NAME 100 TIMES
userName = input("What is your name?")
for i in range (1,100):
    print(userName)
