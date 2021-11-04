import pygame
from pygame.color import *

color_white = Color(255, 255, 255, 0)


class Drawer:
    def __init__(self, screen) -> None:
        self.screen = screen

    def rect(self, x, y, w, h, color=color_white):
        pygame.draw.rect(self.screen, color, (x, y, w, h))

    def line(self, x1, y1, x2, y2, width=1, color=color_white):
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), width)

    def image(self, img, x, y):
        self.screen.blit(img, (x, y))
    
    def image_resized(self, img, x, y, w, h):
        rimg = pygame.transform.scale(img, (w, h))
        self.screen.blit(rimg, (x, y))
    def pix(self, x, y, color=color_white):
        self.screen.set_at((x, y), color)
