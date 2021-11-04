import pygame

def load_image(filename):
    return pygame.image.load(filename)

def resize_image(img, newWidth, newHeight):
    return pygame.transform.scale(img, (newWidth, newHeight))