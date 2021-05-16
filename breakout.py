import random
import pygame
import sys
class Color:
    green=(0,0,0)
    white=(255,7,255)
    red=(255,0,0)
    blue=(0,0,255)
    yellow=(255,255,0)
class Brick:
    def __init__(self):
        self.w=30
        self.h=20
        self.x=10
        self.y=60
        self.bricks=[]

        for i in range(10):
            self.x=7
            for j in range(16):
                self.bricks.append(pygame.draw.rect(Game.screen,Color.red,[self.x,self.y,self.w,self.h]))
                self.x +=31
            self.y+=21
    def show(self):
        for brick in self.bricks:
            self.co = random.choice(['blue', 'green', 'yellow', 'red'])
            self.area=pygame.draw.rect(Game.screen,self.co,brick)

class Rocket:
    def __init__(self):
        self.w=50
        self.h=10
        self.x=Game.width-20
        self.y=Game.height-50
        self.color=Color.blue
        self.speed=2
        self.score=0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])
    def show(self):
        self.area = pygame.draw.rect(Game.screen,self.color,[self.x,self.y,self.w,self.h])

class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width/2
        self.y = Game.height/2
        self.speed = 3
        self.number=3
        self.color = Color.yellow
        self.x_direction = 1
        self.y_direction = 1
        self.area = pygame.draw.circle(Game.screen, Color.yellow, [self.x, self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.screen, Color.yellow, [self.x, self.y], self.r)

    def move_ball(self):
        self.x += self.speed * self.x_direction
        self.y -= self.speed* self.y_direction
        if self.x > Game.width or self.x < 0:
            self.x_direction *= -1

    def new_ball(self):
        self.x = Game.width/2
        self.y = Game.height/2
class Game:
    width=508
    height=600
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Break Out ")
    clock=pygame.time.Clock()

    @staticmethod
    def play():
        brick=Brick()
        rocket=Rocket()
        ball=Ball()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type==pygame.MOUSEMOTION:
                    rocket.x = pygame.mouse.get_pos()[0]
                    if rocket.x > Game.width - rocket.w:
                        rocket.x = Game.width - rocket.w
            ball.move_ball()
            if ball.y > Game.height:
                ball.number-=1
                ball.new_ball()
                ball.x_direction*=-1

            if ball.area.colliderect(rocket.area):
                ball.y_direction *= -1
                ball.y -=4
            for block in brick.bricks:
                if ball.area.colliderect(block):
                    ball.x_direction*=1
                    ball.y_direction*=-1
                    brick.bricks.remove(block)
                    rocket.score += 1
            if ball.number<0:
                pygame.quit()
                sys.exit()
            Game.screen.fill((0,0,0))

            pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], 10)
            rocket.show()
            ball.show()
            brick.show()

            text = pygame.font.Font('COMIC.TTF', 20)
            txt_score =text.render('score: %d ' % rocket.score, True, (255, 255, 255))
            Game.screen.blit(txt_score, [Game.width-400,15])
            txt_number = text.render('number: %d /3' % ball.number, True, (255, 255, 255))
            Game.screen.blit(txt_number, [Game.width-200, 15])
            pygame.display.update()
            Game.clock.tick(30)

if __name__=="__main__":
    pygame.init()
    Game.play()
