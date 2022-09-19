from cmath import rect
import pygame
from settings import *
from os import walk
from debug import debug, debug1

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("images/kaneki2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)

        # Graphics setup
        self.import_assets()
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = self.status + '_idle'




    def import_folder(self, path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
        return surface_list


    def import_assets(self):
        character_path = 'images/player/'
        self.animations = {
            'up': [], 
            'down': [], 
            'left': [], 
            'right': [],
            'up_idle': [],
            'down_idle': [],
            'left_idle': [],
            'right_idle': [],
            }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = self.import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        # Movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):

                    # Moving right
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left

                    # Moving left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):

                    # Moving down
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top

                    # Moving up
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def animate(self):
        animation = self.animations[self.status]

        # Loop animations
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if (self.rect.x > 484 and self.rect.x < 735) and (self.rect.y > 511 and self.rect.y < 707):
            self.room_status = 'Statues'
        elif (self.rect.x > 640 and self.rect.x < 1184) and (self.rect.y > 29 and self.rect.y < 579):
            self.room_status = 'Graveyard'
        elif (self.rect.x > 32 and self.rect.x < 576) and (self.rect.y > 29 and self.rect.y < 579):
            self.room_status = 'Old pit'
        elif (self.rect.x > 640 and self.rect.x < 1184) and (self.rect.y > 637 and self.rect.y < 1219):
            self.room_status = 'Portal'
        elif (self.rect.x > 32 and self.rect.x < 576) and (self.rect.y > 637 and self.rect.y < 1219):
            self.room_status = 'Chest'
        else:
            self.room_status = 'Between'



    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
        debug(self.rect)
        debug1(self.room_status)