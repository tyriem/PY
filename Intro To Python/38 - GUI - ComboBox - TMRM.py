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

#First, we import the ttk library
from tkinter.ttk import *

##Declare/Input VALs & STRINGs


##CALCs


##OUTPUTs
window = Tk()
 
window.title("PYTHON APP: GUI - COMBOBOX")
 
window.geometry('350x200')

#Second, we call the combobox up with the combo = ComboBox(window)declaration
combo = Combobox(window)

#Third, we set the values available in the combobox
combo['values']= (1, 2, 3, 4, 5, "Text")

#Fourth, we set the current value available that is pre-selected (in this case the first option as 0) 
combo.current(0) 

#Fifth, we set the grid and attach the combobox to it 
combo.grid(column=0, row=0)

#OPTIONAL: You can call up the currently selected option in the program with the following code: combo.get()
combo.get()
 
window.mainloop()





