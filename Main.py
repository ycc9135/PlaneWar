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
player = Plane(5)
player.setxy(20, 50)
score = 0

fontBig = pg.font.SysFont('楷体', 50)
fontSmall = pg.font.SysFont('楷体', 24)

perScore = 1


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


def replay():
    global score
    player.alive = True
    player.setxy(20, 50)
    player.fireN = player.cd
    stoneGe.stones.clear()
    player.bullets.clear()
    stoneGe.n = 0
    score = 0


while True:
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()

    stoneGe.run()

    for b in player.bullets:
        b.removeFromMap(_map)
    for s in stoneGe.stones:
        s.removeFromMap(_map)
    if player.alive:
        player.removeFromMap(_map)

    if player.alive:
        player.fireN += 1
        playerCtrl()

    if not player.alive and pg.key.get_pressed()[K_r]:
        replay()

    for b in player.bullets:
        res = b.move(_map)
        if not res:
            player.bullets.remove(b)

    for s in stoneGe.stones:
        res = s.move(_map)
        if not res:
            stoneGe.stones.remove(s)

    for b in player.bullets:
        for s in stoneGe.stones:
            if b.checkAABB(s):
                player.bullets.remove(b)
                stoneGe.stones.remove(s)
                score += perScore
                break

    if player.alive:
        for s in stoneGe.stones:
            if player.checkAABB(s):
                stoneGe.stones.remove(s)
                player.alive = False
                break

    for b in player.bullets:
        b.putInMap(_map)
    for s in stoneGe.stones:
        s.putInMap(_map)

    if player.alive:
        player.putInMap(_map)

    screen.fill(BLACK)  # 通过填充黑色RGB颜色来擦除屏幕

    _map.draw()
    scoreTxt = fontBig.render('Score:' + str(score), 1, GREEN)
    if not player.alive:
        overTxt = fontBig.render('Game  Over', 1, RED)
        tipTxt = fontSmall.render('Press "R" to replay', 1, BLUE)
        screen.blit(overTxt, (100, 200))
        screen.blit(tipTxt, (120, 300))
    screen.blit(scoreTxt, (0, 0))
    pg.display.flip()
    clock.tick(20)
