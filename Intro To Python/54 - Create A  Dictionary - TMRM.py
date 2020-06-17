### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Lists: Colors
### VER: 1.0
### DATE: 06-10-2020

#####################
###   Dictionary  ###
#####################

### OBJECTIVE ###
# Make a dictionary of 4 pairs of descriptive values
# for a car and manipulate the dictionary
### OBJECTIVE ###

##Declare DICTs
# key : value,
car_dict = {
    "type": "lexus",
    "year": "2000",
    "model": "windom",
    "color": "emerald",
}
print(car_dict)

#Access an item by referencing its key name and print it
print("-------------------------------")
a = car_dict["color"]
print(a)

# Use get() to do the same as above
print("-------------------------------")
b = car_dict.get("color")
print(b)

# Change the year of the car to 2018
print("-------------------------------")
car_dict["year"] = 2018
print(car_dict)

# Print the key of the list
print("-------------------------------")
for key, value in car_dict.items() :
    print (key)

# Print the value of the list
print("-------------------------------")
for key, value in car_dict.items() :
    print (value)

#Check if a key exists in a dictionary
print("-------------------------------")
if 'year' in car_dict.keys():
  print("YEAR is present in the database")
else:
  print("YEAR not found")

# Check if a value exists in a dictionary
print("-------------------------------")
if 'emerald' in car_dict.values():
  print("EMERALD is present in the database")
else:
  print("EMERALD not found")


#Add an item to your dictionary
print("-------------------------------")
car_dict["config"] = "sedan"
print(car_dict)

#Print the length 
print("-------------------------------")
print("Items in Dictionary: ", len(car_dict))

#Clear the dictionary
car_dict.clear()
print(car_dict)

#Delete a dictionary
del(car_dict)
print(car_dict)
