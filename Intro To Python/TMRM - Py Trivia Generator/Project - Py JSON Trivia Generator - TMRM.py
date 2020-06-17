### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - HOROSCOPE GENERATOR
### VER: 1.0
### DATE: 06-16-2020

### Declare CALLs ###


### INSTALL REQUESTS ###
import subprocess
import sys
import json


def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

### CALL REQUESTS ###
import requests
import json
import turtle


####################################
t = turtle.Turtle()
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

##OUTPUTs
turtle.done()

####################################


### Declare/Input VALs & STRINGs ###

amount = int(input("How many questions would you like to answer? : "))
cat = int(input("Which category of question would you like? : "))
"""
KEY TO CATEGORIES
category 9 = General Knowledge
category 10 = Books
category 11 = Film
category 12 = Music
category 13 = Musicals & Theatre
category 14 = Television
category 15 = Video Games
category 16 = Board Games
category 17 = Science & Nature
category 18 = Science: Computers
category 19 = Science: Mathematics
category 20 = Science: Mythology
category 21 = Sports
category 22 = Geography
category 23 = History
category 24 = Politics
category 25 = Art
category 26 = Celebrities
category 27 = Animals
"""
diff = input("What difficulty of question would you like? : ")
"""
KEY TO CATEGORIES
diff easy = Easy
diff medium = Medium
diff hard = Hard
"""

## SET COMPATIBLE PARAMS FOR WEBSITE
params = (
('amount', amount),
('category', cat),
('difficulty', diff),
('type', 'multiple'),
)




### CALCs & REQs ###

## SEND PARAMS TO WEBSITE WITH REQUESTS
r = requests.get('https://opentdb.com/api.php?', params = params)

### OUTPUTs ###

## CLEANING THE TEXT
pretty_json = json.loads(r.text)
print (json.dumps(pretty_json, indent=2))
print(pretty_json['results'])
quiz_dict = (pretty_json['results'])

print ("\n ---------------------------------------------------------")
print (quiz_dict)
print ("\n ---------------------------------------------------------")
print (quiz_dict["category"])




"""
## PRINT PREAMBLE
print ("\n ---------------------------------------------------------")
## PRINT SCRAPED CONTENT FROM WEBSITE
print(a.text)
print ("\n ---------------------------------------------------------")
print(a.text[category])
"""

"""
{'response_code': 0, 'results': [{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'Which one of these is not a typical European sword design?', 'correct_answer': 'Scimitar', 'incorrect_answers': ['Falchion', 'Ulfberht', 'Flamberge']},
{'category': 'General Knowledge', 'type': 'multiple', 'difficulty': 'easy', 'question': 'The Flag of the European Union has how many stars on it?', 'correct_answer': '12', 'incorrect_answers': ['10', '14', '16']}]}
"""


