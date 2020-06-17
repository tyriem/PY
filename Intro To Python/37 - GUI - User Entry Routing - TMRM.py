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
 
window.title("PYTHON APP: GUI - USER INPUT ENTRY FIELD")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)

#OPTIONAL: To disable the entry widget we add the property state= and set it to 'disabled'
# txt = Entry(window,width=10, state='disabled')

txt.grid(column=1, row=0)
 
def clicked():

#Here we attach the user input field established in txt= and then output it with a preamble using the res= and lbl.configure(text = res) function
    res = "Welcome to " + txt.get()
 
    lbl.configure(text= res)
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()





