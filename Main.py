from PlaneWar.Plane import *
from PlaneWar.Map import *
from pygame.locals import *
from PlaneWar.Stone import *
from PlaneWar.Bullet import *
import sys

size = width, height = 400, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('飞机大战')
pg.init()

clock = pg.time.Clock()

_map = Map(screen, width, height, 10)
_plane = Plane()
_plane.setxy(_map, 20, 50)

_stone = Stone()
_stone.setxy(_map, 30, 10)

_bullet = Bullet()
_bullet.setxy(_map, 20, 45)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()
    key_press = pg.key.get_pressed()
    if key_press[K_a]:
        _plane.goleft(_map)
    elif key_press[K_d]:
        _plane.goright(_map)
    if key_press[K_w]:
        _plane.goup(_map)
    elif key_press[K_s]:
        _plane.godown(_map)
    screen.fill(BLACK)
    _map.draw()
    pg.display.flip()
    clock.tick(60)
