### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Button Formatting
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
 
window.title("PYTHON APP: GUI - BUTTON FORMATTING")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")


lbl.grid(column=0, row=0)

#We alter the btn = command after the text = field to set the background color (bg=) and foreground button (fg=)
btn = Button(window, text="Click Me", bg="orange", fg="red")

#Third we attach the button to the grid 
btn.grid(column=1, row=0)
 
window.mainloop()


