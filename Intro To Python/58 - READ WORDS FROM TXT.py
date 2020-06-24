### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - OS: File Structure
### VER: 1.0
### DATE: 06-23-2020

############################
### OS - File Structure  ###
############################

### OBJECTIVE ###
# Write a code segment that opens a file for input
# and prints the number of four-letter words in the file.
### OBJECTIVE ###


### IMPORTS ###
#Opens file with name of "demofile.txt" in the same directory

f = open("demofile.txt", "r")
for s in f:
  print(s)
  words = s.split()
  count = 0
  for word in words:
      if len(word) == 4:
         count += 1
  print("Amount of four letter words: ",count)

"""
[MORE THAN FOUR LETTERS]
f = open("demofile.txt", "r")
for s in f:
  print(s)
  words = s.split()
  count = 0
  for word in words:
      if len(word) >= 4:
         count += 1
  print("Amount of four letter (or more) words: ",count)

"""
