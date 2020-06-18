### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - TRIVIA GENERATOR
### VER: 1.2
### DATE: 06-16-2020

### Declare CALLs ###


### INSTALL REQUESTS ###
"""
import subprocess
import sys


def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
"""
### CALL REQUESTS ###
import time
import random
import turtle
from tkinter import *
from tkinter.ttk import *

def selected():
    x = radiovar.get()    

## Submit Button
def clicked():
    
    
    import requests
    import json
    lb2.configure(text="")
    lb3.configure(text="")
    lb4.configure(text="")
    cat_combo.destroy()
    amount_combo.destroy()
    diff_combo.destroy()
    lbl.configure(text="LET'S GO")
    print(amount)
    print(cat)
    print(diff)
    #SET COMPATIBLE PARAMS FOR WEBSITE
    params = (('amount', amount),('category', cat),('difficulty', diff),('type', 'multiple'),)
    ## SEND PARAMS TO WEBSITE WITH REQUESTS
    r = requests.get('https://opentdb.com/api.php?', params = params)
    ## CLEANING THE TEXT
    pretty_json = json.loads(r.text)
    # print (json.dumps(pretty_json, indent=2))
    # print(pretty_json['results'])
    quiz = (pretty_json['results'])
    print ("\n ---------------------------------------------------------")
    print (type(quiz))
    print (quiz)
    #Print the First Category Chosen
    print (quiz[0]['category'])
    #Print the First Question Generated
    print (quiz[0]['question'])
    #The First Question's Possible Answers
    #CORRECT ANSWER
    #print (quiz[0]['correct_answer'])
    #LIST OF WRONG ANSWERS
    #print (quiz[0]['incorrect_answers'])
    #WRONG ANSWERS
    #print (quiz[0]['incorrect_answers'][0])
    #print (quiz[0]['incorrect_answers'][1])
    #print (quiz[0]['incorrect_answers'][2])
    #Print the Second Category Chosen
    #print (quiz[1]['category'])
    print ("---------------------------------------------------------")
    answer_list = [(quiz[0]['correct_answer']), (quiz[0]['incorrect_answers'][0]), (quiz[0]['incorrect_answers'][1]), (quiz[0]['incorrect_answers'][2])]
    #randomly arrange answers
    random.shuffle(answer_list)
    print (answer_list)
    #Radio Button Logic
    lb5 = Label(window, text="Select Your Answer: ")
    lb5.grid(column=10, row=0)
    rad1 = Radiobutton(window,text= answer_list[0], indicatoron = 0, value= answer_list[0], command=selected) 
    rad2 = Radiobutton(window,text= answer_list[1], indicatoron = 0, value= answer_list[1], command=selected)
    rad3 = Radiobutton(window,text= answer_list[2], indicatoron = 0, value= answer_list[2], command=selected)
    rad4 = Radiobutton(window,text= answer_list[3], indicatoron = 0, value= answer_list[3], command=selected)  
    rad1.grid(column=11, row=0)
    rad2.grid(column=12, row=0)
    rad3.grid(column=13, row=0)
    rad3.grid(column=14, row=0)
    btn2 = Button(window, text="SUBMIT ANSWER", command=check)
    btn2.grid(column=15, row=0)


def checked():

    print(selected.get())
    #GUESS RESOLUTION LOGIC
    if selected.get() == quiz[0]['correct_answer']:
       print ("Congratulations!")
       score = score + 1




### GUI WORKSPACE ### 
window = Tk()
 
window.title("OPEN QUIZ")
 
window.geometry('1920x1080')

window.config(background="#ffffff")

window.resizable(0,0)

lbl = Label(window, text="Hello, and welcome to OPEN QUIZ")
 
lbl.grid(column=0, row=0)


#Question Selector

lb2 = Label(window, text="How many questions would you like? ")
 
lb2.grid(column=1, row=0)

 
amount_combo = Combobox(window)
 
amount_combo['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 
amount_combo.current(0) #set the selected item
 
amount_combo.grid(column=2, row=0)

amount = amount_combo.get()

#Category Selector
lb3 = Label(window, text="What Category of Question would you like? ")
 
lb3.grid(column=3, row=0)

 
cat_combo = Combobox()
 
cat_combo['values']= ("General Knowledge", "Books", "Film", "Music", "Musicals & Theatre", "Television", "Video Games", "Board Games", "Nature", "Computers", "Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals")

cat_combo.current(0) #set the selected item
 
cat_combo.grid(column=4, row=0)

cat_raw = cat_combo.get()

## CONVERT CAT_RAW TO CAT

if cat_raw == 'General Knowledge':
	cat = 9	
elif cat_raw == 'Books':
	cat = 10
elif cat_raw == 'Film':
	cat = 11
elif cat_raw == 'Music':
	cat = 12
elif cat_raw == 'Musicals & Theatre':
	cat = 13
elif cat_raw == 'Television':
	cat = 14
elif cat_raw == 'Video Games':
	cat = 15
elif cat_raw == 'Board Games':
	cat = 16
elif cat_raw == 'Nature':
	cat = 17
elif cat_raw == 'Computers':
	cat = 18
elif cat_raw == 'Mathematics':
	cat = 19
elif cat_raw == 'Mythology':
	cat = 20
elif cat_raw == 'Sports':
	cat = 21
elif cat_raw == 'Geography':
	cat = 22
elif cat_raw == 'History':
	cat = 23
elif cat_raw == 'Politics':
	cat = 24
elif cat_raw == 'Art':
	cat = 25
elif cat_raw == 'Celebrities':
	cat = 26
elif cat_raw == 'Animals':
	cat = 27


#Difficulty Selector

lb4 = Label(window, text="What difficulty of question would you like? ")
 
lb4.grid(column=5, row=0)

 
diff_combo = Combobox(window)
 
diff_combo['values']= ("Easy", "Medium", "Hard")
 
diff_combo.current(0) #set the selected item
 
diff_combo.grid(column=6, row=0)

diff = diff_combo.get()


btn1 = Button(window, text="START QUIZ", command=clicked)
 
btn1.grid(column=7, row=0)




### CLOSE OUT GUI
window.mainloop()

"""
####################################
# TURTLE CMDs
##OUTPUTs




t = turtle.Turtle(window)
#TURTLE: RED LETTER E

t.color("red")

t.down()

t.begin_fill()

t.forward(100)

t.right(90)

t.forward(30)

t.right(90)

t.forward(100)

t.left(90)

t.forward(50)

t.left(90)

t.forward(100)

t.right(90)

t.forward(30)

t.right(90)

t.forward(100)

t.left(90)
t.forward(50)

t.left(90)

t.forward(100)

t.right(90)

t.forward(30)

t.right(90)

t.forward(130)

t.right(90)

t.forward(190)

t.right(90)

t.forward(130)

t.end_fill()

t.up()

turtle.done()

####################################
"""


