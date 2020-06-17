### AUTHOR: TMRM   
### PROJECT: INTRO TO PYTHON - Drawing With the Turtle Library
### VER: 1.0
### DATE: 06-09-2020

#####################
###TURTLE  DRAWING###
#####################

### OBJECTIVE ###
# 4 squares, shade in red, blue, yellow, green
# Capital E and shade it RED
### OBJECTIVE ###

##Declare CALLs & DEFs
import turtle

##Declare/Input VALs & STRINGs
t = turtle.Turtle()

#TURTLE: RED SQUARE
t.color("red")

t.begin_fill()

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.end_fill()

t.up()

t.forward(200)


#TURTLE: BLUE SQUARE
t.color("blue")

t.down()

t.begin_fill()

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.end_fill()

t.up()

#TURTLE: YELLOW SQUARE

t.forward(200)

t.color("yellow")

t.down()

t.begin_fill()

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.end_fill()

t.up()



#TURTLE: GREEN SQUARE

t.forward(200)

t.color("green")

t.down()
t.begin_fill()

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.left(90)

t.forward(100)

t.end_fill()

t.up()

t.forward(70)

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
