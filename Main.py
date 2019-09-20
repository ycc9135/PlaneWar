from PlaneWar.Plane import *
from PlaneWar.Map import *
from pygame.locals import *
from PlaneWar.Stone import *
from PlaneWar.Bullet import *
from PlaneWar.StoneGe import *
import sys
import copy
from PlaneWar.Tools import *
from PlaneWar.ML import *
import torch as t
from PlaneWar.Store import *
import numpy as np

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

perScore = 1  # 打死一个加一分


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


def AICtrl(mo):
    if mo == 0:
        player.goleft(_map)
    elif mo == 1:
        player.goright(_map)
    if mo == 2:
        player.goup(_map)
    elif mo == 3:
        player.godown(_map)
    if mo == 4:
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


def exit():
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()


def koutu():
    for b in player.bullets:
        b.removeFromMap(_map)
    for s in stoneGe.stones:
        s.removeFromMap(_map)
    if player.alive:
        player.removeFromMap(_map)


def otherAct():
    global score
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
                score += perScore  # 分数累加
                break


def putInMap():
    for b in player.bullets:
        b.putInMap(_map)
    for s in stoneGe.stones:
        s.putInMap(_map)
    if player.alive:
        player.putInMap(_map)


lastMap = None
aNet = A()
cNet = C()
store = Store(100)
while True:
    exit()
    stoneGe.run()

    # 做动作前
    if lastMap is None:
        map1 = copy.deepcopy(_map.data)
    else:
        map1 = lastMap
    map2 = copy.deepcopy(_map.data)
    inputs = getInputs(map1, map2, _map.h, _map.w)
    inputs = t.Tensor([inputs])
    inputs = inputs.reshape((1, 2, 60, 40))
    # 做动作前

    koutu()

    # 做动作
    if player.alive:
        player.fireN += 1
        a_out = aNet(inputs)
        ss = inputs.detach().numpy().tolist()
        a = a_out.detach().numpy().tolist()
        mo = a_out.max(1)[1].item()
        # playerCtrl()
        AICtrl(mo)
        oldScore = score
    # 做动作

    if not player.alive and pg.key.get_pressed()[K_r]:
        replay()
    otherAct()
    if player.alive:
        for s in stoneGe.stones:
            if player.checkAABB(s):
                stoneGe.stones.remove(s)
                player.alive = False
                break
    putInMap()

    # 做动作后
    r = score - oldScore
    map3 = copy.deepcopy(_map.data)
    s_ = t.Tensor([getInputs(map2, map3, _map.h, _map.w)]).reshape((1, 2, 60, 40)).numpy().tolist()
    store.add(ss, a, r, s_)

    if len(store.stores) == store.maxNum:
        sample = store.sample(64)
        sample = np.array(sample)
        ss = sample[:, 0]
        aa = sample[:, 1]
        rr = sample[:, 2]
        ss_ = sample[:, 3]

        # cInputs = t.Tensor(ss)
        # cInputs = cInputs.view(cInputs.size(), 64)
        # print(cInputs.shape)

        # c网络的输入 = ss拼接aa
        # c网络输出 = c(c网络输入)
        # cnext网络输出(ss_拼接【ss_放入a网络中得到的输出】)
        # c网络输出=cnext网络输出+奖励
        # 计算c网络误差  实际值：c网络输出   标签值：cnext网络输出+奖励
        # c网络梯度归零，c网络误差反向传播
        # c网络参数优化

        # 冻结c网络参数
        # ss输入a网络得到输出aa，ss拼接输出aa传入c网络得到c网络输出
        # a网络误差 = -c网络输出
        # a网络梯度归零
        # a网络误差反向传播
        # a网络按时优化

    # 做动作后

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
