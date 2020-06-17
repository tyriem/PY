### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Buttons
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
 
window = Tk()
 
window.title("PYTHON APP: GUI - BUTTONS")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")

#First we establish the grid upon which the button 
lbl.grid(column=0, row=0)

#Second we label the button with the target text 
btn = Button(window, text="Click Me")

#Third we attach the button to the grid 
btn.grid(column=1, row=0)
 
window.mainloop()


