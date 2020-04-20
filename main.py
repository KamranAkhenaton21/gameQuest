# created by Kamran Akhenaton
# With help and code from Chris Cozort and KidsCanCode

import pygame as pg
from pygame.sprite import Group
# from pg.sprite import Group
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    # function to starts/restarts a new game
    def new(self):
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # gives platforms a position
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        plat1 = Platform(300, 400, 150, 20)
        plat2 = Platform(150, 300, 150, 20)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
        self.all_sprites.add(plat1)
        self.platforms.add(plat1)
        self.all_sprites.add(plat2)
        self.platforms.add(plat2)
        # randomly prints platforms of a random length 
        for plat in range(1,10):
            plat = Platform(random.randint(0, WIDTH), random.randint(0, HEIGHT), 200, 20)
            self.all_sprites.add(plat)
            self.platforms.add(plat)
        self.run()

    # game loop 
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # updating game loop
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if self.player.rect.top > hits[0].rect.top:
                print("i hit my head")
                self.player.vel.y = 10
                self.player.rect.top = hits[0].rect.bottom + 5
                self.player.hitpoints -= 10
                print(self.player.hitpoints)
            # print("it collided")
            else:
                self.player.vel.y = 0
                self.player.pos.y = hits[0].rect.top+1
            

    def events(self):
    # event game loop
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # game loop
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # staring the screen
        pass

    def show_go_screen(self):
        # game over
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
