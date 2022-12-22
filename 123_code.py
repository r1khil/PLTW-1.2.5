import turtle as trtl
import random as rand

#-----setup-----
apple_image = "alan_xmas_head.gif" # Store the file name of your shape
y = 0
wn = trtl.Screen()
wn.bgpic("grid.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = rand.choice(letters)
print(letter)

apple = trtl.Turtle()
apple.penup()
drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()
drawer.goto(0,165)
drawer.color("black")
drawer.write(letter, font=("Arial", 25, "bold"))
x = 0
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# calls falling function
def falling_apple_caller():
  falling_apple(apple)
  drawer.clear()
  apple.hideturtle()
  letter = rand.choice(letters)
  apple.goto(0,0)
  apple.showturtle()
  a = letters.index(letter)
  letters.pop(a)
  drawer.write(letter, font=("Arial", 25, "bold"))
  wn.onkeypress(falling_apple_caller, letter )


# makes apple fall
def falling_apple(active_apple):
  global y
  while(y > -165):
    active_apple.goto(0,y)
    y = y-5

#-----function calls-----
draw_apple(apple)
wn.onkeypress(falling_apple_caller, letter )
wn.listen()
wn.mainloop()
17 
import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

turtle_list = []

temp_turtle = trtl.Turtle()
temp_turtle.pencolor("red")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("blue")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("green")
turtle_list.append(temp_turtle)
temp_turtle = trtl.Turtle()
temp_turtle.pencolor("purple")
turtle_list.append(temp_turtle)

turtle_list[0].forward(500)
turtle_list[1].setheading(45)
turtle_list[1].forward(500)
turtle_list[2].setheading(315)
turtle_list[2].forward(500)
turtle_list[3].setheading(180)
turtle_list[3].forward(500)


trtl.mainloop()
20
import turtle as trtl
import random as rand

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

number_list = [1,2,3,4]
random_numbers = [rand.choice(number_list),rand.choice(number_list),rand.choice(number_list),rand.choice(number_list)]
print(random_numbers)
# Note the usage of the keyword "in" below.
if (2 in random_numbers):
  temp_turtle = trtl.Turtle()
  temp_turtle.write("2 in list.", font=("Arial", 74, "bold"))
if (2 not in random_numbers): 
  temp_turtle = trtl.Turtle()
  temp_turtle.write("2 not in list.", font=("Arial", 74, "bold"))

trtl.mainloop() 
