### AUTHOR: TMRM
### CONTRIBUTORS:  
### PROJECT: MIT COURSEWARE - STRING EVAL - VOWELS
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5
### OBJECTIVE ###


### IMPORTs, INITs & DEFs ###

s = 'azcbobobegghakl'
numVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1

print('Number of vowels is: ' + str(numVowels))


