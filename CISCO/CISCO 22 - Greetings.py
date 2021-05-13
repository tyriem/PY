### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Greetings
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# Ask the user to input traffic light colour.
# If the answer is red, display “STOP”
# Else if answer is yellow, display “Get set”
# Else if answer is green, display “GO”
# Else, display “Wrong colour”
### OBJECTIVE ###

# Print the program title
print('''
########################
###     Greetings    ###
########################
''')

#####################
###     CODE      ###
#####################

### Declare CALLs ###

### INSTALL REQUESTS
import subprocess
import sys

def install(requests):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

### CALL REQUESTS
import requests

### Declare FUNCs ###

# Fetches and prints a random joke
# Source: A08 - get_chuck_norris_joke - https://gist.github.com/AO8/74a3a81fd672a6f8d0cc149ed62295de
def get_joke():

  url = "http://api.icndb.com/jokes/random"
  resp = requests.get(url)
  resp.encoding = "utf-8"
  data = resp.json()
  print(data["value"]["joke"])



### Declare/Input VALs & STRINGs ###

# ACCEPT USER INPUT
stringTrafficRaw = input("Good Day User, How are you feeling today? (happy, sad)")

#Create stringTraffic from stringTrafficRaw
stringTraffic = stringTrafficRaw.lower()


#Create charTraffice from stringTraffic
charTraffic = stringTraffic[0:1]


##CALCs
if charTraffic == 'h':
   print("Glad to hear it!")

elif charTraffic == "s":
   print("That's sad to hear... How about a joke?: ")
   print(get_joke())


else:
   print("ERROR. Mood not detected, try again.")
