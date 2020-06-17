### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Lists
### VER: 1.0
### DATE: 06-10-2020

#####################
###     Lists     ###
#####################

### OBJECTIVE ###
#Create and print a list of fruits
#
### OBJECTIVE ###

##Declare LISTs

thislist = ["apple", "banana", "cherry", "orange", "strawberry"]

#This changes the second item in the list, the value in the [] determines what is changed based on index location (starting at 0)
thislist[1] = "blackberry"

#This appends a new item to the list
thislist.append("grape")

#This reomves an item from the list
thislist.remove("cherry")

##OUTPUTs
#Prints the list
print(thislist)
#Prints the amount of items in the list
print(len(thislist))

#Reverses the order of the list
thislist.reverse()
print(thislist)

#Sorts the list alphanumerically
thislist.sort()
print(thislist)

print(thislist.index("apple"))
