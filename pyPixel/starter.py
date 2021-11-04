import sys
import pygame
from pygame.locals import *
from pyPixel.drawer import Drawer
from pyPixel.signal import *

fn_update = None
fn_draw = None

on_key = Signal()
on_key_release = Signal()
on_mouse = Signal()
on_mouse_down = Signal()
on_mouse_up = Signal()

def __update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            on_key.emit(event.key)
        elif event.type == KEYUP:
            on_key_release.emit(event.key)
        elif event.type == MOUSEMOTION:
            on_mouse.emit(event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            on_mouse_down.emit(event.button)
        elif event.type == MOUSEBUTTONUP:
            on_mouse_down.emit(event.button)
    fn_update(dt)


def __draw(drawer):
    drawer.screen.fill((0, 0, 0))
    fn_draw(drawer)
    pygame.display.flip()


def __runPyGame(title, size):
    pygame.init()
    fps = 60.0
    fpsClock = pygame.time.Clock()
    drawer = Drawer(pygame.display.set_mode(size, pygame.RESIZABLE | pygame.SCALED))
    pygame.display.set_caption(title)
    dt = 1/fps
    while True:
        __update(dt)
        __draw(drawer)
        dt = fpsClock.tick(fps)


def initGame(updateFn, drawFn, title="Game", size=(640, 480)):
    global fn_update
    global fn_draw
    fn_update = updateFn
    fn_draw = drawFn
    __runPyGame(title, size)

