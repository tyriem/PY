### AUTHOR: TMRM   
### PROJECT: My Information Is - Concatenation
### VER: 1.0
### DATE: 05-12-2020

#Declare CALLs

#Declare STRINGs
name= input("Please enter your name")
age= int(input("Please enter your age"))
RAWphone=(input("Please enter phone number"))
phone= int(RAWphone.replace("-",""))
space = ' '


#OUTPUT
### At this stage we concatenate (merge/join together) the above into a sentence
### You cannot concatenate a string and an int together
### You must convert ints to strings to add them together
print("My name is" + space + name + space + "I am" + space + "years" + space + str(age) + space + "my phone number is" + space + str(phone))
