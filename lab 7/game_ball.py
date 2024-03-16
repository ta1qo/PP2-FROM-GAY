import pygame as pg

pg.init()
screen = pg.display.set_mode((700, 500))
window_title = pg.display.set_caption("moving ball")
clock = pg.time.Clock()
running = True

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("white")
    pg.draw.circle(screen, "red", player_pos, 25)

    keys = pg.key.get_pressed()
    if keys[pg.K_UP] and player_pos.y > 30:
        player_pos.y -= 20
    if keys[pg.K_DOWN] and player_pos.y < 470:
        player_pos.y += 20
    if keys[pg.K_LEFT] and player_pos.x > 30:
        player_pos.x -= 20
    if keys[pg.K_RIGHT] and player_pos.x < 670:
        player_pos.x += 20

    pg.display.flip()
    clock.tick(60)

pg.quit()