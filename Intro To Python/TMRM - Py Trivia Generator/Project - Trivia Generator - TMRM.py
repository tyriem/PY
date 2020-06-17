### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - HOROSCOPE GENERATOR
### VER: 1.0
### DATE: 06-16-2020

### Declare CALLs ###


### INSTALL REQUESTS ###
import subprocess
import sys

def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

### CALL REQUESTS ###
import requests


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
a = requests.post('https://opentdb.com/api.php?', params = params)

### OUTPUTs ###

## CLEANING THE TEXT
b = a.text
c = b.replace('{"date_range": "', "\n Day of Birth: \n")
d = c.replace('", "current_date": "', "\n Current Date: \n")
e = d.replace('", "description": "', "\n Horoscope: \n")
f = e.replace('", "compatibility": "', "\n You Are Compatible With The Following Sign: \n")
g = f.replace('", "mood": "', "\n Your Current Mood Is: \n")
h = g.replace('", "color": "', "\n Your Lucky Color Is: \n")
i = h.replace('", "lucky_number": "', "\n Your Lucky Number Is: \n")
j = i.replace('", "lucky_time": "', "\n Your Lucky Time Is: \n")
k = j.replace('"}', "\n \n HAVE A GOOD DAY! \n ---------------------------------------------------------")

## PRINT PREAMBLE
print ("\n ---------------------------------------------------------")
## PRINT SCRAPED CONTENT FROM WEBSITE
print(a.text)
print ("\n ---------------------------------------------------------")
print(a.text[category])

"""
{"response_code":0,"results":[{"category":"General Knowledge","type":"multiple","difficulty":"easy","question":"What is the name of Poland in Polish?","correct_answer":"Polska","incorrect_answers":["Pupcia","Polszka","P&oacute;land"]}]}

"""


