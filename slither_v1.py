# -*- coding: utf-8 -*-
import pygame

CWD = "D:\\SG\\P\\Game\\Snake"
DIR_INPUT = CWD + "\\Input"

BLACK = (0, 0, 0)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Ship(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode((50,50))
clock = pygame.time.Clock()
#screen.fill(BLACK)
BackGround = Background(DIR_INPUT+"\\bk1.png", [0,0])

#pygame.mouse.set_visible(0)
#rect = (200, 100, 100, 100)
#pygame.draw.rect(screen, "RED", rect)
#pygame.display.flip()

flag = 0
while flag == 0:
    screen.fill([155, 155, 155])
    print("BackGround.rect",BackGround.rect)
    screen.blit(BackGround.image, BackGround.rect)
    #screen.blit(BackGround.image, (100,100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: flag = 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
