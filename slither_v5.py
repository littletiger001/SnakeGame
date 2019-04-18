# -*- coding: utf-8 -*-
import pygame
import sys
import math

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
    def __init__(self, screen, image_file, num_image,speed):
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
        self.position = [0,0]
        self.num_x = self.set_num(num_image[0])  #[-0.5,0.5], [-1,0,-1],,,
        self.num_y = self.set_num(num_image[1])  #[-0.5,0.5], [-1,0,-1],,,
        print("self.num_x",self.num_x)
        print("self.num_y",self.num_y)
        self.list_backgournd = []
        self.update_background()


    def set_num(self,number):
        return [ x - ((number-1)/2.0) for x in range(0,number)]

    def update_background(self):
        self.list_backgournd = []
        for num_x in self.num_x:
            for num_y in self.num_y:
                #print("num_x,num_y",num_x,num_y)
                self.list_backgournd.append(Background(self.image_file\
                                                       ,[(num_x-0.5)*self.image_width-self.position[0]+self.screen_center_x\
                                                    ,(num_y-0.5)*self.image_height+self.position[1]+self.screen_center_y]))

    #def set_background(self):
    #    tmp_list = []
    #    #print("move_x,move_y",self.move_x,self.move_y)
    #    for bk in self.list_backgournd:
    #        tmp_list.append(bk.move(self.move_x*speed,self.move_y*speed))

    def render(self):
        self.screen.fill([155, 155, 155])
        for bk in self.list_backgournd:
            #print("[bk.rect.left, bk.rect.top]",[bk.rect.left, bk.rect.top])
            self.screen.blit(bk.image, [bk.rect.left, bk.rect.top])


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, imagehead_file,imagebody_file,speed,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.position = initial_position
        self.screen = screen
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0
        self.imagehead = pygame.image.load(imagehead_file)
        self.headrect = self.imagehead.get_rect()
        print("self.headrect",self.headrect)
        self.imagehead_width = self.headrect.width
        self.imagehead_height = self.headrect.height
        self.headrect.left, self.headrect.top = [0+self.screen_center_x-self.imagehead_width/2.0, 0+self.screen_center_y-self.imagehead_height/2.0]

        self.list_hist = []
        self.size = 10
        self.num_body = 20
        self.set_initial_body()
        print("imagebody_file",imagebody_file)
        self.imagebody = pygame.image.load(imagebody_file)
        self.bodyrect = self.imagehead.get_rect()
        print("self.bodyrect",self.bodyrect)
        self.imagebody_width = self.bodyrect.width
        self.imagebody_height = self.bodyrect.height

    def set_initial_body(self):
        for i in range(0,self.num_body):
            self.list_hist.append([0+(i+1)*10,0])

    def get_position(self):
        return self.position

    def update_move(self):
        tmp_list = []
        tmp_hist =[0,0]
        old_hist=[0,0]
        #print("move_x,move_y", self.move_x, self.move_y)
        #print("self.list_hist",self.list_hist)
        tmp_list.append(self.position)
        tmp_list = tmp_list + self.list_hist[:-1]
        #print("tmp_list",tmp_list)
        self.list_hist = tmp_list.copy()
        print("self.list_hist",self.list_hist)
        #sys.exit()

    def render(self):
        #self.screen.fill([155, 155, 155])
        #print("list_hist",self.list_hist)
        for i in range(len(self.list_hist)-1,0,-1):
            self.screen.blit(self.imagebody, [self.headrect.left+(self.list_hist[i][0]-self.position[0])\
                , self.headrect.top-(self.list_hist[i][1]-self.position[1])])
        #print("[bk.rect.left, bk.rect.top]", [self.headrect.left, self.headrect.top])
        self.screen.blit(self.imagehead, [self.headrect.left, self.headrect.top])


pygame.init()
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
speed_persec = 100
update_persec = 10
delay_sec = int(1000/update_persec)
speed = speed_persec / update_persec
initial_position = [0.0,0.0] # <-- Center is [0.0,0.0]
#screen.fill(BLACK)
DynamicBg = DynamicBackground(screen,DIR_INPUT+"\\bk1.png", [20,20],speed)
Player = Player(screen,DIR_INPUT+"\\snakehead_red.png",DIR_INPUT+"\\snakebody_red.png",speed, initial_position)

#pygame.mouse.set_visible(0)
#rect = (200, 100, 100, 100)
#pygame.draw.rect(screen, "RED", rect)
#pygame.display.flip()

running = True
move_x_pic = -speed
move_y_pic = 0

while running:
    screen.fill([155, 155, 155])
    #print("BackGround.rect",BackGround.rect)
    #screen.blit(BackGround.image, (100,100,100,100))
    position = Player.get_position() #[0.0,0.0]
    screen_center_x = screen.get_width()/2.0
    screen_center_y = screen.get_height()/2.0

    mouse_pos = pygame.mouse.get_pos()
    print("mouse_pos",mouse_pos)
    move_x_pic = (mouse_pos[0] - DynamicBg.screen_center_x)
    move_y_pic = -(mouse_pos[1] - DynamicBg.screen_center_y)
    len_pic = math.sqrt(move_x_pic * move_x_pic + move_y_pic * move_y_pic)
    move_x = (move_x_pic / len_pic) * speed
    move_y = (move_y_pic / len_pic) * speed
    print("move_x,move_y,length",move_x,move_y,math.sqrt(move_x * move_x + move_y * move_y))
    position = [x+y for (x, y) in zip(position, [move_x,move_y])]
    print("position",position)

    DynamicBg.position = position
    Player.position = position


    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               pygame.quit()

    DynamicBg.update_background()
    DynamicBg.render()
    Player.update_move()
    Player.render()
    pygame.display.flip()
    #DynamicBg.move_x = 0
    #DynamicBg.move_y = 0
    clock.tick(delay_sec)
    #clock.tick(10000)


pygame.quit()
