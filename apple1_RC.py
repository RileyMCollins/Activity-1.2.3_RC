#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  active_apple.pu()
  active_apple.shape(apple_image)
  wn.tracer(False)
  active_apple.sety(active_apple.ycor()-30)
  active_apple.color("White")
  active_apple.write("A", align="center", font=("Arial", 40, "bold"))
  active_apple.sety(active_apple.ycor()+30)
  wn.tracer(True)
  wn.update()

def drop_apple():
  apple.pu()
  apple.clear()
  apple.sety(-150)
  apple.hideturtle()
  apple.sety(0)
  apple.showturtle()
  
#-----functions calls-----
draw_apple(apple)

wn.onkeypress(drop_apple, "a")

wn.listen()

wn.mainloop()