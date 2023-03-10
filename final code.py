# a121_catch_a_turtle.py

#-----import statements-----

import turtle as trtl

import random as rand

import leaderboard as lb

#-----game configuration----


leaderboard_file_name = "a125_leaderboard.txt"
player_name = input ("Please enter your name:")

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
    wn.clear()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 
    
def countdown_setup():
  counter.penup()
  counter.hideturtle()
  counter.goto(200, 200)


def manage_leaderboard():
 
 global score
 global alan
 
 # get the names and scores from the leaderboard file
 leader_names_list = lb.get_names(leaderboard_file_name)
 leader_scores_list = lb.get_scores(leaderboard_file_name)
 
 # show the leaderboard with or without the current player
 if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
   lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
   lb.draw_leaderboard(True, leader_names_list, leader_scores_list, alan, score)
 
 else:
   lb.draw_leaderboard(False, leader_names_list, leader_scores_list, alan, score)
#-----events----------------

wn.bgpic("grid.gif")

alan.penup()

score_setup()
countdown_setup()
countdown()
alan.onclick(rikhil_clicked)




wn.mainloop()