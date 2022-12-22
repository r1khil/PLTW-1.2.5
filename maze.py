import turtle as trtl

alan = trtl.Turtle()


alan.penup()
alan.goto(-150, 100)
alan.pendown()
for t in range(3):
  alan.forward(50)
alan.setheading(270)
for s in range(3):
  alan.forward(50)

wn = trtl.Screen()
wn.mainloop()