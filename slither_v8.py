# -*- coding: utf-8 -*-
import pygame
import sys
import math
import random
import time

CWD = "D:\\SG\\P\\Game\\Snake"
DIR_INPUT = CWD + "\\Input"

BLACK = (0, 0, 0)

class Start_screen(pygame.sprite.Sprite):
    def __init__(self, screen, title_file, start_file):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.screen = screen
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0

        self.title = pygame.image.load(title_file).convert_alpha()
        self.start = pygame.image.load(start_file).convert_alpha()

        self.title_rect = self.title.get_rect()
        self.start_rect = self.start.get_rect()

        self.titlegap_y = 100
        self.startgap_y = -100

        self.flag_startscreen = True
        self.flag_setsnake = False

    def render(self):
        self.screen.fill([0, 0, 0])
        self.screen.blit(self.title, [self.screen_center_x - self.title_rect.width/2.0, self.screen_center_y - self.title_rect.height/2.0 - self.titlegap_y])
        self.screen.blit(self.start, [self.screen_center_x - self.start_rect.width/2.0, self.screen_center_y - self.title_rect.height/2.0 - self.startgap_y])

    def check_clickstart(self,pos_cursol):
        print("pos_cursol",pos_cursol)
        if (pos_cursol[0] > (self.screen_center_x - self.title_rect.width/2.0))\
            and (pos_cursol[0] < (self.screen_center_x + self.title_rect.width/2.0))\
            and (pos_cursol[1] > (self.screen_center_y - self.title_rect.height/2.0 - self.startgap_y))\
            and (pos_cursol[1] < (self.screen_center_y + self.title_rect.height/2.0 - self.startgap_y)):
            self.flag_startscreen = False
        else:
            self.flag_startscreen = True


