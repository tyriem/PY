### AUTHOR: TMRM
### CONTRIBUTORS:   
### PROJECT: CISCO DevNet - MEDIA ACCESS - ALIEN
### VER: 1.0
### DATE: 06-XX-2021

### OBJECTIVE ###
#Make a GUI that controls an image of an alien appearing and disappearing
### OBJECTIVE ###

print('''
####################
###     ALIEN    ###
###     MEDIA    ###  
####################
''')

### Declare CALLs & DEFs ###

from tkinter import*

root = Tk()
root.title("Welcome To Earth!")
root.geometry('800x600-5+40')

def showAlien():           
    labelImg.pack()

def hideAlien():
    labelImg.pack_forget()

def buttonQuit():
    root.destroy()


### BUTTON LOGIC ###

buttonON = Button(root, text="Show", width=5, height=2, command=showAlien)
buttonON.pack(side=LEFT) #tell tkinter to put objects in one row

buttonOFF = Button(root, text="Hide", width=5, height=2, command=hideAlien)
buttonOFF.pack(side=LEFT) #tell tkinter to put objects in one row

buttonQUIT = Button(root, text="E.T. GO HOME!", width=10, height=2, command=buttonQuit)
buttonQUIT.pack(side=LEFT) #tell tkinter to put objects in one row

### IMAGE LOGIC ###
img = PhotoImage(file='alien.png')
labelImg = Label(image=img)
labelImg.image = img
labelImg.pack()

root.mainloop()

