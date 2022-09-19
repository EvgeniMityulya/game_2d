from distutils.spawn import spawn
import pygame
from settings import *
from tile import Bench, Bench_L, Bench_R, Box, Box_s, Bush, Chest, Column, Column_low, Column_symb, Grave_horizontal, Grave_vertical, Pit, Portal, Statue, Tile, Tree1, Tree2
from player import Player
from debug import debug

class Level:
    def __init__(self):
        
        # Get display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # Sprite
        self.create_map()
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'g':
                    Grave_vertical((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'h':
                    Grave_horizontal((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 's':
                    Statue((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'b':
                    Bench((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'c':
                    Column((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'cs':
                    Column_symb((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 't1':
                    Tree1((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 't2':
                    Tree2((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'z':
                    Portal((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'k':
                    Bush((x, y), [self.visible_sprites, self.obstacles_sprites])
                elif col == 'bl':
                    Bench_L((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'br':
                    Bench_R((x, y), [self.visible_sprites, self.obstacles_sprites])  
                elif col == 'bh':
                    Box((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'bs':
                    Box_s((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'q':
                    Chest((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'cl':
                    Column_low((x, y), [self.visible_sprites, self.obstacles_sprites]) 
                elif col == 'o':
                    Pit((x, y), [self.visible_sprites, self.obstacles_sprites]) 

                elif col == 'p':
                    room = int(input('What do you see? \n 1 - Old pit\n 2 - Graveyard\n 3 - Chest \n 4 - Portal \nType number...\n'))
                    if room == 1:
                        spawn_x = 290
                        spawn_y = 355
                        print('Successfully! You spawned close to Old pit.\n'
                            'Info:'
                            '\n On the right side Graveyard. Brr...'
                            '\n At the bottom is a Chest. Go here!!!'
                            '\n There is a Portal in the corner. Maybe there are aliens there?!'
                            '\n There are Statues in the center. I wonder what they are!'
                            )

                    elif room == 2:
                        spawn_x = 940
                        spawn_y = 222
                        print('Successfully! You spawned close to Graveyard. Brr...\n'
                            'Info:'
                            '\n On the left side Old pit. Sounds scary.'
                            '\n At the bottom is a Portal. Maybe there are aliens there?!'
                            '\n There is a Chest in the corner. Go here!!!'
                            '\n There are Statues in the center. I wonder what they are!'
                            )

                    elif room == 3:
                        spawn_x = 319
                        spawn_y = 850
                        print('Successfully! You spawned close to Chest. YEAH!\n'
                            'Info:'
                            '\n On the right side is a Portal. Maybe there are aliens there?!'
                            '\n At the top is a Old pit. Sounds scary.'
                            '\n There is a Graveyard in the corner. Brr...'
                            '\n There are Statues in the center. I wonder what they are!'
                            )

                    elif room == 4:
                        spawn_x = 870
                        spawn_y = 824
                        print('Successfully! You spawned close to Portal. Where is Aliens???!\n'
                            'Info:'
                            '\n On the left side is a Chest. Go here!!!'
                            '\n At the top is a Graveyard. Brr...'
                            '\n There is a Old pit in the corner. Sounds scary.'
                            '\n There are Statues in the center. I wonder what they are!'
                            )

                    else:
                        spawn_x = 590
                        spawn_y = 620
                        print('DASDADADA!!! You spawned close to Statues, because you crashed the mechanism.\n'
                            'Info:'
                            '\n On the top left side Old pit. Sounds scary.'
                            '\n There is a Graveyard in the top right corner. Brr...'
                            '\n At the bottom left is a Chest. Go here!!!'
                            '\n There is a Portal at the bottom right. Maybe there are aliens there?!'
                            )

                    self.player = Player((spawn_x,spawn_y), [self.visible_sprites], self.obstacles_sprites)
            

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) :

        # General setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('images/map2.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (-600,-400))

    def custom_draw(self, player):

        # Gettinng offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Drawing floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)