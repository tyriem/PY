### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Window Size
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

##Declare/Input VALs & STRINGs


##CALCs


##OUTPUTs

window.title("PYTHON APP: GUI - WINDOW SIZE")
 
lbl = Label(window, text="Hello")

#The window.geometry call draws the GUI to a certain size
window.geometry('350x200')
 
lbl.grid(column=0, row=0)
 
window.mainloop()

