import pygame
import time
import random
pygame.init()

#change the values of the below variables to get ur desired color.
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 253, 213)

#the dis_width and dis_height are the scaling of the game window.
dis_width = 1200
dis_height = 700

#change the above things or you can change it from the below line(i.e width and height)
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Classic Snake Game')
clock = pygame.time.Clock()

snake_block = 10 #This is the size of the snake
snake_speed = 25 #This is the Game Difficulty level for  easy:15 Medium:25 Hard : 30 Hardest:40


#You can change the font and its size below:
font_style = pygame.font.SysFont("Times New Roman", 40)
score_font = pygame.font.SysFont("algerian", 35)

#This function displays the score after completing the game
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
#this is the main game loop
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


#this is the iterating part of the game which executes untill u lose
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()


#I have mapped arrow keys to control the game kindly use arrow keys to play ...
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
        dis.fill(white) #change the background color here
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) #change the color of the food here
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)


#This statement stops the game and exits(closes the window created)
    pygame.quit()
    quit()
gameLoop()