class Background(pygame.sprite.Sprite):
    def __init__(self, screen, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.screen = screen
        print("screen width:",screen.get_width())
        print("screen height:",screen.get_height())
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0
        self.position_init = location
        self.position = [0,0]
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect()
        print("self.rect:",self.rect)
        self.rect.left, self.rect.top = [self.position_init[0]-self.rect.left/2.0, self.position_init[1]-self.rect.top/2.0]
        print("self.rect.left:",self.rect.left)
        print("self.rect.top:",self.rect.top)

    def update_background(self):
        self.rect.left, self.rect.top = [self.position_init[0]-self.rect.left/2.0-self.position[0]\
                                        ,self.position_init[1]-self.rect.left/2.0+self.position[1]]
        return self

    def render(self):
        self.screen.fill([0, 0, 0])
        self.screen.blit(self.image, [self.rect.left, self.rect.top])
'''
class DynamicBackground(pygame.sprite.Sprite):
    def __init__(self, screen, image_file, num_image,speed):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.screen = screen
        print("screen surface:",screen.get_width())
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0
        self.screen.fill([155, 155, 155])
        self.image_file = image_file
        self.image = pygame.image.load(image_file).convert()
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
        self.screen.fill([0, 0, 0])
        for bk in self.list_backgournd:
            #print("[bk.rect.left, bk.rect.top]",[bk.rect.left, bk.rect.top])
            if (bk.rect.left + self.image_width >= 0.0) and (bk.rect.left <= self.screen_center_x*2) and (bk.rect.top + self.image_height >= 0.0) and (bk.rect.top <= self.screen_center_y*2):
                self.screen.blit(bk.image, [bk.rect.left, bk.rect.top])
'''

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, imagehead_file,imagebody_file,speed,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.position = initial_position
        self.screen = screen
        self.screen_center_x = screen.get_width()/2.0
        self.screen_center_y = screen.get_height()/2.0
        self.imagehead = pygame.image.load(imagehead_file).convert_alpha()
        self.headrect = self.imagehead.get_rect()
        #print("self.headrect",self.headrect)
        self.imagehead_width = self.headrect.width
        self.imagehead_height = self.headrect.height
        self.headrect.left, self.headrect.top = [0+self.screen_center_x-self.imagehead_width/2.0, 0+self.screen_center_y-self.imagehead_height/2.0]

        self.list_hist = []
        self.size = 10
        self.num_body = 100
        self.set_initial_body()
        #print("imagebody_file",imagebody_file)
        self.imagebody = pygame.image.load(imagebody_file).convert_alpha()
        self.bodyrect = self.imagehead.get_rect()
        #print("self.bodyrect",self.bodyrect)
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
        #print("self.list_hist",self.list_hist)
        #sys.exit()

    def render(self):
        #self.screen.fill([155, 155, 155])
        #print("list_hist",self.list_hist)
        for i in range(len(self.list_hist)-1,0,-1):
            self.screen.blit(self.imagebody, [self.headrect.left+(self.list_hist[i][0]-self.position[0])\
                , self.headrect.top-(self.list_hist[i][1]-self.position[1])])
        #print("[bk.rect.left, bk.rect.top]", [self.headrect.left, self.headrect.top])
        self.screen.blit(self.imagehead, [self.headrect.left, self.headrect.top])

class Snake(pygame.sprite.Sprite):
    def __init__(self, screen, Bg, imagehead_file,imagebody_file,speed,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_center_x = 0.0
        self.screen_center_y = 0.0
        self.imagehead = pygame.image.load(imagehead_file).convert_alpha()
        self.headrect = self.imagehead.get_rect()
        #print("self.headrect",self.headrect)
        self.imagehead_width = self.headrect.width
        self.imagehead_height = self.headrect.height

        self.bg_width = Bg.rect.width
        self.bg_height = Bg.rect.height
        #print("self.bg_width",self.bg_width)
        #print("self.bg_height",self.bg_height)
        self.position = [random.randint(-self.bg_width/2.0+15, self.bg_width/2.0-15), random.randint(-self.bg_height/2.0+15, self.bg_height/2.0-15)]
        self.headrect.left, self.headrect.top = [self.position[0] - self.imagehead_width / 2.0, self.position[0] - self.imagehead_height / 2.0]

        self.list_hist = []
        self.size = 10
        self.num_body = 100
        self.set_initial_body()

        #print("imagebody_file",imagebody_file)
        self.imagebody = pygame.image.load(imagebody_file).convert_alpha()
        self.bodyrect = self.imagehead.get_rect()
        #print("self.bodyrect",self.bodyrect)
        self.imagebody_width = self.bodyrect.width
        self.imagebody_height = self.bodyrect.height

        self.speed = speed
        self.next_position = [random.randint(-self.bg_width/2.0+15, self.bg_width/2.0-15), random.randint(-self.bg_height/2.0+15, self.bg_height/2.0-15)]
        #print("self.next_position",self.next_position)


    def set_initial_body(self):
        for i in range(0,self.num_body):
            self.list_hist.append([self.position[0],self.position[1]+i*10])

    def get_position(self):
        return self.position

    def set_screen_center(self,position_center):
        self.screen_center_x = position_center[0]
        self.screen_center_y = position_center[1]

    def update_move(self):

        if math.sqrt((self.next_position[0] - self.position[0]) * (self.next_position[0] - self.position[0])\
                    +(self.next_position[1] - self.position[1]) * (self.next_position[1] - self.position[1])) < 50.0:

            self.next_position = [random.randint(-self.bg_width/2.0+15, self.bg_width/2.0-15), random.randint(-self.bg_height/2.0+15, self.bg_height/2.0-15)]
            print("Renewed Next Position:",self.next_position)
            #sys.exit()

        move_x_pic = (self.next_position[0]  - self.position[0])
        move_y_pic = (self.next_position[1] - self.position[1])
        len_pic = math.sqrt(move_x_pic * move_x_pic + move_y_pic * move_y_pic)
        move_x = (move_x_pic / len_pic) * self.speed
        move_y = (move_y_pic / len_pic) * self.speed
        #print("move_x,move_y,length", move_x, move_y, math.sqrt(move_x * move_x + move_y * move_y))
        self.position = [x + y for (x, y) in zip(self.position, [move_x, move_y])]
        #print("self.position", self.position)

        tmp_list = []
        tmp_hist =[0,0]
        old_hist=[0,0]
        #print("move_x,move_y", self.move_x, self.move_y)
        #print("self.list_hist",self.list_hist)
        tmp_list.append(self.position)
        tmp_list = tmp_list + self.list_hist[:-1]
        #print("tmp_list",tmp_list)
        self.list_hist = tmp_list.copy()
        #print("self.list_hist",self.list_hist)
        #sys.exit()

    def render(self):
        #self.screen.fill([155, 155, 155])
        #print("list_hist",self.list_hist)
        for i in range(len(self.list_hist)-1,0,-1):
            self.screen.blit(self.imagebody, [self.list_hist[i][0]-self.screen_center_x + self.bg_width/2.0 - self.bodyrect.width/2.0\
                , -(self.list_hist[i][1]-self.screen_center_y) + self.bg_height/2.0 - self.bodyrect.height/2.0])
        #print("[bk.rect.left, bk.rect.top]", [self.headrect.left, self.headrect.top])
        self.screen.blit(self.imagehead, [self.list_hist[0][0]-self.screen_center_x + self.bg_width/2.0 - self.bodyrect.width/2.0\
                , -(self.list_hist[0][1]-self.screen_center_y) + self.bg_height/2.0 - self.bodyrect.height/2.0])


pygame.init()
screen = pygame.display.set_mode((1600,1200))
clock = pygame.time.Clock()
speed_persec = 200
update_persec = 25
delay_sec = int(1000/update_persec)
speed = speed_persec / update_persec
initial_position = [0.0,0.0] # <-- Center is [0.0,0.0]
num_Snake = 3


#screen.fill(BLACK)
Start_screen = Start_screen(screen,DIR_INPUT+"\\title1_startscreen.png",DIR_INPUT+"\\start1_stratscreen.png")
Bg = Background(screen,DIR_INPUT+"\\bk1_mid.png", [0,0],speed)
#DynamicBg = DynamicBackground(screen,DIR_INPUT+"\\bk1_large.png", [1,1],speed)
#DynamicBg = DynamicBackground(screen,DIR_INPUT+"\\bk1.png", [10,10],speed)
Player = Player(screen,DIR_INPUT+"\\snakehead_red.png",DIR_INPUT+"\\snakebody_red.png",speed, initial_position)
list_snake = []
for i in range(0,num_Snake):
    list_snake.append(Snake(screen,Bg,DIR_INPUT+"\\snakehead_blue.png",DIR_INPUT+"\\snakebody_blue.png",speed, initial_position))

#pygame.mouse.set_visible(0)
#rect = (200, 100, 100, 100)
#pygame.draw.rect(screen, "RED", rect)
#pygame.display.flip()

running = True
move_x_pic = -speed
move_y_pic = 0

while running:

    if Start_screen.flag_startscreen == True:

        if Start_screen.flag_setsnake == False:
            list_snake = []
            for i in range(0, num_Snake):
                list_snake.append(
                    Snake(screen, Bg, DIR_INPUT + "\\snakehead_blue.png", DIR_INPUT + "\\snakebody_blue.png", speed,
                          initial_position))
            Start_screen.flag_setsnake = True

        Start_screen.render()
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            print("1:event type",event.type)
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                Start_screen.check_clickstart(pygame.mouse.get_pos())
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   pygame.quit()


    else:


        events = pygame.event.get()
        for event in events:
            print("2:event type", event.type)
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


        screen.fill([0, 0, 0])
        #print("BackGround.rect",BackGround.rect)
        #screen.blit(BackGround.image, (100,100,100,100))
        position = Player.get_position() #[0.0,0.0]
        screen_center_x = screen.get_width()/2.0
        screen_center_y = screen.get_height()/2.0

        mouse_pos = pygame.mouse.get_pos()
        #print("mouse_pos",mouse_pos)
        #move_x_pic = (mouse_pos[0] - DynamicBg.screen_center_x)
        #move_y_pic = -(mouse_pos[1] - DynamicBg.screen_center_y)
        move_x_pic = (mouse_pos[0] - Bg.screen_center_x)
        move_y_pic = -(mouse_pos[1] - Bg.screen_center_y)
        len_pic = math.sqrt(move_x_pic * move_x_pic + move_y_pic * move_y_pic)
        move_x = (move_x_pic / len_pic) * speed
        move_y = (move_y_pic / len_pic) * speed
        #print("move_x,move_y,length",move_x,move_y,math.sqrt(move_x * move_x + move_y * move_y))
        position = [x+y for (x, y) in zip(position, [move_x,move_y])]
        #print("position",position)

        #DynamicBg.position = position
        Bg.position = position
        Player.position = position
        for i in range(len(list_snake)):
            list_snake[i].set_screen_center(position)


        # Crash Judge
        # Lose
        for i in range(len(list_snake)):
            tmp_list_length = [math.sqrt((tmp_position[0] - position[0])**2 + (tmp_position[1] - position[1])**2) for tmp_position in list_snake[i].list_hist]
            min_length = min(tmp_list_length)
            #print("Snake Head Min Length",i,min_length)
            if min_length < 10:
                print("You lose!!")
                time.sleep(1)
                Start_screen.flag_startscreen = True
                Start_screen.flag_setsnake = False

        # Kill Snake
        tmp_list_snake=[]
        for i in range(len(list_snake)):
            tmp_list_length = [math.sqrt((list_snake[i].list_hist[0][0] - tmp_position[0])**2 + (list_snake[i].list_hist[0][1] - tmp_position[1])**2) for tmp_position in Player.list_hist]
            min_length = min(tmp_list_length)
            #print("Player Head Min Length",min_length)
            if min_length < 10:
                print("You Win!!")
            else:
                tmp_list_snake.append(list_snake[i])

        list_snake = tmp_list_snake

        #DynamicBg.update_background()
        #DynamicBg.render()
        Bg.update_background()
        Bg.render()
        for i in range(len(list_snake)):
            list_snake[i].update_move()
            list_snake[i].render()
        Player.update_move()
        Player.render()
        #pygame.display.update([0,0,600,600])
        pygame.display.update()



        if len(list_snake)<1:
            time.sleep(1)
            Start_screen.flag_startscreen = True
            Start_screen.flag_setsnake = False


        #DynamicBg.move_x = 0
        #DynamicBg.move_y = 0
        clock.tick(delay_sec)
        #clock.tick(10000)

time.sleep(2)
#pygame.quit()
