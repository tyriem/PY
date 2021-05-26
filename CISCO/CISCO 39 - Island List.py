### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - ISLAND LIST
### VER: 1.0
### DATE: 05-XX-2021

#####################
###     CODE      ###
#####################

### OBJECTIVE ###
# Create 4 lists that outlines the islands of The Bahamas based on the area that they fall in. 
# Print each list of Bahamian island. Then print each list in alphabetical order.
### OBJECTIVE ###

### Declare CALLs & DEFs ###


### Declare/Input VALs & LISTs ###
islandAreaENW = ["Bimini", "Grand Bahama", "Abaco (North)"]
islandAreaNW = ["Abaco (South)", "Andros", "Berry Islands", "Eleuthera", "New Providence"]
islandAreaC = ["Cat Island", "Exuma", "Long Island", "Rum Cay"]
islandAreaSE = ["Acklins", "Crooked Island", "Inagua", "Mayaguana", "Ragged Island"]

### OUTPUT LISTS ###
print("Extreme North-West Bahamas Islands: ", islandAreaENW)
print("North-West Bahamas Islands: ", islandAreaNW)
print("Central Bahamas Islands: ", islandAreaC)
print("South-East Bahamas Islands: ", islandAreaSE)

### SORT LISTS ###
islandAreaENW.sort()
islandAreaNW.sort()
islandAreaC.sort()
islandAreaSE.sort()

### OUTPUT LISTS ###
print("-----------------------")
print("IN ALPHABETICAL ORDER: ")
print("Extreme North-West Bahamas Islands: ", islandAreaENW)
print("North-West Bahamas Islands: ", islandAreaNW)
print("Central Bahamas Islands: ", islandAreaC)
print("South-East Bahamas Islands: ", islandAreaSE)







