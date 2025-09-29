import pygame as pg
import random as r

pg.init()

window = pg.display.set_mode((800, 600))
pg.display.set_caption("Моя первая игра")

player_size = 50
player_x = 400
player_y = 300
player_speed = 5

is_run = True

while is_run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pg.K_RIGHT] and player_x < 800:
        player_x += player_speed
    if keys[pg.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pg.K_DOWN] and player_y < 600:
        player_y += player_speed

    window.fill((0, 0, 0))

    pg.draw.rect(window, (0, 0, 255), (player_x, player_y, player_size, player_size))

    pg.display.update()