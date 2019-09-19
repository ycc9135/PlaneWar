from PlaneWar.Plane import *
from PlaneWar.Map import *
from pygame.locals import *
from PlaneWar.Stone import *
from PlaneWar.Bullet import *
from PlaneWar.StoneGe import *
import sys

size = width, height = 400, 600
screen = pg.display.set_mode(size)
pg.display.set_caption('飞机大战')
pg.init()

clock = pg.time.Clock()

_map = Map(screen, width, height, 10)
stoneGe = StoneGe(_map, 5, 10)
player = Plane()
player.setxy(20, 50)


def playerCtrl():
    key_press = pg.key.get_pressed()
    if key_press[K_a]:
        player.goleft(_map)
    elif key_press[K_d]:
        player.goright(_map)
    if key_press[K_w]:
        player.goup(_map)
    elif key_press[K_s]:
        player.godown(_map)
    if key_press[K_j]:
        player.fire()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()


    stoneGe.run()

    for b in player.bullets:
        b.removeFromMap(_map)
    for s in stoneGe.stones:
        s.removeFromMap(_map)
    player.removeFromMap(_map)

    playerCtrl()

    for b in player.bullets:
        res = b.move(_map)
        if not res:
            player.bullets.remove(b)

    for s in stoneGe.stones:
        res = s.move(_map)
        if not res:
            stoneGe.stones.remove(s)

    for b in player.bullets:
        b.putInMap(_map)
    for s in stoneGe.stones:
        s.putInMap(_map)
    player.putInMap(_map)



    screen.fill(BLACK)
    _map.draw()
    pg.display.flip()
    clock.tick(20)
