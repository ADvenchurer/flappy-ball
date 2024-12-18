import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Ball"

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

GRAVITY = 2000.0 #pixels per second


class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)





ball = Ball(50, 100)


def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    if ball.y > HEIGHT - ball.radius: #we've bounced!
        ball.y = HEIGHT - ball.radius #fit the position
        ball.vy = -ball.vy * 0.9 #inelastic collision

    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()
