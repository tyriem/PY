### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Lists: Colors
### VER: 1.0
### DATE: 06-10-2020

#####################
###     Lists     ###
#####################

### OBJECTIVE ###
#Make list of [yellow,red,blue,green, black];Output list, Access and Print out the Color: Yellow", append the color: Pink to the end of the list, Sort The List, Print The Length of the list, Insert The Color White at the beginning of the list
#Remove the first item in the list, Delete the color Black, Pop Last Item in The List, Remove The Index Value 1 from the list

### OBJECTIVE ###

##Declare LISTs


#1
print("Step 1: Make & Print The List")
color_list = ["yellow", "red", "blue", "green", "black"]
print(color_list)
#2
print("Step 2: Access The List and Print The Color Yellow")
print (color_list[0])
#3
print("Step 3: Append The Color Pink to the list")
color_list.append("pink")
print(color_list)
#4
print("Step 4: Sort The List")
color_list.sort()
print(color_list)
#5
print("Step 5: Print The Length Of The List")
print(len(color_list))
#6
print("Step 6: Add The Color White To the Beginning of The List")
color_list.insert(0,"white")
print(color_list)
#7
print("Step 7: Remove The First Item From The List")
color_list.pop(0)
print(color_list)
#8
print("Step 8: Remove The Color Black From The List")
color_list.remove("black")
print(color_list)
#9
print("Step 9: Pop The Last Element of the List")
color_list.pop(4)
print(color_list)
#10
print("Step 10: Remove The Element in Index Position 1 of The List")
color_list.pop(1)
print(color_list)
