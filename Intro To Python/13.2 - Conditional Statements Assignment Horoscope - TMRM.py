### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - HOROSCOPE GENERATOR
### VER: 1.0
### DATE: 05-24-2020

### Declare CALLs ###


### INSTALL REQUESTS
import subprocess
import sys

def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

### CALL REQUESTS
import requests



### Declare/Input VALs & STRINGs ###

name = input("Please Enter Your Name: ")
raw_month = input("Please Enter Your Birth Month : ")
day = int(input("Please Enter Your Birth Day: "))

month = raw_month.lower()


####################################################
###########    BIRTHDAY EVALUATORS    ##############
####################################################

## CONVERT MONTH AND DAY TO SIGN

if month == 'december':
	astro = 'Sagittarius' if (day < 22) else 'Capricorn'	
elif month == 'january':
	astro = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == 'february':
	astro = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'march':
	astro = 'Pisces' if (day < 21) else 'Aries'
elif month == 'april':
	astro = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may':
	astro = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june':
	astro = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july':
	astro = 'Cancer' if (day < 23) else 'Leo'
elif month == 'august':
	astro = 'Leo' if (day < 23) else 'Virgo'
elif month == 'september':
	astro = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october':
	astro = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november':
	astro = 'Scorpio' if (day < 22) else 'Sagittarius'


## SET COMPATIBLE PARAMS FOR WEBSITE
params = (
('sign', astro),
('day', 'today'),
)




### CALCs & REQs ###

## SEND PARAMS TO WEBSITE WITH REQUESTS
a = requests.post('https://aztro.sameerkumar.website/', params = params)

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
print ("\n Thank you " + name + ", your sign is " + astro + " and your horoscope for today is: ")
## PRINT SCRAPED CONTENT FROM WEBSITE
print(k)

