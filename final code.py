# a121_catch_a_turtle.py

#-----import statements-----

import turtle as trtl

import random as rand

from playsound import playsound

import libwinmedia

player = libwinmedia.Player()

media = libwinmedia.Media("https://archive.org/download/Kalimba.mp3_377/Kalimba.mp3")

player.open(media)
#-----game configuration----


score = 0

font_setup = ("Arial", 20, "normal")

timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

wn = trtl.Screen()


#-----initialize turtle-----

alan = trtl.Turtle()

score_writer = trtl.Turtle()

counter =  trtl.Turtle()

list_of_x_coords = [-100, 0, 100]

list_of_y_coords = [-100, 0, 100]

wn.addshape('alan_xmas_head.gif')

alan.shape('alan_xmas_head.gif')


#-----game functions--------


def rikhil_clicked(x, y):
  if timer_up == False:
    update_score()

    change_position()
  alan_scream()

    
def alan_scream():
  playsound(r'C:/Users/rsharma/Desktop/CSP/PLTW-1.2.5/alanscream.mp3')

  


def change_position():
  new_xpos = rand.choice(tuple(list_of_x_coords))

  new_ypos = rand.choice(tuple(list_of_y_coords))

  alan.hideturtle()
  alan.goto(new_xpos, new_ypos)
  alan.showturtle()
  
def update_score():
  global score # gives this function access to the score that was created above
  score += 1
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=font_setup)  
  
  
def score_setup():
  score_writer.penup()
  score_writer.hideturtle()
  score_writer.goto(-300, 200)
  score_writer.write("Score: " + str(score), font=font_setup)  



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
def countdown_setup():
  counter.penup()
  counter.hideturtle()
  counter.goto(200, 200)
#-----events----------------

wn.bgpic("grid.gif")

alan.penup()

score_setup()
countdown_setup()
countdown()
alan.onclick(rikhil_clicked)




wn.mainloop()