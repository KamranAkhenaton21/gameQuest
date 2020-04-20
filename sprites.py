
# # Sprite classes for platform game
# # © 2019 KidsCanCode LLC / All rights reserved.
# help and code from Mr. Cozort 
import pygame as pg
from pygame.sprite import Sprite
from settings import *
vec = pg.math.Vector2

class Player(Sprite):
    # include game parameter to pass game class as argument in main
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def myMethod(self):
        pass
    # function for jumping 
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits: 
            self.vel.y = -20
    # function that updates the character, for example: movement
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
        if keys[pg.K_SPACE]:
            self.jump()

        # applies friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT: 
            self.pos.y = 0

    # creating a gun for character
    # def gun(self):
    #     self.rect.midbottom = self.pos


# function to create platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
