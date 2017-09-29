import pygame
import random
import numpy as np
import time

#define variables for game
FPS = 60

#size of game widnow
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#size of paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#size of our ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#speed of paddle and wall
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB Colors paddle and ball
WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_BUFFER = 4

#initialize our screen
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
#draw our ball
def drawBall(ballXpos,ballYpos):
    #top left, top right, delta x , delta y
    ball = pygame.Rect(ballXpos,ballYpos,BALL_WIDTH,BALL_HEIGHT)
    pygame.draw.rect(screen,WHITE,ball)

def drawPaddle1(paddle1YPos):
    paddle1 = pygame.Rect(PADDLE_BUFFER,paddle1YPos,PADDLE_WIDTH,PADDLE_HEIGHT)
    pygame.draw.rect(screen,WHITE,paddle1)

def drawPaddle2(paddle2YPos):
    paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER-PADDLE_WIDTH,paddle2YPos,PADDLE_WIDTH,PADDLE_HEIGHT)
    pygame.draw.rect(screen,WHITE,paddle2)

def updateball(paddle1YPos,paddle2YPos,ballXpos,ballYpos,ballXDirection,ballYDirection):

    #update x and y position
    ballXpos = ballXpos + ballXDirection *BALL_X_SPEED
    ballYpos = ballYpos + ballYDirection * BALL_Y_SPEED
    score = 0

    #check for collisions with first paddle
    if(PADDLE_BUFFER + PADDLE_WIDTH >= ballXpos and  paddle1YPos + PADDLE_HEIGHT> ballYpos > paddle1YPos):
        #if the ball hits the left paddle, switch direction
        score = 1
        ballXDirection = 1

    elif(ballXpos <= 0):
        ballXDirection = 1
        score = -1
        return [score,paddle1YPos,paddle2YPos,ballXpos,ballYpos,ballXDirection,ballYDirection]
    #collision with the right paddle

    #and ballXpos < WINDOW_WIDTH - PADDLE_BUFFER
    #   and ballYpos <= PADDLE_HEIGHT + paddle1YPos and ballYpos > paddle1YPos ):
    
    
    if(ballXpos+BALL_WIDTH >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and (ballYpos <= PADDLE_HEIGHT + paddle2YPos and ballYpos > paddle2YPos)):
        ballXDirection = -1

    elif(ballXpos >= WINDOW_WIDTH-BALL_WIDTH):
        ballXDirection = -1
        score = 1
        return [score,paddle1YPos,paddle2YPos,ballXpos,ballYpos,ballXDirection,ballYDirection]

    #if the ball hits the top
    if(ballYpos <=0):
        ballYDirection = 1
        ballYpos = 0
    elif(ballYpos >= WINDOW_HEIGHT - BALL_HEIGHT):
        ballYpos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1
    return [score,paddle1YPos,paddle2YPos,ballXpos,ballYpos,ballXDirection,ballYDirection]

def updatePaddle1(action, paddle1YPos):
    if(action[1] ==1):
        paddle1YPos = paddle1YPos -PADDLE_SPEED


    #if move down

    if(action[2] == 1):
            paddle1YPos = paddle1YPos + PADDLE_SPEED

    #don't let it move off thecreen
    if(paddle1YPos<0):
        paddle1YPos = 0
    if(paddle1YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1YPos = WINDOW_HEIGHT - PADDLE_HEIGHT

    return paddle1YPos

def updatePaddle2(paddle2YPos,ballYpos):
    #try to move the paddle to the ball
    middle = paddle2YPos + PADDLE_HEIGHT/2
    if(ballYpos-middle == 0):
        pass
    elif(ballYpos-middle > 0):
        paddle2YPos = paddle2YPos + PADDLE_SPEED
    elif(ballYpos-middle < 0):
        paddle2YPos = paddle2YPos - PADDLE_SPEED

    if (paddle2YPos < 0):
        paddle2YPos = 0
    if (paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2YPos = WINDOW_HEIGHT - PADDLE_HEIGHT

    return paddle2YPos


            #if move up
    # if(action[1] ==1):
    #     paddle2YPos = paddle2YPos -PADDLE_SPEED
    #
    # #if move down
    # if(action[2] == 1):
    #     paddle2YPos = paddle2YPos + PADDLE_SPEED
    #
    #
    # #don't let it move off the screen
    # if(paddle2YPos<0):
    #     paddle2YPos = 0
    # if(paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
    #     paddle2Yps = WINDOW_HEIGHT - PADDLE_HEIGHT

class PongGame:
    def __init__(self):
        #random number for initial direction of ball
        num = random.randint(0,9)
        #keep score
        self.tally = 0
        #intialize positions of our paddles
        self.paddle1YPos = WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2
        self.paddle2YPos = WINDOW_HEIGHT/2 - PADDLE_HEIGHT/2

        self.ballXDirection = 1
        self.ballYDirection = 1

        #starting point
        self.ballXpos = WINDOW_WIDTH/2 - BALL_WIDTH/2
        self.ballYpos = WINDOW_HEIGHT/2 - BALL_HEIGHT/2

    def getPresentFrame(self):
        #for each frame, call the event queue
        pygame.event.pump()
        #make background black
        screen.fill(BLACK)
        #draw the paddles
        drawPaddle1(self.paddle1YPos)
        drawPaddle2(self.paddle2YPos)
        #draw ball
        drawBall(self.ballXpos,self.ballYpos)

        #get pixels
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update the window
        pygame.display.flip()

        #return the surface data
        return image_data

    def getNextFrame(self,action):
        pygame.event.pump()
        screen.fill(BLACK)
        self.paddle1YPos = updatePaddle1(action,self.paddle1YPos)
        drawPaddle1(self.paddle1YPos)
        self.paddle2YPos = updatePaddle2(self.paddle2YPos,self.ballYpos)
        drawPaddle2(self.paddle2YPos)
        #update the ball and draw it

        score, self.paddle1YPos, self.paddle2YPos, self.ballXpos, self.ballYpos, self.ballXDirection, self.ballYDirection = \
            updateball(self.paddle1YPos,self.paddle2YPos,self.ballXpos,self.ballYpos,self.ballXDirection,self.ballYDirection)

        #update tally
        self.tally = self.tally + score
        

        drawBall(self.ballXpos,self.ballYpos)

        #get pixels
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())
        #update the window
        pygame.display.flip()

        #return the surface data
        return (score, image_data)

