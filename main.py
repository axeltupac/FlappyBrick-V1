#SETUP PYGAME ZERO
import pgzrun
import random
#SCREEN
WIDTH = 600
HEIGHT = 400
#SETUP SCORE
score = 0
#SETUP BRICK
brick = Actor("brick")
brick.x = 90
brick.y = 250
#SETUP WALLS
wall_top = Actor("wall-top")
wall_bottom = Actor("wall-bottom")
gap = 150
wall_top.x = 300
wall_top.y = 0
wall_bottom.x = 300
wall_bottom.y = wall_top.height + gap
#BUTTON PRESSES
def on_mouse_down():
  brick.y=brick.y-50
#DRAW STUFF TO SCREEN
def draw():
  screen.fill("black")
  brick.draw()
  wall_top.draw()
  wall_bottom.draw()
  screen.draw.text(str(score), (450, 30), color="orange")
  

#EACH CYCLE THROUGH THE LOOP
def update():
  global score
  brick.y = brick.y + 1
  wall_top.x = wall_top.x - 1
  wall_bottom.x = wall_bottom.x - 1
    #COLLISIONS
  if brick.y > 600:
    reset()
  if brick.colliderect(wall_top) or brick.colliderect(wall_bottom):
   reset()
  if wall_top.x <=0:
    score = score + 1
    reset_walls()
#RESET
def reset():
  global score
  score = 0
  print("The game is resetting!")
  brick.y = 250
  wall_top.x = 300
  wall_bottom.x = 300
  
def reset_walls():
    wall_top.x = 600
    wall_bottom.x = 600
    wall_top.y = random.randint(-50, 50)
    wall_bottom.y = wall_top.y + wall_top.height + gap

#RUN PYGAME ZERO
pgzrun.go()