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

    def move(self,move_x,move_y):
        self.rect.left, self.rect.top = [self.rect.left+move_x, self.rect.top+move_y]
        return self

class DynamicBackground(pygame.sprite.Sprite):
    def __init__(self, screen, image_file, num_image,):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.screen = screen
        print("screen surface:",screen.get_width())
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0
        self.screen.fill([155, 155, 155])
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        print("self.rect",self.rect)
        self.image_width = self.rect.width
        self.image_height = self.rect.height
        print("self.image_width",self.image_width)
        print("self.image_height",self.image_height)
        self.move_x = 0
        self.move_y = 0
        self.num_x = self.set_num(num_image[0])
        self.num_y = self.set_num(num_image[1])
        print("self.num_x",self.num_x)
        print("self.num_y",self.num_y)
        self.list_backgournd = []
        self.set_background()


    def set_num(self,number):
        return [ x - ((number-1)/2.0) for x in range(0,number)]

    def set_background(self):
        for num_x in self.num_x:
            for num_y in self.num_y:
                print("num_x,num_y",num_x,num_y)
                self.list_backgournd.append(Background(self.image_file\
                                                       ,[(num_x-0.5)*self.image_width-self.move_x+self.screen_center_x\
                                                    ,(num_y-0.5)*self.image_height-self.move_y+self.screen_center_y]))

    def update_move(self):
        tmp_list = []
        print("move_x,move_y",self.move_x,self.move_y)
        for bk in self.list_backgournd:
            tmp_list.append(bk.move(self.move_x,self.move_y))

    def render(self):
        self.screen.fill([155, 155, 155])
        for bk in self.list_backgournd:
            print("[bk.rect.left, bk.rect.top]",[bk.rect.left, bk.rect.top])
            self.screen.blit(bk.image, [bk.rect.left, bk.rect.top])


class Ship(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
#screen.fill(BLACK)
DynamicBg = DynamicBackground(screen,DIR_INPUT+"\\bk1.png", [8,8])

#pygame.mouse.set_visible(0)
#rect = (200, 100, 100, 100)
#pygame.draw.rect(screen, "RED", rect)
#pygame.display.flip()

flag = 0
while flag == 0:
    screen.fill([155, 155, 155])
    #print("BackGround.rect",BackGround.rect)
    #screen.blit(BackGround.image, (100,100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: flag = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                DynamicBg.move_y = 1
            if event.key == pygame.K_DOWN:
                DynamicBg.move_y = -1
            if event.key == pygame.K_LEFT:
                DynamicBg.move_x = 1
            if event.key == pygame.K_RIGHT:
                DynamicBg.move_x = -1
    DynamicBg.update_move()
    DynamicBg.render()
    pygame.display.flip()
    #DynamicBg.move_x = 0
    #DynamicBg.move_y = 0
    clock.tick(60)

pygame.quit()
