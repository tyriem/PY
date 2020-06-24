### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - OS: File Structure
### VER: 1.0
### DATE: 06-23-2020

############################
### OS - File Structure  ###
############################

### OBJECTIVE ###
# PRINT THE FILE STRUCTURE
### OBJECTIVE ###


import os

currentDirectoryPath = os.getcwd()

listofFileNames = os.listdir(currentDirectoryPath)

for name in listofFileNames:

     if ".py" in name:

          print(name)

