### AUTHOR: TMRM   
### PROJECT: Perform Calculations using Formulas
### VER: 1.0
### DATE: 05-18-2020

#Task #1: Find the area of a circle
print ("\n [TASK #1: Find the area of a circle using the formula  pi(3.14) x radius^2]")

#Declare STRINGs & VALs
rad = float(input("\n Enter the Radius of The Circle = "))
measure = str(input("\n Enter the Measurement Units = (mm,cm,in,etc.) "))
pi = float(3.14)

#CALCs
val = (pi * (rad * rad))
dia = (rad * 2)
#OUTPUT
print ("\n Diameter of the circle: " + str(dia) + str(measure))
print ("\n Area of the circle: " + str(val) + str(measure) + "^2")


##################################################################################################

#Task #2: Calculate Simple Interest
print ("\n [TASK #2: Calculate Simple Interest using the formula: (Principal x Time x Rate)/100]")

#Declare STRINGs & VALs
raw_prin = input("\n Principle Of Loan (Amount of money loaned/borrowed in $) = ")
prin = float(raw_prin.replace("$",""))
raw_time = input("\n Time (Amount of Years) = ")
time = float(raw_time.replace("years",""))
raw_rate = input("\n Rate (Percentage Interest) = ")
rate = float(raw_rate.replace("%",""))

#CALCs
simple_interest = ((prin * time * rate)/ 100 )

#OUTPUT
print (str(" $ ") + str(simple_interest))


##################################################################################################

#Task #3: Calculate Perimeter & Area of Rectangle
print ("\n [TASK #3: Calculate Perimeter ((L*2)+(W*2)) & Area(L*W) of a Rectangle")

#Declare STRINGs & VALs
len_rec = float(input("\n Enter The Length of Rectangle = "))
wid_rec = float(input("\n Enter The Width of Rectangle = "))
measure_rec = str(input("\n Enter the Measurement Units = (mm,cm,in,etc.) "))

#CALCs
perim_rec = float(((len_rec * 2) + (wid_rec * 2)))
area_rec = float((len_rec * wid_rec))

#OUTPUT
print ("\n Perimeter of the square: " + str(perim_rec) + str(measure_rec))
print ("\n Area of the square: " + str(area_rec) + str(measure_rec) + "^2")
