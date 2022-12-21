import turtle as trtl

#-----setup-----

alan_head = "alan_xmas_head.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("grid.gif")

wn.addshape(alan_head) # Make the screen aware of the new file

alan = trtl.Turtle()

xcor = alan.xcor()
ycor = alan.ycor()

letters = ["a", "s", "d", "f", "g", "h", "i", "j", "k", "l"]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image fill
'''

def draw_alan(active_alan):
  active_alan.shape(alan_head)
  wn.update()
'''
'''
def drop_apple():
  apple.goto(0, -160)
  letter.clear()
  apple.hideturtle()
'''
'''
#-----function calls-----
draw_apple(apple)
apple.penup()
letter = trtl.Turtle()
letter.hideturtle()
letter.penup()
letter.goto(-20, 100)
letter.color("white")
letter.write("a", font=("Unbounded", 50))

wn.onkeypress(drop_apple, "a")
wn.listen()
'''

alan.forward(60)
wn.mainloop()