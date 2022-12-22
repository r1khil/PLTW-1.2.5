import turtle as trtl

#-----setup-----

alan_head = "alan_xmas_head.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("grid.gif")

wn.addshape(alan_head) # Make the screen aware of the new file

alan = trtl.Turtle()



alan.backward(60)
wn.mainloop()