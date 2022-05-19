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