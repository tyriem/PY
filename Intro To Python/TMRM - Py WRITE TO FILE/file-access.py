### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Classwork: Read & Write To File
### VER: 1.0
### DATE: 06-16-2020

############################
### READ & Write To TXT  ###
############################

### OBJECTIVE ###
# READ & WRITE TO FILE IN PYTHON
### OBJECTIVE ###


################################################
### 1.2.6.1: Read an External File

#TASK #1 - Open a blank script and save it as file-access.py
#DONE#


#TASK #2 - Create a script to read and print the content of a file
f= open("devices.txt", "r")
print(f.read())

#TASK #3 - The devices.txt file should be in the same directory as your script.
#DONE#

#TASK #4 - After printing the contents of the file, use the close() function to remove it from the computer's memory.
f.close()

################################################

### 1.2.6.2: Remove Blank Lines from the Output

#TASK #1 - Strip the blank lines from the output
file=open("devices.txt","r")
for item in file:
item=item.strip()
print(item)
file.close()

################################################

### 1.2.6.3: Copy File Content Into a List Variable

#TASK #1 - Create an empty list

devices=[]

#TASK #2 - Use the append parameter to copy file content to the new list.
file=open("devices.txt","r")
for item in file:
item=item.strip()
devices.append(item)
file.close()
print(devices)


#HW - Create a script to allow user to add devices










#DELETE THE CONTENTS OF FILE
#THIS WORKS BY OVERWRITING THE CONTENTS OF THE FILE
#f= open("test.txt", "w")

#Close the file
#f.close()

#WRITE TO THE FILE FROM WITHIN PYTHON
#f= open("test.txt", "w")
#f.write("I am a test file. \n")
#f.write("Maybe someday, he will promote me to a real file.\n")
#f.write("Man, I long to be a real file \n")
#f.write("and hang out with all my new real file friends. \n")
#f.write("OOPS, there goes the contents of your file. ")
#f.close()

#APPEND A LINE
#OPENS THE FILE WITH THE POINT OF APPENDING IT AT THE END
#f= open("test.txt", "a")
#f.write(" ...and can I get some pickles on that.")
#f.close()

### OUTPUTs ###

