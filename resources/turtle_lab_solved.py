import turtle

raphael = turtle.Turtle()

#==================================================
# TURTLE OPERATION
#
#    t = turtle.Turtle() makes a new turlte
#    t.fd(<length>)
#        t.fd(100)
#    t.bk(<length>)
#        t.bk(100)
#    t.rt(<angle>)
#        t.rt(45)
#    t.lt(<length>)
#        t.lt(45)
#    t.position() returns (x, y) coordinates of the turtle
#    t.setx(<x coordinate>)
#        t.setx(0)
#    t.sety(<y coordinate>)
#        t.sety(0)
#    t.color((<red>, <green>, <blue>))
#        t.color((255, 255, 0))
#==================================================


#==================================================
# Problem 0

# Test out some of the turtle commands
# Note there is a turtle already created above
# it is the variable raphael
#==============
# Your Code Here
#==============

# End Problem 0
#==================================================

#==================================================
# Problem 1

# Write the function square which will instruct a turtle to
# draw a square with a specified side length
# This should not be recursive

def draw_square(t, size):
    #==============
    # Your Code Here
    sides = 4
    while sides > 0:
        t.fd(size)
        t.rt(90)
        sides-= 1
    #==============

# Test your function
# YOU MUST COMMENT OUT ANY CODE FROM PROBLEM 0
#==============
# Your Code Here
#draw_square(raphael, 300)
#==============

#End Problem 1
#==================================================


#==================================================
# Problem 2

# A stright spiral is a sprial like shape made of
# sides that are straight lines at 90 degree angles
# to each other.
# Each side is shorter than the previous side.

# Write a RECURSIVE funtion that draws a stright
# spiral given a turtle and the length of the
# initial side.

def draw_spiral(t, size):
    #==============
    # Your Code Here
    if size > 0:
        t.fd(size)
        t.rt(90)
        draw_spiral(t, size - 5)
    #==============

# Test your function
# YOU MUST COMMENT OUT ANY CODE FROM PROBLEMS 0 and 1
#==============
# Your Code Here
draw_spiral(raphael, 200)
#==============

#End Problem 2
#==================================================

def draw_spiral2(t, size):
    #==============
    # Your Code Here
    if size > 0:
        t.fd(size)
        t.rt(60)
        draw_spiral2(t, size - 5)

#draw_spiral2(raphael, 200)

# These 2 lines create a window and will display
# the drawing results of any turtle code written above.
# You should not change these lines.
window = turtle.Screen()
window.exitonclick()
