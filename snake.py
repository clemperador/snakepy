import pygame
import time
import random

SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
dis=pygame.display.set_mode((800,600))
dis.fill(SHADOW)
pygame.display.set_caption('LA CULEBRA')

x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0

snake_speed= 30
snake_block = 10

dis_width = 800
dis_height  = 600

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def message2(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/10, dis_height/10])

game_over = False

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    
    while not game_over:

        while game_close == True:
            dis.fill(WHITE)
            message("presiona j para jugar denuevo", RED)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(WHITE)
        pygame.draw.rect(dis, BLACK, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, LIGHTGREEN, [foodx, foody, snake_block, snake_block])
    
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            print("mmmmmmm")
    
        clock.tick(snake_speed)

    message("Thank you for playing.", RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()

gameLoop()