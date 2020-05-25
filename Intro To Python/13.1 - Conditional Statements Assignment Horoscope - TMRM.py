### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - HOROSCOPE GENERATOR
### VER: 1.0
### DATE: 05-24-2020

##Declare CALLs


### INSTALL REQUESTS
import subprocess
import sys

def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

### CALL REQUESTS
import requests


##Declare/Input VALs & STRINGs

raw_name = input("Please Enter Your Name: ")
raw_month = input("Please Enter Your Birth Month (As A Number): ")
raw_day = int(input("Please Enter Your Birth Day: "))


####################################################
###########    BIRTHDAY EVALUATORS    ##############
####################################################

### CONVERT NAMED DATE TO NUMBER ###


proc_month = int(raw_month)


###JAN BIRTHDAYS ###

if proc_month == 1 and raw_day <=19:
  astro = "capricorn"
elif proc_month == 1 and raw_day >=20:
  astro = "aquarius"


#### FEB BIRTHDAYS ###

elif proc_month == 2 and raw_day <=18:
  astro = "aquarius"
elif proc_month == 2 and raw_day >=19:
  astro = "pisces"


#### MAR BIRTHDAYS ###
  
elif proc_month == 3 and raw_day <=20:
  astro = "pisces"
elif proc_month == 3 and raw_day >=21:
  astro = "aries"


#### APR BIRTHDAYS ###
  
elif proc_month == 4 and raw_day <=19:
  astro = "aries"
elif proc_month == 4 and raw_day >=20:
  astro = "taurus"


#### MAY BIRTHDAYS ###
  
elif proc_month == 5 and raw_day <=20:
  astro = "taurus"
elif proc_month == 5 and raw_day >=21:
  astro = "gemini"


#### JUN BIRTHDAYS ###
  
elif proc_month == 6 and raw_day <=20:
  astro = "gemini"
elif proc_month == 6 and raw_day >=22:
  astro = "cancer"

#### JUL BIRTHDAYS ###
  
elif proc_month == 7 and raw_day <=22:
  astro = "cancer"
elif proc_month == 7 and raw_day >=23:
  astro = "leo"

#### AUG BIRTHDAYS ###
  
elif proc_month == 8 and raw_day <=22:
  astro = "leo"
elif proc_month == 8 and raw_day >=23:
  astro = "virgo"

#### SEP BIRTHDAYS ###
  
elif proc_month == 9 and raw_day <=22:
  astro = "virgo"
elif proc_month == 9 and raw_day >=23:
  astro = "libra"

#### OCT BIRTHDAYS ###
  
elif proc_month == 10 and raw_day <=22:
  astro = "libra"
elif proc_month == 10 and raw_day >=23:
  astro = "scorpio"

#### NOV BIRTHDAYS ###
  
elif proc_month == 11 and raw_day <=22:
  astro = "scorpio"
elif proc_month == 11 and raw_day >=23:
  astro = "sagittarius"

#### DEC BIRTHDAYS ###
  
elif proc_month == 12 and raw_day <=22:
  astro = "sagittarius"
elif proc_month == 12 and raw_day >=23:
  astro = "capricorn"

### SET ACCEPT ASTRO VAR


### SET COMPATIBLE PARAMS FOR WEBSITE
params = (
('sign', astro),
('day', 'today'),
)




##CALCs & REQs

### SEND PARAMS TO WEBSITE WITH REQUESTS
x = requests.post('https://aztro.sameerkumar.website/', params = params)

##OUTPUTs


print ("\n ---------------------------------------------------------")
print ("\n Thank you " + raw_name + ", your sign is " + astro + " and your horoscope for today is: \n \n")
### PRINT SCRAPED CONTENT FROM WEBSITE
print(x.text)
