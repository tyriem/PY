### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Dictionary: Manipulate A Dictionary
### VER: 1.0
### DATE: 06-15-2020

#####################
###   Dictionary  ###
#####################

### OBJECTIVE ###
# Make and manipulate a dictionary of months
### OBJECTIVE ###

##Step #1 - Declare DICT
month_dict = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
##Step #2 - Print DICT
print(month_dict)


##Step #3 - Print the key of the list
print("-------------------------------")
for key, value in month_dict.items() :
    print (key)

##Step #4 - Delete the Fifth Element, print the keys
print("-------------------------------")

month_dict.pop("5")
print(month_dict)


for key, value in month_dict.items() :
    print (key)

##Step #5 - Update an element of a dictionary, assign a new value to its key,
##that is “Jan” to replace “January”, print output.   
print("-------------------------------")
month_dict["1"] = "Jan"
print(month_dict)

##Step #6 - Print the length of the dict
print("-------------------------------")
print("Items in Dictionary: ", len(month_dict))

##Step #7 - Print out the months: July, August and September in one line.
print("-------------------------------")
print(month_dict["7"], month_dict["8"], month_dict["9"])
print('{} {} {}'.format(month_dict["7"], month_dict["8"], month_dict["9"]))


