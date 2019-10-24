# Pong by Zeyu Li
# This is a program that is a recreation of pong

# imports the pygame, sys and some math modules module
import pygame
import sys
from math import floor, sin, cos, sqrt

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# scale
scale = 5

# window width and height respectively
window_w = 200 * scale
window_h = 100 * scale
true_window_w = window_w + scale*4
true_window_h = window_h + scale*4

def main():

    # inits pygame
    pygame.init()

    # window size is window plus 2 scales for walls 
    window_size = pygame.display.set_mode(
        (true_window_w, true_window_h)
    )
    # set title of application as Bing Bong
    pygame.display.set_caption('Bing Bong - Python Application')

    # tick speed is 60 f/s
    tick_speed = 60
    run(tick_speed, window_size)


def run(tick_speed, window_size):

    # runs the pong game
    # - tick_speed = frames per seconds
    # - window_size = windows

    # inits run and paddle x, y coords
    run = True
    x_p, y_p = 2 * scale, window_h / 2

    # states center of ball and ball speed
    center = [floor(true_window_w/2), floor(true_window_h/2)]
    ball_speed = [scale, scale]

    # while game runs
    while run:

        for event in pygame.event.get():

            # if event quit is active, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    pygame.quit()
                    return 0
                else:
                    break

        # gets key pressed
        keys = pygame.key.get_pressed()

        # if up key pressed, move up unless it goes into the walls
        if keys[pygame.K_UP]:
            if y_p - 2*scale > scale:
                y_p -= scale
            else:
                y_p = 2*scale

        # if down key pressed, move down unless it goes into the walls
        if keys[pygame.K_DOWN]:
            if y_p + scale < window_h*.9 + scale:
                y_p += scale
            else:
                y_p = floor(window_h*.9) + scale

        # inits background as black
        window_size.fill(black)

        # draws walls
        Objects(window_size).walls()

        # draws player paddle
        Objects(window_size, x_p, y_p).paddle()

        # draws ball
        Objects(window_size, x_p, y_p, center, ball_speed).ball()

        # updates display
        pygame.display.update()

        # tick speed
        clock = pygame.time.Clock()
        clock.tick(tick_speed)


class Objects():

    def __init__(self, window_size, x_p = 0, y_p = 0, center = 0, speed = [scale, scale]):
        self.window_size = window_size
        self.center = center
        self.y_p = y_p
        self.x_p = x_p
        self.speed = speed

    def ball(self):
        # draws ball
        # - window_size = size of window
        # - center = center of ball
        # - y_p = the height of paddle
        # - speed = speed of a ball as a list. 
        # First number is the x speed, second is the y speed, default = [scale, scale]

        # NOTE: +3 is ~ the radius of ball

        # if the center of ball plus speed plus the radius of ball is greater 
        # than the wall's position, reverse the speed of the ball
        if self.center[0] + self.speed[0] + 3 > true_window_w - 2*scale:
            self.speed[0] = -self.speed[0]
        elif self.center[0] - 2*scale - 6 < 0:
            # tests to see if it hits the paddle. If it doesn't quit game
            if self.y_p > self.center[1] - 2*scale - 6 or self.y_p + int(window_h * .1) < self.center[1] - 2*scale - 3:
                pygame.quit()
                sys.exit()
            # else, take the position that it hit the paddle and calculate a degree at which it should bounce back
            # the more out of the center it is, the more vertical it becomes
            else:
                degrees = (self.center[1] - 2*scale - 6 - self.y_p)/(window_h * .1) * 110 + 35
                self.speed[0] = round(cos(degrees)*sqrt(50))
                self.speed[1] = round(sin(degrees)*sqrt(50))
            self.speed[0] = -self.speed[0]
        if self.center[1] + self.speed[1] + 3 > true_window_h - 2*scale:
            self.speed[1] = -self.speed[1]
        elif self.center[1] - 2*scale - 6 < 0:
            self.speed[1] = -self.speed[1]

        # calculates next position and draws it
        self.center[0] += self.speed[0]
        self.center[1] += self.speed[1]
        circle = pygame.draw.circle(self.window_size, white, self.center, scale)

    def walls(self):
        # draws the walls of the board
        # - window_size = size of window

        # sets the wall width and height
        wall_w = window_w
        wall_h = scale

        # draws the top and bottom wall
        pygame.draw.rect(
            self.window_size, white, (2*scale, scale, wall_w, wall_h)
        )
        pygame.draw.rect(
            self.window_size, white, (2*scale, scale+window_h, wall_w, wall_h)
        )


    def paddle(self):
        # draws the player paddle
        # - window_size = size of window
        # - x_p = the x position of the paddle
        # - y_p = the y position of the paddle

        # TODO: rounded paddles like css border-radius
        # defines the height and width of the paddle
        height_p = int(window_h * .1)
        width_p = scale

        # draws the player paddle
        pygame.draw.rect(
            self.window_size, white, (self.x_p, self.y_p, width_p, height_p)
        )

# calls main function
main()
