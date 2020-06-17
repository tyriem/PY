### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: CheckButton
### VER: 1.0
### DATE: 06-06-2020

#####################
###     GUIs      ###
#####################

### OBJECTIVE ###
#Code a basic GUI for user
#
### OBJECTIVE ###

##Declare CALLs & DEFs

from tkinter import*

#First, we import the ttk library
from tkinter.ttk import *

##Declare/Input VALs & STRINGs


##CALCs


##OUTPUTs

window = Tk()
 
window.title("PYTHON APP: GUI - CHECKBUTTON")
 
window.geometry('350x200')

#First, We set the Check state in this case as a Bool Variable 
chk_state = BooleanVar()

#Second, we set the check state
chk_state.set(True) 

#Third we present the user with the check button and label it with text
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
 
window.mainloop()






