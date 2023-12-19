#!/usr/bin/env python

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

class Planet(pygame.sprite.Sprite):

    def __init__(self, img_file, rate):
        pygame.sprite.Sprite.__init__(self)
        self.img_file = img_file
        self.original_image = pygame.image.load(self.img_file).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.angle = 0
        self.rate = rate

    def initLoc(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def update(self):
        center = pygame.math.Vector2(self.pos) + pygame.math.Vector2(0, -self.radius).rotate(-self.angle)
        self.rect = self.image.get_rect(center = (round(center.x), round(center.y)))

    def orbitLeft(self):
        self.angle = (self.angle + (1/self.rate)) % 360


def main():
    imgdir = "images"
    pygame.init()
    pygame.display.set_caption('typode')
    window = pygame.display.set_mode((1200, 1200))
    clock = pygame.time.Clock()

    bg = pygame.image.load(os.path.join(imgdir, "background.png"))

    # Relative orbital period and distance constants taken from:
    # https://nssdc.gsfc.nasa.gov/planetary/factsheet/

    mercury = Planet(os.path.join(imgdir, "mercury_30x30.png"), 0.2)
    mercury.initLoc(window.get_rect().center, 39)

    venus = Planet(os.path.join(imgdir, "venus_30x30.png"), 0.6)
    venus.initLoc(window.get_rect().center, 72)

    earth = Planet(os.path.join(imgdir, "earth_30x30.png"), 1)
    earth.initLoc(window.get_rect().center, 100)

    mars = Planet(os.path.join(imgdir, "mars_30x30.png"), 1.9)
    mars.initLoc(window.get_rect().center, 152)

    jupiter = Planet(os.path.join(imgdir, "jupiter_30x30.png"), 11.9)
    jupiter.initLoc(window.get_rect().center, 520)

    all_sprites = pygame.sprite.Group(mercury, venus, earth, mars, jupiter)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.blit(bg, (0, 0))

        # Change positions
        mercury.orbitLeft()
        venus.orbitLeft()
        earth.orbitLeft()
        mars.orbitLeft()
        jupiter.orbitLeft()

        all_sprites.update()

        #window.fill(0)
        #pygame.draw.circle(window, (127, 127, 127), window.get_rect().center, 100, 1)

        all_sprites.draw(window)
        pygame.display.flip()

    pygame.quit()
    exit()


if __name__ == "__main__":
        main()
