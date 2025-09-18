import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

GRAVITY = 2000.0  # pixels per second

# Random RGB color
CLR = (randint(0, 255), randint(0, 255), randint(0, 255))

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = randint(20, 60)

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)




ball = Ball(50, 100)


def draw():
    screen.clear()
    ball.draw()



def update(dt):
    #Apply constant acceleratiion formula
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt



    #detect and handle bounce 
    if ball.y > HEIGHT - ball.radius:  # We've bounced!
        ball.y = HEIGHT - ball.radius # fix the positioon
        ball.vy = -ball.vy * 0.9 #inelastic collision

    


    #X vomponent dousnt have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx



def on_key_down(key):
    """Pressing a key will kick the ball upwards"""
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()
