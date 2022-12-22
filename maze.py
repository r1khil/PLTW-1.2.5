import turtle as trtl

alan = trtl.Turtle()


wn = trtl.Screen()

wn.bgpic("grid.gif")

wn.setup (width=300, height=300)

print(wn.window_height())
print(wn.window_width())

alan.backward(100)
alan.left(90)
alan.forward(100)

alan.goto(0, 100)

wn.mainloop()