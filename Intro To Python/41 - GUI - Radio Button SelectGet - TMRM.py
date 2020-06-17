### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Radio Buttons Select & Get
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
 
window.title("PYTHON APP: GUI - RADIO BUTTONS SELECT & GET")
 
#First, we issue the selected = IntVar() 
selected = IntVar()
 
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
 
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
 
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
 
 #Second, we define a function for clicked
def clicked():
 
   print(selected.get())
 
btn = Button(window, text="Click Me", command=clicked)
 
rad1.grid(column=0, row=0)
 
rad2.grid(column=1, row=0)
 
rad3.grid(column=2, row=0)
 
btn.grid(column=3, row=0)
 
window.mainloop()



