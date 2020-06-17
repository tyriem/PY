### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Button To Action
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
 
window.title("PYTHON APP: GUI - BUTTON TO ACTION")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)

#Here we define a function with an outcome
def clicked():
 
    lbl.configure(text="Button was clicked !!")
#Next we attach the function to the button click with the command=
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()



