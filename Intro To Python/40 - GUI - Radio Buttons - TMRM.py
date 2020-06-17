### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Radio Buttons
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
 
window.title("PYTHON APP: GUI - RADIO BUTTONS")
 
window.geometry('350x200')

#First, we set the Radio Buttons with its Displayed text and value 
rad1 = Radiobutton(window,text='First', value=1)

 
rad2 = Radiobutton(window,text='Second', value=2)
 
rad3 = Radiobutton(window,text='Third', value=3)

#Second, we set the display of the radio buttons on the grid space
rad1.grid(column=0, row=0)
 
rad2.grid(column=1, row=0)
 
rad3.grid(column=2, row=0)


 
window.mainloop()







