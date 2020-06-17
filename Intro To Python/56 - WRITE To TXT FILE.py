### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Write To File
### VER: 1.0
### DATE: 06-16-2020

#####################
### Write To TXT  ###
#####################

### OBJECTIVE ###
# WRITE TO FILE IN PYTHON
### OBJECTIVE ###



### CALLs ###



### CMDs ###

#DELETE THE CONTENTS OF FILE
#THIS WORKS BY OVERWRITING THE CONTENTS OF THE FILE
f= open("delete.txt", "w")

#Close the file
f.close()

#WRITE TO THE FILE FROM WITHIN PYTHON
f= open("delete.txt", "w")
f.write("I am a test file. \n")
f.write("Maybe someday, he will promote me to a real file.\n")
f.write("Man, I long to be a real file \n")
f.write("and hang out with all my new real file friends. \n")
f.write("OOPS, there goes the contents of your file. ")
f.close()

#APPEND A LINE
#OPENS THE FILE WITH THE POINT OF APPENDING IT AT THE END
f= open("delete.txt", "a")
f.write(" ...and can I get some pickles on that.")
f.close()

### OUTPUTs ###

