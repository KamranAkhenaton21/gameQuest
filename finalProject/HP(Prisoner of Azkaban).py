

# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
# with code and help from Chris Cosort 

# basic settings
import pygame as pg
from pygame.sprite import Sprite
import random
from os import path

WIDTH = 480
HEIGHT = 600
FPS = 60
score = 0

# define colors
WHITE = (255, 255, 255)
DARKBLUE = (39, 54, 77)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (123, 153, 184  )
game_dir = path.join(path.dirname(__file__))


# code that uploads of images
# background_image = pg.image.load(game_dir + "/img/bg.png")
# background_rect = background_image.get_rect()
# setup a second background for scrolling - feature added by Chris Cozort
# background_rect2 = background_image.get_rect()
player_image = pg.image.load(game_dir + "/img/player.png")
mob_image = pg.image.load(game_dir + "/img/mob.png")
# ammo_image = pg.image.load(game_dir + "/img/ammo.png")



# initializes pygame
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Harry's Dementor Encounter")
clock = pg.time.Clock()

# utils(collection of smal functions and classes)
font_name = pg.font.match_font('arial')

# a function that puts texts on the game screen 
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# class for the playable character
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.transform.scale(player_image, (50, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 10
        self.hitpoints = 100
        self.ammo = 100
    def update(self):
        # this code allows the player to move with keys 
        self.speedx = 0
        # self.speedy = 0
        keystate = pg.key.get_pressed()
        # if keystate[pg.K_w]:
        #     self.pew()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        # if keystate[pg.K_w]:
        #     self.speedy = -8
        # if keystate[pg.K_s]:
        #     self.speedy = 8
        self.rect.x += self.speedx
        # self.rect.y += self.speedy
    # this is the ammo for the "lazer" class 
    def pew(self):
        if self.ammo > 0:
            lazer = Lazer(self.rect.centerx, self.rect.top)
            all_sprites.add(lazer)
            lazers.add(lazer)
            self.ammo-=1
            # print(self.ammo)
# randomized enemies that will move down the screen 
class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.transform.scale(mob_image, (40, 40))
        self.image.set_colorkey(WHITE)
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
# class that allows the player to shoot
class Lazer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pg.Surface((5,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# # the class that makes the powerups show up
# class Pow(Sprite):
#     def __init__(self, center):
#         Sprite.__init__(self)
#         self.image = pg.transform.scale(ammo_images, (40, 40))
#         self.image.set_colorkey(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.center = center
#         self.speedy = 5
    
#     def update(self):
#         self.rect.y += self.speedy
#         # kills it if it goes of the screen
#         if self.rect.top > HEIGHT:
#             self.kill()





# where all the new things get created and grouped
all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
lazers = pg.sprite.Group()
powerups = pg.sprite.Group()
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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.pew()

    # updating the bullet collisions 
    all_sprites.update()
    hits = pg.sprite.groupcollide(mobs, lazers, True, True)
    hits = pg.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    
    if len(mobs) == 0:
        for i in range(0,8):
            mob = Mob()
            all_sprites.add(mob)
            # # randomly spawns the powerups 
            # if random.random() > 0.9:
            #     pow = Pow(hit.rect.center)
            #     all_sprites.add(pow)
            #     powerups.add(pow)
            mobs.add(mob)

# This refills the ammo when the player collides with the power up
# hits = pg.sprite.spritecollide(mobs, laser, True,)
# for hit in hits:
#      if hit.type == 'ammo':
        # player.ammo += random.randrange(10, 30)
        # if player.ammo >= 100:
        #     player.ammo = 100
       

    
    # code below creates scrolling background using player speed on the y axis
    # background_rect2.y = background_rect.y - 600
    # background_rect.y+= player.speedy
    # background_rect2.y+= player.speedy

    # when background rect2 swap background on top
    # if background_rect2.y >= 0:
    #     background_rect.y = background_rect.y -600
    
    # this creates the background
    # Shows different things for the background like hp
    screen.fill(LIGHTBLUE)
    # screen.blit(background_image, background_rect)
    # screen.blit(background_image, background_rect2)
    draw_text(screen, str(score), 24, WIDTH / 2, 10)
    draw_text(screen, str(player.ammo), 24, WIDTH / 4, 10) 
    draw_text(screen, str(player.hitpoints), 16, player.rect.x, player.rect.y)

    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()


