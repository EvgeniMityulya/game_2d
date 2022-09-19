import pygame
from settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/wall1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-30, -10)

class Statue(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/statue.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-127, -100)

class Grave_vertical(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/grave_vertical.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-63, -40)

class Grave_horizontal(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/grave_horizontal.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-40, -60)

class Bench(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/bench.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-50, -63)

class Bench_L(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/bench_l.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-63, -30)

class Bench_R(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/bench_r.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-50, -63)

class Column(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/column.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-127, -110)

class Column_symb(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/column_symb1.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-127, -110)

class Chest(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/chest.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-60, -40)

class Bush(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/bush1.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-60, -60)

class Box(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/box.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-60, -40)

class Box_s(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/box_s.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-60, -40)

class Tree1(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/tree1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.hitbox = self.rect.inflate(-110, -60)

class Tree2(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/tree2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.hitbox = self.rect.inflate(-90, -50)

class Portal(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/portal.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.hitbox = self.rect.inflate(-30, -10)

class Pit(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/pit.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-40, -20)

class Column_low(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('images/column_low.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.inflate(-63, -30)