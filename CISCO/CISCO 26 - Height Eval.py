### AUTHOR: TMRM   
### PROJECT: CISCO DevNet - Height Evaluator
### VER: 1.0
### DATE: 05-XX-2021

### OBJECTIVE ###
# The python ride at Snake World is one of the most exciting, intensive rides in Europe.
# It is not recommended for the faint hearted. You also have to be at least 1.4 meters to ride the ride.
# The head safety officer wants an automatic messaging system which tells people IF they are tall enough to ride the ride.
# Customize your messages for your Bahamian audience.
### OBJECTIVE ###

# Print the program title
print('''
###########################
###      WELCOME TO     ###
###          THE        ###
###      PYTHON RIDE    ###
###          AT         ###
###      SNAKE WORLD    ### 
###########################
''')

#####################
###     CODE      ###
#####################

##Declare CALLs


##Declare/Input VALs & STRINGs

# ACCEPT USER INPUT
stringNatlRaw = input("PLEASE INPUT YOUR NATIONALITY: ")

#Create stringNatl from stringNatlRaw
stringNatl = stringNatlRaw.lower()




##CALCs
if stringNatl == 'b' or stringNatl == "bahamian" or stringNatl == "bahamas":
   print("Ayyy, welcome to da snake ride. This ride don't play, you in for it now.  How tall ah you bui?")
   intHeightFeet = int(input("How many feet tall are you?: "))
   intHeightInch = int(input("How many inches?: "))
   intHeight = ((intHeightFeet * 12)+ intHeightInch)
   if intHeight >= 55:
      print("C'mon in king, you got dis!")
      
   elif intHeight >= 55:
      print("Mudda sick dred, you ain' tall nuff to ride this one king.  How bout the slip n' slide instead?")
   

elif stringNatl == 'a' or stringNatl == 'american':
   print("Howdy there, this here snake ride ain't for the faint ah heart. How tall are you anyway there partner? ")
   intHeightFeet = int(input("How many feet tall are you?: "))
   intHeightInch = int(input("How many inches?: "))
   intHeight = ((intHeightFeet * 12)+ intHeightInch)
   if intHeight >= 55:
      print("Hoooooooo boy you hit the mark. Jump on in for the ride of your life!")
      
   elif intHeight >= 55:
      print("Shuck son, you just don't meet the measure. How bout a burger instead?")


elif stringNatl == 'b' or stringNatl == 'british' or stringNatl == 'britain':
   print("Good Day Chap, this tram is quite the sticky wicket  ")
   floatHeightCenti = float(input("How many centimeters tall are you?: "))
   if floatHeightCenti >= 140:
      print("Jolly good, you are in for a tickety boo show; hop aboard!")
      
   elif floatHeightCenti >= 55:
      print("Sorry there bloke, you're a tad below the reqs. How about a spot of tea instead?")

else:
   print("Nationality Not Detected. Try again please.")


