### IMPORTs ###
#Import TKInter GUI Engine
import tkinter as tk
import tkinter.ttk as ttk
#Import REQs web module
import requests
#Import JSON Processor
import json
#Import SYSTime
import time
#Import Random Generator
import random
#Import Turtle Drawer
import turtle

### CALLs ###

#Draw initial window
window = tk.Tk()
window.geometry("1280x550")
window.title("QUIZ")
window.grid_columnconfigure(0, weight=1)

### VARs ###
var_one = tk.StringVar()
var_two = tk.StringVar()
scoreOneInt = 0
scoreTwoInt = 0

questInt = 0
selection_one = 0
selection_two = 0

      

### FUNCTIONs ###

#FUNC to select P1 radio button
def selected_one():
    global selection_one
    selection_one = str(var_one.get())

#FUNC to select P2 radio button
def selected_two():
    global selection_two
    selection_two = str(var_two.get())

#FUNC to post the question for the players
def start_quiz():

    global name_one
    global name_two
    name_one = name_one_input.get()
    name_two = name_two_input.get()

    global player_one_window
    player_one_window = tk.Toplevel(window)
    p1_label = tk.Label(player_one_window, text = ("Player One: ", str(name_one)))
    player_one_window.geometry("600x550+0+600")
    player_one_window.title("Player One")
    player_one_window.grid_columnconfigure(0, weight=1)

    global player_two_window
    player_two_window = tk.Toplevel(window)
    p2_label = tk.Label(player_two_window, text = ("Player Two: ", str(name_two)))
    player_two_window.geometry("600x550+600+600")
    player_two_window.title("Player Two")
    player_two_window.grid_columnconfigure(0, weight=1)
    ## CONVERT CAT_RAW TO CAT
    cat_raw = cat_combo.get()
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
    ## CONVERT DIFF_RAW TO DIFF
    diff_raw = diff_combo.get()
    if diff_raw == 'Easy':
        diff = 'easy'
    elif diff_raw == 'Normal':
          diff = 'medium'
    elif diff_raw == 'Hard':
          diff = 'hard'
    # SET AMOUNT OF Qs
    global amount
    amount = int(amount_combo.get())
    # DELIVER PAYLOAD TO API
    print(amount)
    print(cat)
    print(diff)
    payload = {'amount' : '1', 'category' : cat, 'difficulty' : diff, 'type' : 'multiple'}
    response = requests.get("https://opentdb.com/api.php?", params=payload)
    # FORMAT THE API RESPONSE
    global text_response
    text_response = response.text
    global text_proc
    text_proc = text_response.replace('&quot;', " ' ").replace('&#039;', " ' ").replace('&rsquo;', " ' ").replace('&shy;', ' - ').replace('&ouml;', ' o ')
    # CLEAR THE WINDOW
    lb1.configure(text="")
    lb2.configure(text="")
    lb3.configure(text="")
    playerone_label.grid_forget()
    playertwo_label.grid_forget()
    name_one_input.grid_forget()
    name_two_input.grid_forget()
    cat_combo.grid_forget()
    amount_combo.grid_forget()
    diff_combo.grid_forget()
    start_button.grid_forget()
    pretty_json = json.loads(str(text_proc))
    global quiz
    quiz = (pretty_json['results'])
    print ("\n ---------------------------------------------------------")
    print (type(quiz))
    print (quiz)
    #Print the Category Chosen
    print (quiz[0]['category'])
    #Print the Question Generated
    print (quiz[0]['question'])
    #The Question's Possible Answers
    #CORRECT ANSWER
    #quiz[0]['correct_answer']
    #LIST OF WRONG ANSWERS
    #quiz[0]['incorrect_answers']
    #WRONG ANSWERS
    #quiz[0]['incorrect_answers'][0]
    #quiz[0]['incorrect_answers'][1]
    #quiz[0]['incorrect_answers'][2]
    print ("---------------------------------------------------------")
    answer_list = [(quiz[0]['correct_answer']), (quiz[0]['incorrect_answers'][0]), (quiz[0]['incorrect_answers'][1]), (quiz[0]['incorrect_answers'][2])]
    #Randomly arrange answers
    random.shuffle(answer_list)
    print (answer_list)
    #Question Display:
    global lb4
    lb4 = tk.Label(window, text=  quiz[0]['question'], font=("Helvetica", 18))        
    lb4.grid(row=9, column=0, sticky="WE", padx=10, pady=10)
    #Select Your Answer Prompt P1:
    lb5 = tk.Label(player_one_window, text="Select Your Answer: ")        
    lb5.grid(row=0, column=0, sticky="WE", padx=10, pady=10)
    #Radio Button Logic P1:
    global rad1
    rad1 = ttk.Radiobutton(player_one_window, text= answer_list[0], variable=var_one, value= answer_list[0], command=selected_one)
    rad1.grid(row=1, column=0, sticky="WE", padx=10, pady=10)
    var_one.set(0)
    global rad2
    rad2 = ttk.Radiobutton(player_one_window, text= answer_list[1], variable=var_one, value= answer_list[1], command=selected_one)
    rad2.grid(row=2, column=0, sticky="WE", padx=10, pady=10)
    global rad3
    rad3 = ttk.Radiobutton(player_one_window, text= answer_list[2], variable=var_one, value= answer_list[2], command=selected_one)
    rad3.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
    global rad4
    rad4 = ttk.Radiobutton(player_one_window, text= answer_list[3], variable=var_one, value= answer_list[3], command=selected_one)  
    rad4.grid(row=4, column=0, sticky="WE", padx=10, pady=10)
    var_one.set(1)

    #Select Your Answer Prompt P2:
    lb6 = tk.Label(player_two_window, text="Select Your Answer: ")        
    lb6.grid(row=0, column=0, sticky="WE", padx=10, pady=10)
    #Radio Button Logic P2:
    global rad5
    rad5 = ttk.Radiobutton(player_two_window, text= answer_list[0], variable=var_two, value= answer_list[0], command=selected_two)
    rad5.grid(row=1, column=0, sticky="WE", padx=10, pady=10)
    global rad6
    rad6 = ttk.Radiobutton(player_two_window, text= answer_list[1], variable=var_two, value= answer_list[1], command=selected_two)
    rad6.grid(row=2, column=0, sticky="WE", padx=10, pady=10)
    global rad7
    rad7 = ttk.Radiobutton(player_two_window, text= answer_list[2], variable=var_two, value= answer_list[2], command=selected_two)
    rad7.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
    global rad8
    rad8 = ttk.Radiobutton(player_two_window, text= answer_list[3], variable=var_two, value= answer_list[3], command=selected_two)  
    rad8.grid(row=4, column=0, sticky="WE", padx=10, pady=10)
    
    
    #SUBMIT Button Logic:
    global btn2
    btn2 = tk.Button(window, text="SUBMIT ANSWERS", command=combo)
    btn2.grid(row=10, column=0, sticky="WE", padx=10, pady=10)

