#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Margaret Whitmer
#Date
# 12/19/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries

import turtle as trtl

#create turtle
size = 1

drawer = trtl.Turtle()
drawer.pensize(size)

#movement functions

# go up
def up():
  drawer.setheading(90) # turn to up position
  drawer.forward(10)  # move forward 10

# go down
def down():
  drawer.setheading(270) # turn to down position
  drawer.forward(10)  # move forward 10

# go left
def left():
  drawer.setheading(180) # turn to left position
  drawer.forward(10)  # move forward 10

# go right
def right():
  drawer.setheading(0) # turn to right position
  drawer.forward(10)  # move forward 10

#color/drawing functions

# pensize gets bigger
def pen_size_big():
    global size # check current size
    drawer.pensize(size + 1) # add one to that size
    size += 1

# pensize gets smaller
def pen_size_small():
   global size # check current size
   drawer.pensize(size - 1) # subtract one from that size
   size -= 1

# make the pen pich up / go down
def pen_up_down():
    if drawer.isdown() == True: # check if the pen is up/down
        drawer.penup() # if down, pick up
    else:
        drawer.pendown() # if up, put down

# clear the drawing
def clear_screen():
    drawer.clear() # clear screen


def color_change():
    color = input("type a color:")
    drawer. pencolor(color)

  
#create screen

wn = trtl.Screen()

#bind to keypresses

# arrow keys = move turtle
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
# o = make bigger, p = make smaller
wn.onkeypress(pen_size_big, "o")
wn.onkeypress(pen_size_small, "p")
# space = clear screen
wn.onkeypress(clear_screen, "space")
# u = pen up/down
wn.onkeypress(pen_up_down, "u")
# c = change pen color 
wn.onkeypress(color_change, "c")

#listen

wn.listen()

#mainloop

wn.mainloop()
