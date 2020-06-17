### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Write To File
### VER: 1.0
### DATE: 06-16-2020

#####################
### READ FROM TXT ###
#####################

### OBJECTIVE ###
# READ FROM FILE IN PYTHON
### OBJECTIVE ###



### CALLs ###



### CMDs ###

#Opens file with name of "test.txt" in the same directory
f= open("test.txt", "r")




### OUTPUTs ###

##READING FROM YOUR FILE
#file.read(n) - This methods reads n number of characters from the file, or if n is empty it reads the entire file
#file.readline(n) - This method reads an entire line from the text file

#Task: PRINT the first character of the file
print(f.read(1))

#Task: PRINT the first 5 characters of the file
print(f.read(5))

#Task: PRINT the file
print(f.read())

#Task: PRINT all the lines of the file using a FOR Loop
for x in f:
  print(x)

#Task: Enter the information in the list
myList=[]
for line in f:
   myList.append(line)
print(myList)

#NB: REMEMBER TO CLOSE THE FILE AT THE END TO NOT HAVE ISSUES WITH THE MEMORY BUFFER
f.close()



