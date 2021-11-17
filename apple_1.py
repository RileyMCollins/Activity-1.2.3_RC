#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
draw_apple(apple)
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)
drawer.goto(-12, 100)

# This function takes care of font and color.
def draw_an_A():
  drawer.color("white")
  drawer.write("A", font=("Arial", 30, "bold")) 

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.
draw_an_A()

wn.listen()

#-----function calls-----

wn.bgpic("background.gif")
wn.mainloop()