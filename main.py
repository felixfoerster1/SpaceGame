import pgzrun
import random
import os

HEIGHT = 800
WIDTH = 800


for image in images:
    if image.startswith('gem'):
        images.remove(image)

score=0
ship = Actor("playership1_blue.png")
ship.x = 50
ship.y = 700

gem = Actor("gemgreen.png")
gem.x = random.randint(0 , 800)
gem.y = 0
def draw():
    screen.clear()
    global score
    gem.draw()
    ship.draw()
    screen.draw.text(f'Score: {score}',(0,0), fontsize=40, color=(255,255,255))

def update():
    global score
    gem.y+= 4
    if keyboard.right:
        ship.x +=5
    if keyboard.left:
        ship.x +=-5
    if ship.colliderect(gem):
        r = random.randint(0, len(images) - 1)
        ship.image = images[r]
        score+=10
        gem.y=0
        gem.x= random.randint(0,800)
    if gem.y>= 750:
        gem.y=0
        gem.x= random.randint(0,800)
        score+= -20
    

pgzrun.go()