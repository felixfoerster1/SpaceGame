import pgzrun
import random

HEIGHT = 800
WIDTH = 800
speed = False
onscreen = False
speed2 = False
speedtimer = 0
speedtimer2 = 0
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

speeditem = Actor("pill_red.png")
speeditem.x = 10
speeditem.y = 10

galaxy = Actor("galaxy.png")
galaxy.x = 500
galaxy.y = 500

def draw():
    screen.clear()
    global score
    global score2
    
    galaxy.draw()
    gem1.draw()
    gem2.draw()
    gem3.draw()
    ship.draw()
    ship2.draw()
    speeditem.draw()
    screen.draw.text(f'Score: {score}',(0,0), fontsize=40, color=(0,169,224))
    screen.draw.text(f'Score: {score2}',(670,0), fontsize=40, color=(255,0,0))

def update():
    global score
    global score2
    global speed, onscreen, speed2, speedtimer, speedtimer2
    gem1.y+= 4
    gem2.y+= 1
    gem3.y+= 6
    speeditem.y+=4
    if speed == True :
        if keyboard.right:
            ship.x +=10
        if keyboard.left:
            ship.x +=-10
    elif speed == False :
        if keyboard.right:
            ship.x +=5
        if keyboard.left:
            ship.x +=-5
    if speed2 == True :
        if keyboard.d:
            ship2.x +=10
        if keyboard.a:
            ship2.x +=-10
    elif speed2 == False :
        if keyboard.d:
            ship2.x +=5
        if keyboard.a:
            ship2.x +=-5
    
    if ship.colliderect(gem1):
        score+=20
        gem1.y=0
        gem1.x= random.randint(0,800)
    if ship2.colliderect(gem1):
        score2+=20
        gem1.y=0
        gem1.x= random.randint(0,800)
    if gem1.y>= 750:
        gem1.y=0
        gem1.x= random.randint(0,800)
        score2+= -20
        score+= -20

    if ship.colliderect(gem2):
        score+=10
        gem2.y=0
        gem2.x= random.randint(0,800)
    if ship2.colliderect(gem2):
        score2+=10
        gem2.y=0
        gem2.x= random.randint(0,800)
    if gem2.y>= 750:
        gem2.y=0
        gem2.x= random.randint(0,800)
        score2+= -50
        score+= -50

    if ship.colliderect(gem3):
        score+=50
        gem3.y=0
        gem3.x= random.randint(0,800)
    if gem3.y>= 750:
        gem3.y=0
        gem3.x= random.randint(0,800)
        score+= -10
        score2+= -10
    if ship2.colliderect(gem3):
        score2+=50
        gem3.y=0
        gem3.x= random.randint(0,800)
    
    if onscreen == False :
        if random.randint(0,1000) == 1 :
            speeditem.y = 0
            speeditem.x = random.randint(0,800) 
            onscreen = True
        else : speeditem.y = 1000


    if ship.colliderect(speeditem):
        onscreen = False
        speed = True
        speedtimer = 250
    if speed == True :
        speedtimer -= 1
        if speedtimer == 0 :
            speed = False
    if ship2.colliderect(speeditem):
        onscreen = False
        speed2 = True
        speedtimer2 = 250
    if speed2 == True :
        speedtimer2 -= 1
        if speedtimer2 == 0 :
            speed2 = False
    if speeditem.y == 700 :
        onscreen = False 
        speeditem.y = 1000
    print(speedtimer,speedtimer2)
pgzrun.go()
