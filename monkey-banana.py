#Matt Westelman
#3/22/18
#monkey-banana.py - my first game

from ggame import *
from random import randint

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

#Moves monkey right 1 cell if possible + collects banana
def moveRight(event):
     if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x +=CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#Moves monkey left 1 cell if possible + collects banana  
def moveLeft(event):
    if monkey.x> 0:
        monkey.x -=CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#Moves monkey up 1 cell if possible + collects banana    
def moveUp(event):
    if monkey.y> 0:
        monkey.y -=CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#Moves monkey down 1 cell if possible + collects banana
def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y +=CELL_SIZE 
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#Banana teleports to a new location    
def moveBanana():
    data['frames'] = 0 #reset the tp timer
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
  
# updating score
def updateScore():
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
#Keeps track of how many frames since last teleport, and TPs it after 150 frames
def step():
    data['frames'] +=1
    if data['frames']%150 == 0:
        moveBanana()

#Sets up and runs game    
if __name__ == '__main__':
    
    #hold variable in dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    #colors for the color god
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    #graphics for the graphic throne
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS, LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(step)
