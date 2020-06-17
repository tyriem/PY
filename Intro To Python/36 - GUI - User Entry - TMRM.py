### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: User Input Field
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
 
window.title("PYTHON APP: GUI - USER INPUT FIELD")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)

#Here we set an entry field for user input with the text = call 
txt = Entry(window,width=10)

#OPTIONAL: Here we set the point of focus on the user input field so that you can type once the program launches
txt.focus()
 
txt.grid(column=1, row=0)
 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()




