### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Digital Clock
### VER: 1.0
### DATE: 06-09-2020

#####################
###  DIGI CLOCK   ###
#####################

### OBJECTIVE ###
# CREATE A GUI THAT DRAWS A DIGITAL CLOCK
### OBJECTIVE ###

### Declare CALLs & DEFs ###


from tkinter import * 
from tkinter.ttk import *
  
 
# IMPORT STRFTIME FROM TIME FOR SYS TIME
from time import strftime 
  

### OUTPUTs ###


# creating tkinter window 
root = Tk() 
root.title('Digital Clock') 
  
# This function is used to  
# display time on the label 
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(root, font = ('arial', 40, 'bold'), 
            background = 'green', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 
