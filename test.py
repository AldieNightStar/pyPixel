from pygame.constants import *
from pygame.draw import lines
import pyPixel as pp

img = pp.resize_image(pp.load_image("test.png"), 200, 200)

class G:
    x = 0
    y = 0
    xsp = 1
    ysp = 1
    poses = []
    lines = []

@pp.on_key.connect
@pp.on_key_release.connect
@pp.on_mouse.connect
@pp.on_mouse_down.connect
@pp.on_mouse_up.connect
def logger(*a):
    print("LOG: ", *a)

@pp.on_key.connect
def k(kk):
    if kk in (pp.K_LEFT, pp.K_RIGHT):
        G.xsp *= -1
        bounce()
    if kk in (pp.K_UP, pp.K_DOWN):
        G.ysp *= -1
        bounce()

def bounce():
    G.poses.append((G.x, G.y))
    if len(G.poses) > 3:
        pos1 = G.poses.pop()
        pos2 = G.poses.pop()
        G.poses.append(pos1)
        G.lines.append((*pos1, *pos2))

def update(dt):
    G.x += G.xsp
    G.y += G.ysp
    if G.x > 100 or G.x < 0:
        G.xsp *= -1
        bounce()
    if G.y > 80 or G.y < 0:
        G.ysp *= -1
        bounce()

def draw(drawer):
    drawer.rect(G.x, G.y, 2, 2)
    # drawer.image(img, G.x, G.y)
    for line in G.lines:
        drawer.line(*line)

pp.initGame(update, draw, "Some game", (100, 100))