# FUNC to check P1's Answer
def checked_one():
    print(amount)
    lb4.grid_forget()
    rad1.grid_forget()
    rad2.grid_forget()
    rad3.grid_forget()
    rad4.grid_forget()
    btn2.grid_forget()
    #GUESS RESOLUTION LOGIC
    if selection_one == 0:
       lb7 = tk.Label(window, text="Sorry Player One, You Didn't Answer The Question.")        
       lb7.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
       print ("Incorrect Answer Detected")
       global scoreOneInt
       print("Current Score: ",scoreOneInt)

    elif selection_one == str(quiz[0]['correct_answer']):
       lb7 = tk.Label(window, text="Great Job Player One, You Answered Correctly.")        
       lb7.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
       print ("Correct Answer Detected")
       scoreOneInt = scoreOneInt + 1
       print("Current Score: ",scoreOneInt)

    else:
       lb7 = tk.Label(window, text="Sorry Player One, You Answered Incorrectly.")        
       lb7.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
       print ("Incorrect Answer Detected")
       print("Current Score: ",scoreOneInt)

    lb8 = tk.Label(window, text=('PLAYER ONE SCORE: ', str(scoreOneInt)), font=("Helvetica", 20))        
    lb8.grid(row=19, column=0, sticky="WE", padx=10, pady=10)
    print("Incorrect Answer Detected")
    print("Current Score: ",scoreOneInt)
    player_one_window.destroy()

