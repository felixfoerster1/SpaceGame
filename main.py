import pgzrun
import random

HEIGHT = 800
WITH = 800


ship = Actor("playership1_blue.png")
ship.x = 50
ship.y = 100

gem = Actor("gemgreen.png")
gem.x = random.randint(0 , 800)
gem.y = 0



def draw():
    screen.clear()
    ship.draw()
    gem.draw()
    screen.draw.text(f"score:{score}",(0,0),fontsize=40, color="white")
def update():
    global score
    gem.y+= 4
    if keyboard.right():
        ship.x +=5
    if keyboard.left():
        ship.x +=-5
    if ship.colliderect(gem):
        score+=10
    if gem.y>= 750:
        gem.y=0
        gem.x= random.randint(0,800)
        score+= -20

pgzrun.go()