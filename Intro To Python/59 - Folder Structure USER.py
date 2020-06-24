### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - OS: File Structure
### VER: 1.0
### DATE: 06-23-2020

############################
### OS - File Structure  ###
############################

### OBJECTIVE ###
# Write a code segment that prompts the user for a filename.
# If the file exists, the program should print its  contents on the terminal.
# Otherwise, it should print an error message. 
### OBJECTIVE ###


import os
counter = 0
file= input("TYPE THE NAME OF THE FILE YOU WOULD LIKE TO SEARCH FOR: ")

currentDirectoryPath = os.getcwd()

listofFileNames = os.listdir(currentDirectoryPath)


      

for name in listofFileNames:

     if file in name:
          print(name)
          counter = counter + 1
          f = open(name, "r")
          for s in f:
            print(s)                   
if counter == 0:
             print("ERROR")         
     