# FUNC to check P2's Answer
def checked_two():
    print(amount)
    lb4.grid_forget()
    rad5.grid_forget()
    rad6.grid_forget()
    rad7.grid_forget()
    rad8.grid_forget()
    #GUESS RESOLUTION LOGIC
    if selection_two == 0:
       lb7 = tk.Label(window, text="Sorry Player Two, You Didn't Answer The Question.")        
       lb7.grid(row=11, column=0, sticky="WE", padx=10, pady=10)
       print ("Incorrect Answer Detected")
       global scoreTwoInt
       print("P2 Current Score: ",scoreTwoInt)

    elif selection_two == str(quiz[0]['correct_answer']):
       lb7 = tk.Label(window, text="Great Job Player Two, You Answered Correctly.")        
       lb7.grid(row=11, column=0, sticky="WE", padx=10, pady=10)
       print ("Correct Answer Detected")
       scoreTwoInt = scoreTwoInt + 1
       print("P2 Current Score: ",scoreTwoInt)

    else:
       lb7 = tk.Label(window, text="Sorry Player Two, You Answered Incorrectly.")        
       lb7.grid(row=11, column=0, sticky="WE", padx=10, pady=10)
       print ("Incorrect Answer Detected")
       print("Current Score: ",scoreTwoInt)

    lb8 = tk.Label(window, text=('PLAYER TWO SCORE: ', str(scoreTwoInt)), font=("Helvetica", 20))        
    lb8.grid(row=20, column=0, sticky="WE", padx=10, pady=10)
    print("Incorrect Answer Detected")
    print("P2 Current Score: ",scoreTwoInt)
    player_two_window.destroy()

# Combined Function to issue the quiz start and iterate the checking funcs             
def combo():
    checked_one()
    checked_two()
    start_quiz()
    global questInt
    questInt = questInt + 1
    ###ENDGAME LOGIC###
    if int(questInt) == int(amount):
       print("END")
       window.destroy()
       #TURTLE Drawing
       canvas = tk.Canvas(master=None,width=900,height=550)
       canvas.pack()
       t = turtle.RawTurtle(canvas)
       t.hideturtle()
       t.up()
       t.right(90)
       t.forward(20)
       t.down()
       #canvas.create_rectangle(900, 550, 0, 0, fill="black")
       t.color('black')
       style = ('Courier', 50, 'bold')
       t.write('THANKS FOR PLAYING', font=style, align='center')
       t.up()
       t.forward(60)
       t.down()
       t.color('blue')
       style = ('Courier', 20, 'bold')
       t.write('PlAYER ONE: ' + (str(name_one) + ' SCORE: ' + str(scoreOneInt)), font=style, align='center')
       t.up()
       t.forward(30)
       t.down()
       t.color('blue')
       style = ('Courier', 20, 'bold')
       t.write('PlAYER TWO: ' + (str(name_two) + ' SCORE: ' + str(scoreTwoInt)), font=style, align='center')
       t.up()
       t.forward(60)
       t.down()
       t.color('blue')
       style = ('Courier', 50, 'bold')
       t.write('TMRM GAMES', font=style, align='center')
       t.up()
       if int(scoreOneInt) > int(scoreTwoInt):
          t.backward(300)
          t.down()
          t.color('blue')
          style = ('Courier', 50, 'bold')
          t.write('PLAYER ONE WINS', font=style, align='center')
       elif int(scoreTwoInt) > int(scoreOneInt):
          t.backward(300)
          t.down()
          t.color('blue')
          style = ('Courier', 50, 'bold')
          t.write('PLAYER TWO WINS', font=style, align='center')
       else:
          t.backward(300)
          t.down()
          t.color('blue')
          style = ('Courier', 50, 'bold')
          t.write('DRAW', font=style, align='center')
           

