import pygame as pg,sys
from pygame.locals import *
import time 

# Global game variables 
XO = 'x'
winner = None 
draw = False 
width = 400
height = 400 
white = (255,255,255)
line_colour = (10,10,10)
TTT = [ [None] *3, [None] *3, [None]*3 ]#The tic tac toe board, currently holds nine None values

#Font Colours 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)


#Initialization (assignment) of pygame window using pygame methods 

# 'pg' is the alias for pygame as specified in line 1 
# .init is always needed in pygame as it initializes pygame and imports all necessary modules 
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe by Mac")

#open images
loadscreen_image = pg.image.load ('C:/Users/mcant/Desktop/test/.venv/tic-tacs-1473284.jpg')
x_image = pg.image.load ('C:/Users/mcant/Desktop/test/.venv/X.png')
o_image = pg.image.load ('C:/Users/mcant/Desktop/test/.venv/O.png')
#Add text to the loadscreen image
#sprite = pg.sprite.Sprite()
#sprite.loadscreen_image = loadscreen_image
#sprite.rect = loadscreen_image.get_rect()

font = pg.font.SysFont('Sans', 200)
text1 = font.render(' Tic tac toe by Mac', True, (RED))
text2 = font.render('Thanks for playing, Mac', True,(RED) )
loadscreen_image.blit(text1, (20,20))
loadscreen_image.blit(text2,(150,600))
#sprite.loadscreen_image.blit(text2, sprite.rect)


#resize image 
loadscreen_image = pg.transform.scale(loadscreen_image,(width, height+100))
x_image = pg.transform.scale (x_image,(80,80))
o_image = pg.transform.scale(o_image,(80,80))

#defining game functions 
def game_start():
    screen.blit(loadscreen_image,(0,0))
    pg.display.update()
    time.sleep(2)
    screen.fill(white)

    #Drawing game board (Vertical)
    pg.draw.line (screen,line_colour,(width/3,0), (width/3, height),7)
    pg.draw.line(screen,line_colour,(width/3*2,0),(width/3*2, height),7)
    #Horizontal 
    pg.draw.line(screen,line_colour,(0,height/3),(width, height/3),7)
    pg.draw.line(screen,line_colour,(0,height/3*2),(width, height/3*2),7)
    draw_status()

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn "
    else:
        message = winner.upper() + "  won!"
    if draw: 
        message = 'Game Draw '
    font = pg.font.Font(None, 30)
    text = font.render (message, 1,(255,255,255))

     # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_for_winner():
    for row in range (0,3):
        if((TTT[row][0] ==TTT[row][1] ==TTT[2] and TTT[row][0] is not None)):
            #Then, player wins by rows 
            winner = TTT[row] [0] # because Winner != None as described above 
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                              (width, (row + 1)*height/3 - height/6 ), 4)
            break
    # check winner by columns
    for col in range (0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None): # look up this syntax 
            # this column won
            winner = TTT[0][col]
            #draw winning line
            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                          ((col + 1)* width/3 - width/6, height), 4)
            break
          # check for diagonal winners
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        # game won diagonally left to right
        winner = TTT[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)

    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
        # game won diagonally right to left
        winner = TTT[0][2]
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)

    if(all([all(row) for row in TTT]) and winner is None ):
        draw = True
    draw_status()


def drawXO (row, col): 
    global TTT, XO
    if row ==1: 
        posx = 30
    if row == 2:
        posx = width/3 + 30 
    if row ==3: 
        posx = width/3*2 + 30 
    
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    TTT[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_image,(posy,posx))
        XO= 'o'
    else:
        screen.blit(o_image,(posy,posx))
        XO= 'x'
    pg.display.update()
    #print(posx,posy)
    #print(TTT)


# To get mouse co-ordinates 
def userclick():
    x,y = pg.mouse.get_pos()

    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None

     #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)

    if(row and col and TTT[row-1][col-1] is None):
        global XO

        #draw the x or o on screen
        drawXO(row,col)
        check_for_winner()

def reset_game():
    global TTT, winner, XO, draw
    time.sleep(1)
    XO = 'x'
    draw = False
    game_start()
    winner=None
    TTT = [[None]*3,[None]*3,[None]*3]

game_start()

# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit() 
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userclick()
            if(winner or draw):
                reset_game()
    
    pg.display.update()
    CLOCK.tick(fps)

