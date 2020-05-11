
# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
# code borrowed from Chris Cozort

import pygame as pg
from pygame.sprite import Sprite
import random


WIDTH = 480
HEIGHT = 600
FPS = 60

# defining the colors
WHITE = (255, 255, 255)
DARKBLUE = (39, 54, 77)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# ground colors for the map
BROWN = (112, 78, 15)
BEIGHE = (222, 206, 177)

# initialize pygame...
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("The Battle of Helm's Deep")
clock = pg.time.Clock()

# this is the main class that will be the main character
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.pew()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        # if keystate[pg.K_w]:
        #     self.speedy = -8
        # if keystate[pg.K_s]:
        #     self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
    def pew(self):
        lazer = Lazer(self.rect.centerx, self.rect.top)
        all_sprites.add(lazer)
        lazers.add(lazer)
# monster or enemy class that that will be based on the uruk hai
class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((40,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(0, 240)
        self.speedx = random.randrange(1,10)
        self.speedy = random.randrange(1,10)
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.speedx*=-1
            self.rect.y += 25
        if self.rect.y > HEIGHT:
            self.rect.y = -25
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
# this class makes the projectiles(arrows)
class Lazer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((5,25))
        self.image.fill(BEIGHE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# where all the new things get created and grouped...
all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
lazers = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(0,8):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)


# the game loop
running = True
while running: 
    # keep loop running based on clock
    clock.tick(FPS)
    for event in pg.event.get():
        # window x button
        if event.type == pg.QUIT:
            running = False

    # update
    all_sprites.update()
    hits = pg.sprite.groupcollide(mobs, lazers, True, True)

    hits = pg.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # function to create platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
    # Draw
    def new(self):
        self.all_sprites = Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # gives platforms a position
        ground = Platform(0, HEIGHT-40, WIDTH, 40)
        self.all_sprites.add(ground)
        self.platforms.add(ground)
    
    
        self.run()
    # ground or field where enemies run
    screen.fill(BROWN)  
    all_sprites.draw(screen)
    pg.display.flip()

# # import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([800,600])
# screen.fill(white)

# pygame.display.flip()

pg.quit()



# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement

# import pygame as pg
# from pygame.sprite import Sprite
# import random
# from os import path

# WIDTH = 480
# HEIGHT = 600
# FPS = 60

# # define colors
# WHITE = (255, 255, 255)
# DARKBLUE = (39, 54, 77)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# font_name = pg.font.match_font('arial')
# game_dir = path.join(path.dirname(__file__))

# # load all images...
# # background_image = pg.image.load(game_dir + "/img/bg.png")
# # background_rect = background_image.get_rect()
# # background_rect2 = background_image.get_rect()
# player_image = pg.image.load(game_dir + "/img/player.png")
# mob_image = pg.image.load(game_dir + "/img/mob.png")

# # initialize pygame...
# pg.init()
# pg.mixer.init()
# screen = pg.display.set_mode((WIDTH, HEIGHT))
# pg.display.set_caption("The Defense of Helm's Deep")
# clock = pg.time.Clock()

# # utils

# # def draw_text(text, size, color, x, y):
# #         font = pg.font.Font('arial', size)
# #         text_surface = font.render(text, True, color)
# #         text_rect = text_surface.get_rect()
# #         text_rect.midtop = (int(x), int(y))
# #         screen.blit(text_surface, text_rect)

# class Player(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         self.image = pg.transform.scale(player_image, (50, 40))
#         self.image.set_colorkey(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH / 2
#         self.rect.bottom = HEIGHT - 10
#         self.speedx = 0
#         self.speedy = 10
#         self.hitpoints = 100
#         self.ammo = 100
#     def update(self):
#         self.speedx = 0
#         # self.speedy = 0
#         keystate = pg.key.get_pressed()
#         if keystate[pg.K_w]:
#             self.pew()
#         if keystate[pg.K_a]:
#             self.speedx = -8
#         if keystate[pg.K_d]:
#             self.speedx = 8
#         # if keystate[pg.K_w]:
#         #     self.speedy = -8
#         # if keystate[pg.K_s]:
#         #     self.speedy = 8
#         self.rect.x += self.speedx
#         # self.rect.y += self.speedy
#     def pew(self):
#         if self.ammo > 0:
#             lazer = Lazer(self.rect.centerx, self.rect.top)
#             all_sprites.add(lazer)
#             lazers.add(lazer)
#             self.ammo-=1
#             # print(self.ammo)

# class Mob(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         self.image = pg.transform.scale(mob_image, (20, 20))
#         self.image.set_colorkey(BLACK)
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(0, WIDTH-self.rect.width)
#         self.rect.y = random.randrange(0, 240)
#         self.speedx = random.randrange(1,10)
#         self.speedy = random.randrange(1,10)
#     def update(self):
#         self.rect.x += self.speedx
#         if self.rect.x > WIDTH or self.rect.x < 0:
#             self.speedx*=-1
#             self.rect.y += 25
#         if self.rect.y > HEIGHT:
#             self.rect.y = -25
#             self.rect.x = random.randrange(0, WIDTH-self.rect.width)
# class Lazer(Sprite):
#     def __init__(self, x, y):
#         Sprite.__init__(self)
#         self.image = pg.Surface((5,25))
#         self.image.fill(BROWN)
#         self.rect = self.image.get_rect()
#         self.rect.bottom = y
#         self.rect.centerx = x
#         self.speedy = -10
#     def update(self):
#         self.rect.y += self.speedy
#         if self.rect.bottom < 0:
#             self.kill()

# # where all the new things get created and grouped...
# all_sprites = pg.sprite.Group()
# mobs = pg.sprite.Group()
# lazers = pg.sprite.Group()
# player = Player()
# all_sprites.add(player)
# for i in range(0,8):
#     mob = Mob()
#     all_sprites.add(mob)
#     mobs.add(mob)


# # the game loop
# running = True
# while running: 
#     # keep loop running based on clock
#     clock.tick(FPS)
#     for event in pg.event.get():
#         # window x button
#         if event.type == pg.QUIT:
#             running = False

#     # update
#     all_sprites.update()
#     hits = pg.sprite.groupcollide(mobs, lazers, True, True)

#     hits = pg.sprite.spritecollide(player, mobs, False)
#     if hits:
#         running = False
    
#     if len(mobs) == 0:
#         for i in range(0,8):
#             mob = Mob()
#             all_sprites.add(mob)
#             mobs.add(mob)
    
#     # background_rect2.y = background_rect.y - 600
#     # background_rect.y+= player.speedy
#     # background_rect2.y+= player.speedy

#     # if background_rect2.y >- 0:
#     #     background_rect.y = background_rect.y -600
    
#     # Draw
#     screen.fill(BEIGHE)
#     # screen.blit(background_image, background_rect)
#     # screen.blit(background_image, background_rect2)
#     # draw_text(str(player.ammo), 22, WHITE, WIDTH/2, 15)
#     # all_sprites.draw(screen)
#     # pg.display.flip()

# pg.quit()