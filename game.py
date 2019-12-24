import pygame
import random
import math

directions={'left':1,'right':2,'up':3,'down':4}

class Game:
    gameRunning = True
    board = None
    surface = None
    speed = 8
    s = None
    f = None

    def gameInit():
        pygame.init()
        Game.board = pygame.display.set_mode((500,500))
        pygame.display.set_caption('SNAKE!')
        Snake.surface = Game.board
        Food.surface = Game.board
        f = Food()
        s = Snake()
        while Game.gameRunning:
            pygame.time.delay(math.floor(1000/(Game.speed)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game.gameRunning = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    s.dir=directions['down']
                if keys[pygame.K_UP]:
                    s.dir=directions['up']
                if keys[pygame.K_RIGHT]:
                    s.dir=directions['right']
                if keys[pygame.K_LEFT]:
                    s.dir=directions['left']

            Game.update(s,f)

    def update(s,f):
        Game.board.fill((0,0,0))
        f.update()
        f.body = s.update(f.body)
        print(str(s.length))
        pygame.display.update()


class Snake:
    import pygame
    surface = None
    size = 10
    color = (0,255,255)
    def __init__(self):
        self.x=250
        self.y=250
        self.dir = directions['right']
        self.head = pygame.Rect(self.x,self.y,Snake.size,Snake.size)
        self.body = None
        self.length = 1
#at some point, have the body move by checking the piece in body right before it's old direction(before being update) and move in that direction
# for keys, go into for loop above and look up K_DOWN, etc

    def drawSnake(self):
        self.head = pygame.Rect(self.x,self.y,Snake.size,Snake.size)
        pygame.draw.rect(Snake.surface, Snake.color, self.head)

    def moveSnake(self):
        print('moving' + str(random.randint(0,100)))
        if self.dir == directions['right']:
            self.x+=10
        if self.dir == directions['left']:
            self.x-=10
        if self.dir == directions['up']:
            self.y-=10
        if self.dir == directions['down']:
            self.y+=10

    def update(self,fbody):
        if self.head.contains(fbody):
            self.length +=1
            self.add()
            return Food.newBody()
        self.moveSnake()
        self.drawSnake()


class Food:
    surface = None
    size = 10
    color = (0,255,0)
    def __init__(self):
        self.x = (random.randint(0,1000)%25)*10
        self.y = (random.randint(0,1000)%25)*10
        self.body = None
    def update(self):
        self.body = pygame.Rect(self.x, self.y, Food.size, Food.size)
        pygame.draw.rect(Food.surface,Food.color,self.body)
    def newBody():
                newx = (random.randint(0,1000)%25)*10
                newy = (random.randint(0,1000)%25)*10
                newbody = pygame.Rect(newx, newy, Food.size, Food.size)
                return newbody


if __name__=='__main__':
    Game.gameInit()
