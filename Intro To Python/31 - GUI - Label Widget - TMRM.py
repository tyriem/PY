### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - GUI: Label Widget
### VER: 1.0
### DATE: 05-XX-2020

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

# To add a label to our previous example, we will create a label using the label class like this:
# lbl = Label(window, text="Hello")
#Then we will set its position on the form using the grid function and give it the location like this:
#lbl.grid(column=0, row=0)


##CALCs


##OUTPUTs

window = Tk()

#Title The Window 
window.title("PYTHON APP: GUI - LABEL WIDGET")

#Label The Window
lbl = Label(window, text="Hello")

#To format the text of the label use: , =font=("INSERT FONT HERE", INSERT FONT SIZE HERE))
#lb1 = Label(window, text="LARGER TEXT", font=("Arial Bold", 50))

#Draw the borders of the window 
lbl.grid(column=0, row=0)

#Attach the window to the main  
window.mainloop()


