### AUTHOR: TMRM
### CONTRIBUTORS:  
### PROJECT: CISCO DevNet - ELIF STATEMENTS + CONDITIONALS
### VER: 1.0
### DATE: 06-XX-2021


### OBJECTIVE ###
# EDIT THE CODE BELOW TO GENERATE A HOROSCOPE
### OBJECTIVE ###

# PRINT PROGRAM NAME
print('''
########################
###     HOROSCOPE    ###
###     GENERATOR    ###  
########################
''')

### IMPORTs, INITs & DEFs ###

# IMPORT subprocess
import subprocess

# IMPORT sys
import sys


# FUNC TO INSTALL MODULE requests
def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# IMPORT REQUESTS
import requests



### VARs & CALCs ###

# ACCEPT USER INPUT name
name = input("Please Enter Your Name: ")

# ACCEPT USER INPUT raw_month
raw_month = input("Please Enter Your Birth Month : ")

# ACCEPT USER INPUT day
day = int(input("Please Enter Your Birth Day: "))

# convert raw month to formatted month
month = raw_month.lower()


####################################################
###########    BIRTHDAY EVALUATORS    ##############
####################################################

## CONVERT MONTH AND DAY TO SIGN

if month == 'december' or month == '12':
	astro = 'Sagittarius' if (day < 22) else 'Capricorn'	
elif month == 'january' or month == '1'or month == '01':
	astro = 'Capricorn' if (day < 20) else 'Aquarius'
elif month  == 'february' or month == '2'or month == '02':
	astro = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'march' or month == '3'or month == '03':
	astro = 'Pisces' if (day < 21) else 'Aries'
elif month == 'april' or month == '4'or month == '04':
	astro = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may' or month == '5'or month == '05':
	astro = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june' or month == '6'or month == '06':
	astro = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july' or month == '7'or month == '07':
	astro = 'Cancer' if (day < 23) else 'Leo'
elif month == 'august' or month == '8'or month == '08':
	astro = 'Leo' if (day < 23) else 'Virgo'
elif month == 'september' or month == '9'or month == '09':
	astro = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october' or month == '10':
	astro = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november' or month == '11':
	astro = 'Scorpio' if (day < 22) else 'Sagittarius'


## SET COMPATIBLE PARAMS FOR WEBSITE
params = (
('sign', astro),
('day', 'today'),
)




### CALCs & REQs ###

## SEND PARAMS TO WEBSITE WITH MODULE requests
a = requests.post('https://aztro.sameerkumar.website/', params = params)

### OUTPUTs ###

## STRING WATERFALL CLEANING THE TEXT
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

print ("---------------------------------------------------------")

