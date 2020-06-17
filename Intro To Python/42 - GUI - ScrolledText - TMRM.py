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


from tkinter.ttk import *

#First, we import the scrolledtext library from tkinter
from tkinter import scrolledtext 

##Declare/Input VALs & STRINGs


##CALCs


##OUTPUTs
 
window = Tk()
 
window.title("PYTHON APP: GUI - Scrolled Text")
 
window.geometry('350x200')


#Second, issue the scrolledText class and then define it 
txt = scrolledtext.ScrolledText(window,width=40,height=10)

#OPTIONAL: You can set scrolledText content with txt.insert
txt.insert(INSERT,'You text goes here')

#OPTIONAL: Delete/Clear scrolledText content
txt.delete(1.0,END)

txt.grid(column=0,row=0)
 
window.mainloop()




