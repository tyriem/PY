### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Lists: Colors
### VER: 1.0
### DATE: 06-10-2020

#####################
###   Dictionary  ###
#####################

### OBJECTIVE ###
# Make a dictionary of fruits and their colors
### OBJECTIVE ###

##Declare LISTs
thisdict = {
    "apple": "green",
    "banana": "yellow",
    "cherry": "red",
}
print(thisdict)

##You can also use the constructor to make a dictionary:
##thisdict = dict(apple="green", banana="yellow", cherry="red")


# Change the color of the apple

thisdict["apple"] = "red"
print(thisdict)

# Add an item

thisdict["grape"] = "purple"
print(thisdict)

# Remove an item
del(thisdict["banana"])
print(thisdict)

# Length of Dictionary
print(len(thisdict))


