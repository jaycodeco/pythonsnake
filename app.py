import pygame
import sys
import random

class snake(object):
    def __init__(self):
        self.length = 1
        self.pos =[((DISPLAY_WIDTH/2)-10, (DISPLAY_HEIGHT/2)-10)]
        self.direction = random.choice([UP,DOWN])
        self.color = (27,37,57)
    
    def get_head_pos(self):
        return self.pos[0]
    
    def turn(self,point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_pos()
        x, y= self.direction
        new = (((cur[0]+(x*GRID_SIZE))%DISPLAY_WIDTH), ((cur[1]+(y*GRID_SIZE))%DISPLAY_HEIGHT))
        if len(self.pos)>2 and new in self.pos[2:]:
            self.reset()
        else:
            self.pos.insert(0, new)
            if len(self.pos)>self.length:
                self.pos.pop()
    
    def reset(self):
        self.__init__()
    
    def render(self, surface):
        for p in self.pos:
            cell = pygame.Rect((p[0],p[1]), (GRID_SIZE,GRID_SIZE))
            pygame.draw.rect(surface, self.color, cell)
            # pygame.draw.rect(surface, (93, 216, 188), cell, 1)
    
    def handle_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.turn(UP)
                elif ev.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif ev.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif ev.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
    

class food(object):
    def __init__(self):
        self.pos = (0,0)
        self.color = (255,0,0)
        self.new_pos()
    
    def new_pos(self):#a random position
        self.pos = (random.randint(0, GRID_WIDTH-1)*GRID_SIZE, random.randint(0, GRID_HEIGHT-1)*GRID_SIZE)
    
    def render(self, surface):
        cell = pygame.Rect((self.pos[0],self.pos[1]), (GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(surface, self.color, cell)
        pygame.draw.rect(surface, (150, 0, 0), cell, 5)
    
    

def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y)%2==0:
                white_tile = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (50, 200, 50), white_tile)
            else:
                black_tile = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (0,0,0), black_tile)


#some vars
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT =500

GRID_SIZE = 20
GRID_WIDTH =DISPLAY_HEIGHT/GRID_SIZE
GRID_HEIGHT =DISPLAY_WIDTH/GRID_SIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0,32)
    
    surface = pygame.Surface(screen.get_size()).convert()
    # draw_grid(surface)
    
    viper = snake()
    apple = food()
    score =0
    
    
    while(1):
        clock.tick(5)
        viper.handle_events()
        draw_grid(surface)
        viper.move()
        if viper.get_head_pos() == apple.pos:
            viper.length += 1
            score += 1
            apple.new_pos()
        
        viper.render(surface)
        apple.render(surface)
        screen.blit(surface, (0,0))
        pygame.display.update()

main()