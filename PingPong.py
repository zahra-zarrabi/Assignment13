import random
import sys

import pygame
import time

class Color:
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    blue=(0,0,255)
    yellow=(255,255,0)

class Rocket:
    def __init__(self,x,y,color):
        self.w=10
        self.h=50
        self.x=x
        self.y=y
        self.color=color
        self.speed=7
        self.score=0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])
    def show(self):
        self.area=pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])
    def move_rocket(self,b):
        if self.y < b.y:
            self.y+=self.speed
        elif self.y>b.y:
            self.y -=self.speed
        if self.y<0:
            self.y=0
        if self.y>Game.height-self.h:
            self.y=Game.height-self.h

class Ball:
    def __init__(self):
        self.r=10
        self.x=random.randint(40,Game.width-100)
        self.y=random.randint(40,Game.height-100)
        self.speed=3
        self.color=Color.yellow
        self.x_direction=-1
        self.y_direction=1
        self.area = pygame.draw.circle(Game.screen, Color.yellow, [self.x, self.y], self.r)
    def show(self):
        self.area=pygame.draw.circle(Game.screen,Color.yellow,[self.x,self.y],self.r)
    def move_ball(self):
        self.x += self.speed * self.x_direction
        self.y += self.speed * self.y_direction
        if self.y>Game.height or self.y<0:
            self.y_direction *= -1
    def new_ball(self):
        self.x=random.randint(0,Game.width-10)
        self.y=random.randint(0,Game.height-10)
class Game:
    width=700
    height=400
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Ping Pong")
    clock=pygame.time.Clock()
    fps=50

    @staticmethod
    def play():
        me = Rocket(20, Game.height/2, Color.red)
        computer=Rocket(Game.width-30,Game.height/2,Color.blue)
        ball=Ball()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1]
                    if me.y>Game.height-me.h:
                        me.y=Game.height-me.h

            ball.move_ball()
            if ball.x_direction > 0:
                computer.move_rocket(ball)
            if ball.x<0:
                computer.score+=1
                ball.new_ball()
            elif ball.x>Game.width:
                me.score+=1
                ball.new_ball()


            if me.area.colliderect(ball.area):
                ball.x_direction *= -1
                ball.x += 5
            elif computer.area.colliderect(ball.area):
                ball.x_direction *= -1
                ball.x -= 5



            Game.screen.fill((Color.black))

            pygame.draw.rect(Game.screen,Color.white,[0,0,Game.width,Game.height],10)
            pygame.draw.aaline(Game.screen,Color.white,[Game.width/2,0],[Game.width/2,Game.height])

            me.show()
            computer.show()
            ball.show()

            if computer.score > 7:
                print('computer win')
                pygame.quit()
                sys.exit()
            if me.score > 7:
                print('you win')
                pygame.quit()
                sys.exit()



            text = pygame.font.Font('COMIC.TTF', 20)
            txt_score_me = text.render('score: %d' % me.score, True, (255, 255, 255))
            txtrect = txt_score_me.get_rect()
            txtrect.center = (Game.width // 3, 50)
            txt_score_computer = text.render('score: %d' % computer.score, True, (255, 255, 255))
            txtrect2 = txt_score_computer.get_rect()
            txtrect2.center = (Game.width - 250, 50)
            Game.screen.blit(txt_score_me, txtrect)
            Game.screen.blit(txt_score_computer, txtrect2)

            pygame.display.update()
            Game.clock.tick(Game.fps)

if __name__=="__main__":
    pygame.init()
    Game.play()

