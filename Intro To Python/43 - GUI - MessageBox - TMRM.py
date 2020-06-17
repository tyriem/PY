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

#First, we import the messagebox library from tkinter
from tkinter import messagebox

##Declare/Input VALs & STRINGs


##CALCs


##OUTPUTs
 
window = Tk()
 
window.title("PYTHON APP: GUI - Message Box")
 
window.geometry('350x200')
 
def clicked():
 
    messagebox.showinfo('Message title', 'Message content')
 
btn = Button(window,text='Click here', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()





