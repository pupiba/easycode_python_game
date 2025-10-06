import pygame as pg
import random as r
import math as m

pg.init()

WIDTH = 800
HEIGHT = 600

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Defender")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.width = 40
        self.height = 40
        self.speed = 5
        self.color = GREEN
        self.hp = 100

    def draw(self, screen):
        points = [(self.x, self.y - self.height // 2),
                  (self.x - self.width // 2, self.y + self.height // 2),
                  (self.x + self.width // 2, self.y + self.height // 2)]
        pg.draw.polygon(screen, self.color, points)

    def move(self, keys):
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pg.K_RIGHT] and self.x < 750:
            self.x += self.speed
        if keys[pg.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pg.K_DOWN] and self.y < 550:
            self.y += self.speed

class Enemy:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = r.randint(self.width, WIDTH - self.width)
        self.y = r.randint(-100, -40)
        self.speed = r.uniform(1, 3)
        self.color = RED
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height))
    
    def move(self):
        self.y += self.speed
        
    def off_screen(self):
        return self.y > HEIGHT
    
    def collides_with(self, bullet):
        distance = m.sqrt((self.x - bullet.x) ** 2 + (self.y - bullet.y) ** 2)
        return distance < (self.width // 2 + bullet.radius)

clock = pg.time.Clock()
player = Player()
enemys = []
timer = 0
score = 0


is_run = True
while is_run:
    window.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_run = False

    timer += 1
    if timer >= 60:
        timer = 0
        enemys.append(Enemy())

    for enemy in enemys:
        enemy.move()
        enemy.draw(window)
        if enemy.off_screen():
            enemys.remove(enemy)
            player.hp -= 10

    keys = pg.key.get_pressed()
    player.move(keys)

    player.draw(window)
    

    
    clock.tick(60)
    pg.display.update()