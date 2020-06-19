import tkinter as tk
import tkinter.ttk as ttk
import requests
import json
import time
import random

window = tk.Tk()
window.geometry("900x550")
window.title("QUIZ")
window.grid_columnconfigure(0, weight=1)
var = tk.StringVar()
scoreInt = 0
global amount
global cat_raw
global cat
global diff


def selected():
  global selection
  selection = str(var.get())

def start_quiz():
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
  diff_raw = diff_combo.get()
  if diff_raw == 'Easy':
      diff = 'easy'
  elif diff_raw == 'Normal':
        diff = 'medium'
  elif diff_raw == 'Hard':
        diff = 'hard'
  #user_input = text_input.get()
  amount = amount_combo.get()
  print(amount)
  print(cat)
  print(diff)
  ## CONVERT CAT_RAW TO CAT
  payload = {'amount' : amount, 'category' : cat, 'difficulty' : diff}
  response = requests.get("https://opentdb.com/api.php?", params=payload)
  global text_response
  text_response = response.text
  lb1.configure(text="")
  lb2.configure(text="")
  lb3.configure(text="")
  cat_combo.grid_forget()
  amount_combo.grid_forget()
  diff_combo.grid_forget()
  start_button.grid_forget()
  pretty_json = json.loads(response.text)
  # print (json.dumps(pretty_json, indent=2))
  # print(pretty_json['results'])
  global quiz
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
  #print the Second Category Chosen
  #print (quiz[1]['category'])
  print ("---------------------------------------------------------")
  answer_list = [(quiz[0]['correct_answer']), (quiz[0]['incorrect_answers'][0]), (quiz[0]['incorrect_answers'][1]), (quiz[0]['incorrect_answers'][2])]
  #randomly arrange answers
  random.shuffle(answer_list)
  print (answer_list)
  #Question Display:
  global lb4
  lb4 = tk.Label(window, text=  quiz[0]['question'])        
  lb4.grid(row=9, column=0, sticky="WE", padx=10, pady=10)
  #Select Your Answer Prompt:
  lb5 = tk.Label(window, text="Select Your Answer: ")        
  lb5.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
  #Radio Button Logic
  global rad1
  rad1 = ttk.Radiobutton(window, text= answer_list[0], variable=var, value= answer_list[0], command=selected)
  rad1.grid(row=11, column=0, sticky="WE", padx=10, pady=10)
  global rad2
  rad2 = ttk.Radiobutton(window, text= answer_list[1], variable=var, value= answer_list[1], command=selected)
  rad2.grid(row=12, column=0, sticky="WE", padx=10, pady=10)
  global rad3
  rad3 = ttk.Radiobutton(window, text= answer_list[2], variable=var, value= answer_list[2], command=selected)
  rad3.grid(row=13, column=0, sticky="WE", padx=10, pady=10)
  global rad4
  rad4 = ttk.Radiobutton(window, text= answer_list[3], variable=var, value= answer_list[3], command=selected)  
  rad4.grid(row=14, column=0, sticky="WE", padx=10, pady=10)
  global btn2
  btn2 = tk.Button(window, text="SUBMIT ANSWER", command=checked )
  btn2.grid(row=15, column=0, sticky="WE", padx=10, pady=10)


def checked():
  lb4.grid_forget()
  rad1.grid_forget()
  rad2.grid_forget()
  rad3.grid_forget()
  rad4.grid_forget()
  btn2.grid_forget()
  #GUESS RESOLUTION LOGIC
  if selection == quiz[0]['correct_answer']:
     lb6 = tk.Label(window, text="Great Job, You Answered Correctly.")        
     lb6.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
     print ("Correct Answer Detected")
     global scoreInt
     scoreInt = scoreInt + 1
     print("Current Score: ",scoreInt)


  else:
      lb7 = tk.Label(window, text="Sorry, You Answered Incorrectly.")        
      lb7.grid(row=10, column=0, sticky="WE", padx=10, pady=10)
      print("Current Score: ",scoreInt)

  
#textwidget = tk.Text()
#textwidget.insert(tk.END, text_response)
#textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

credits_label = tk.Label(window, text="Open Trivia DB API by PIXELTAIL GAMES")
credits_label.grid(row=20, column=0, sticky="WE", padx=10)


welcome_label = tk.Label(window,
                       text="Hello, and welcome to OPEN QUIZ \n Please Enter Your Name:",
                       font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

#Text Input
#text_input = tk.Entry()
#text_input.grid(row=1, column=0, sticky="WE", padx=10)


#Question Selector

lb1 = tk.Label(window, text="How many questions would you like? ")

lb1.grid(row=2, column=0, sticky="WE", padx=10)


amount_combo = ttk.Combobox(window)

amount_combo['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

amount_combo.current(0) #set the selected item

amount_combo.grid(row=3, column=0, sticky="WE", padx=10)

amount = amount_combo.get()

#Category Selector
lb2 = tk.Label(window, text="What Category of Question would you like? ")

lb2.grid(row=4, column=0, sticky="WE", padx=10)


cat_combo = ttk.Combobox()

cat_combo['values']= ("General Knowledge", "Books", "Film", "Music", "Musicals & Theatre", "Television", "Video Games", "Board Games", "Nature", "Computers", "Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals")

cat_combo.current(0) #set the selected item

cat_combo.grid(row=5, column=0, sticky="WE", padx=10)

cat_raw = cat_combo.get()



#Difficulty Selector

lb3 = tk.Label(window, text="What difficulty of question would you like? ")

lb3.grid(row=6, column=0, sticky="WE", padx=10)


diff_combo = ttk.Combobox(window)

diff_combo['values']= ("Easy", "Normal", "Hard")

diff_combo.current(0) #set the selected item

diff_combo.grid(row=7, column=0, sticky="WE", padx=10)

diff_raw = diff_combo.get()

start_button = tk.Button(text="START QUIZ", command=start_quiz)
start_button.grid(row=8, column=0, sticky="WE", padx=10, pady=10)


if __name__ == "__main__":
  window.mainloop()

