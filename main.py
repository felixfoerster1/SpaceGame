import pgzrun
import random

HEIGHT = 800
WIDTH = 800

score2=0
score=0
ship = Actor("playership1_blue.png")
ship.x = 50
ship.y = 700
ship2 = Actor("playership1_red.png")
ship2.x = 50
ship2.y = 700

gem1 = Actor("gemgreen.png")
gem1.x = random.randint(0 , 800)
gem1.y = 0

gem2 = Actor("gemred.png")
gem2.x = random.randint(0 , 800)
gem2.y = 0

gem3 = Actor("gemyellow.png")
gem3.x = random.randint(0 , 800)
gem3.y = 0  

def draw():
    screen.clear()
    global score
    global score2
    
    gem1.draw()
    gem2.draw()
    gem3.draw()
    ship.draw()
    ship2.draw()
    screen.draw.text(f'Score: {score}',(0,0), fontsize=40, color=(255,255,255))
    screen.draw.text(f'Score: {score2}',(650,0), fontsize=40, color=(200,255,255))

def update():
    global score
    global score2
    
    gem1.y+= 4
    gem2.y+= 1
    gem3.y+= 6
    if keyboard.right:
        ship.x +=5
    if keyboard.left:
        ship.x +=-5
    if keyboard.d:
        ship2.x +=5
    if keyboard.a:
        ship2.x +=-5
    
    if ship.colliderect(gem1):
        score+=20
        gem1.y=0
        gem1.x= random.randint(0,800)
    if ship2.colliderect(gem1):
        score+=20
        gem1.y=0
        gem1.x= random.randint(0,800)
    if gem1.y>= 750:
        gem1.y=0
        gem1.x= random.randint(0,800)
        score2+= -20

    if ship.colliderect(gem2):
        score+=10
        gem2.y=0
        gem2.x= random.randint(0,800)
    if ship2.colliderect(gem2):
        score+=10
        gem2.y=0
        gem2.x= random.randint(0,800)
    if gem2.y>= 750:
        gem2.y=0
        gem2.x= random.randint(0,800)
        score2+= -50

    if ship.colliderect(gem3):
        score+=50
        gem3.y=0
        gem3.x= random.randint(0,800)
    if gem3.y>= 750:
        gem3.y=0
        gem3.x= random.randint(0,800)
        score+= -10
    if ship2.colliderect(gem3):
        score2+=50
        gem3.y=0
        gem3.x= random.randint(0,800)
    if gem3.y>= 750:
        gem3.y=0
        gem3.x= random.randint(0,800)
        score+= -10
pgzrun.go()