#textwidget = tk.Text()
#textwidget.insert(tk.END, text_response)
#textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#CREDITS 
credits_label = tk.Label(window, text="Open Trivia DB API by PIXELTAIL GAMES", font=("Helvetica", 8))
credits_label.grid(row=21, column=0, sticky="WE", padx=10)

#INSTRUCTIONS
#CREDITS
instructions_label = tk.Label(window, text="[INSTRUCTIONS FOR PLAY] \n STEP 1: Both Players Enter Their Name & Select The Type of Quiz \n STEP 2: Click START QUIZ \n STEP 3: Each Player Selects Their Answer To The Question \n STEP 4: Click SUBMIT ANSWER \n STEP 5: HAVE FUN!", font=("Helvetica", 8))
instructions_label.grid(row=22, column=0, sticky="WE", padx=10)

#WELCOME
welcome_label = tk.Label(window, text="Hello, and welcome to OPEN QUIZ", font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)


#PLAYER ONE PROMPT
playerone_label = tk.Label(window, text="Player ONE, Please Enter Your Name:", font=("Helvetica", 15))
playerone_label.grid(row=1, column=0, sticky="N", padx=20, pady=10)

#PLAYER ONE Name Input
name_one_input = tk.Entry(window,width=10)
name_one_input.grid(row=2, column=0, sticky="WE", padx=10)

#PLAYER TWO PROMPT
playertwo_label = tk.Label(window, text="Player TWO, Please Enter Your Name:", font=("Helvetica", 15))
playertwo_label.grid(row=3, column=0, sticky="N", padx=20, pady=10)

#PLAYER TWO Name Input
name_two_input = tk.Entry(window,width=10)
name_two_input.grid(row=4, column=0, sticky="WE", padx=10)



#Question Selector
lb1 = tk.Label(window, text="How many questions would you like? ", font=("Helvetica", 15))

lb1.grid(row=5, column=0, sticky="WE", padx=10)


amount_combo = ttk.Combobox(window)

amount_combo['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

amount_combo.current(0) #set the selected item

amount_combo.grid(row=6, column=0, sticky="WE", padx=10)

amount = amount_combo.get()

#Category Selector
lb2 = tk.Label(window, text="What Category of Question would you like? ", font=("Helvetica", 15))

lb2.grid(row=7, column=0, sticky="WE", padx=10)


cat_combo = ttk.Combobox()

cat_combo['values']= ("General Knowledge", "Books", "Film", "Music", "Musicals & Theatre", "Television", "Video Games", "Board Games", "Nature", "Computers", "Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals")

cat_combo.current(0) #set the selected item

cat_combo.grid(row=8, column=0, sticky="WE", padx=10)

cat_raw = cat_combo.get()



#Difficulty Selector

lb3 = tk.Label(window, text="What difficulty of question would you like? ", font=("Helvetica", 15))

lb3.grid(row=9, column=0, sticky="WE", padx=10)


diff_combo = ttk.Combobox(window)

diff_combo['values']= ("Easy", "Normal", "Hard")

diff_combo.current(0) #set the selected item

diff_combo.grid(row=10, column=0, sticky="WE", padx=10)

diff_raw = diff_combo.get()

start_button = tk.Button(text="START QUIZ", command=start_quiz)
start_button.grid(row=11, column=0, sticky="WE", padx=10, pady=10)


window.mainloop()


##END

