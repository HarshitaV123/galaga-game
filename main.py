import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE = (255,255,255)
GREEN = (0,255,0)

score = 0
lives = 3

#creating the ship
ship = Actor("ship")
ship.pos = (WIDTH //2,HEIGHT-60)

bullets = []
enemies = []

#creating the enemies
for i in range(8):
    enemy=Actor("bug")
    enemy.x = random.randint(0, WIDTH -100)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

#set enemy movement direction
direction = 1

#set enemy movement speed
speed = 5

#function to display score
def display_score():
    global score, lives
    screen.draw.text(f"Score: {score}",(50,30))
    screen.draw.text(f"Lives: {lives}",(50,60))

#function to handle key down events
def on_key_down(key):
    if key == keys.SPACE:
        #create a new bullet
        bullet=Actor("bullet")
        bullet.x = ship.x
        bullet.y = ship.y - 50
        bullets.append(bullet)

#function to update the game
def update():
    global lives
    global score
    global direction

    #move the ship left or right
    if keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    elif keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
        