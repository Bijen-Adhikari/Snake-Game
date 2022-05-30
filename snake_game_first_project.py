
# First let us import some libraries.

import pygame     #............................................................... Library 1


#Pygame is a set of python modules and it is designed for writing video games. 
#pygame adds functionality on top of the excellent SDL library.
#It includes computer graphics and sound libraries designed to be used with the python programming langugae.


import time     #.................................................................. Library 2


#It allows functionality like getting the current time,
#  pausing the Program from executing, etc. So before starting with this module we need to import it.

import random   #..................................................................Library 3


#The random module is a built-in module to generate the pseudo-random variables. 
# It can be used perform some action randomly such as to get a random number, 
# selecting a random elements from a list, shuffle elements randomly, etc.


#Now,

#Let us define some colors.
gray = (127, 127, 127)
black = pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
magenta = (255, 0, 255)
cyan = (0, 255, 255)

#init() initialize all imported pygame modules is a convenient way to get everything started.
pygame.init()

# Let us define the Window size
window_x_axis=840
window_y_axis=600

#speed of the snake
speed_of_snake=15



# Now, we are Initializing the game window

pygame.display.set_caption('My frist project in python- Snake Game')
game_window=pygame.display.set_mode((window_x_axis,window_y_axis))

#Frames per second (FPS) controller
fps=pygame.time.Clock()

#defining snake default postion
snake_position=[300,250]

#Now, we are about to define the four blocks for the snake body
snake_body= [[300,250],[290,50],[280,50],[270,50]]

#As we are making the snake game, we know that snake eats fruit to grow itself. It is the goal of the game. so, we are defining the position of the fruit

the_position_of_apple=[random.randrange(1,(window_x_axis//10))*10,
                 random.randrange(1,(window_y_axis//10))*10]

#so here,
# >>> 33 //10  
# 3
# >>> 33 //10  * 10
# 30
# >>> 33 //10  * 10 
# 30
# if we get the random value like 33 then it will be 3 then again it will be multiply by 10 and becomes 30
# to get the values like 10 20 30 40...............840 in x axis and same as y axis . 
#example:- 
# x = 15
# y = 2

# print(x // y)
#the floor division // rounds the result down to the nearest whole number

apple_spawn = True  

#setting default snake direction towards the right
direction='RIGHT'
change_to=direction

#The initial value of the score
score=0 

# Now we are defining function to display the score

def show_score(choice,color,font,size):
    #Creating font object score_font
    score_font=pygame.font.SysFont(font,size)

    #create the display surface object
    #score_surface
    score_surface=score_font.render('score:'+str(score),True,color)

    #Now creating a rectangular object for the text.
    #Surface object.
    score_rect=score_surface.get_rect()

    #now displaying the text
    game_window.blit(score_surface,score_rect)

#Creating the game over function

def game_over():

    #creating font object my_font
    my_font=pygame.font.SysFont('times new roman',50)

    #creating a text surface on which text will be drawn

    game_over_surface=my_font.render('Your Score is :'+str(score), True,red)

    #create a rectangular object for the text
    #surface object
    game_over_rect=game_over_surface.get_rect()

    #setting postion of the text
    game_over_rect.midtop = (window_x_axis/2,window_y_axis/4)

    #blit will draw the text on screen
    game_window.blit(game_over_surface,game_over_rect)
    pygame.display.flip()

    #NOw after 3 seconds the program will be quit
    time.sleep(2)

    #deactivating pygame library
    pygame.quit()

    #quit the program
    quit()

#Heading towards the main function

while True:

    #handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                #if two keys pressed simultaneously then we dont want sanke to move into two directions
                #simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #moving the snake

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    

    #Snake body growing mechanism
    #if fruits and snakes collide then score will be incremented by 10

    snake_body.insert(0,list(snake_position))
    if snake_position[0]==the_position_of_apple[0] and snake_position[1]==the_position_of_apple[1]:
        score+=10
        apple_spawn=False
    else: 
       # print("before pop ", snake_body)
        snake_body.pop()
       # print("affter pop", snake_body)
    
    if not apple_spawn:
       the_position_of_apple =[random.randrange(1,(window_x_axis//10))*10,
                        random.randrange(1,(window_y_axis//10))*10]
    
    apple_spawn=True
    game_window.fill(green)

    for pos in snake_body:
        pygame.draw.rect(game_window,gray,pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(game_window,red,pygame.Rect(the_position_of_apple[0],the_position_of_apple[1],10,10))

    #game over condition
    if snake_position[0] < 0 or snake_position[0] > window_x_axis-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y_axis-10:
        game_over()
    #Condition for Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0]==block[0] and snake_position[1]==block[1]:
            print("touched snake bvody", snake_position, block, snake_body)
            game_over()
    #displaying the score in the game continuously

    #displaying score continuosly
    show_score(1,white,'times new roman',20)

    #refresh game screen
    pygame.display.update()
    #Frame Per second / Refresh Rate
    fps.tick(speed_of_snake)
    if score==20:
        speed_of_snake=20
        
    if score==50:
        speed_of_snake=30
        
    if score==70:
       
        speed_of_snake=35