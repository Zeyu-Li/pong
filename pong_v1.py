# Pong by Zeyu Li
# This is a program that is a recreation of pong

# imports the pygame module
import pygame


# User-defined functions

def main():

    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window 500 px by 400 px
    pygame.display.set_mode((500, 400))

    # set the title of the display window
    pygame.display.set_caption('Pong - Python Application')   
    # get the display surface
    w_surface = pygame.display.get_surface()

    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit() 


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # sets surface and the color black
        self.surface = surface
        self.bg_color = pygame.Color('black')

        # sets fps to 60
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # defines middle of window
        y_middle = int(self.surface.get_height()/2)

        # game objects: ball, left paddle and right paddle
        self.ball = Ball(
            'white', 5, [int(self.surface.get_width()/2), 
            y_middle], [6, 3], self.surface
        )
        self.left_paddle = Paddle(
            'white', pygame.Rect(100, y_middle - 20, 10, 40), 5, self.surface
        )
        self.right_paddle = Paddle(
            'white', pygame.Rect(self.surface.get_width() - 100, y_middle - 20, 10, 40), 5, self.surface
        )
        # max frames not needed
        # self.max_frames = 150
        self.frame_counter = 0

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()            
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        self.ball.draw()
        self.left_paddle.draw()
        self.right_paddle.draw()
        pygame.display.update() # make the updated surface appear on the display

    def update(self):
        # Update the game objects.
        # - self is the Game to update

        self.ball.move()
        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        
        # TODO: check score of 11 on either side
        if False:
            self.continue_game = False


class Ball:
    # An object in this class represents objects in the game

    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
        # Initialize a Ball.
        # - self is the Ball to initialize
        # - color is the pygame.Color of the ball
        # - center is a list containing the x and y int
        #   coords of the center of the ball
        # - radius is the int pixel radius of the ball
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame. Surface object

        self.color = pygame.Color(ball_color)
        self.radius = ball_radius
        self.center = ball_center
        self.velocity = ball_velocity
        self.surface = surface

    def move(self):
        # Change the location of the Ball by adding the corresponding 
        # speed values to the x and y coordinate of its center
        # - self is the Ball
        
        for i in range(0,2):
            if i == 0:
                if self.surface.get_width() < self.center[i] + self.velocity[i] or 0 > self.center[i] + self.velocity[i]:
                    self.velocity[i] = -self.velocity[i]
            else:
                if self.surface.get_height() < self.center[i] + self.velocity[i] or 0 > self.center[i] + self.velocity[i]:
                    self.velocity[i] = -self.velocity[i]
            self.center[i] = (self.center[i] + self.velocity[i])

    def draw(self):
        # Draw the ball on the surface
        # - self is the Ball
        
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


class Paddle:
    # An object in this class represents objects in the game
    
    def __init__(self, paddle_color, paddle_object, paddle_velocity, surface):
        # Initialize a paddle.
        # - self is the paddle to initialize
        # - color is the pygame.Color of the paddle
        # - object of the paddle as a Rect
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame. Surface object

        self.color = pygame.Color(paddle_color)
        self.center = paddle_object
        self.velocity = paddle_velocity
        self.surface = surface
        
    def move(self):

        # NOT in use at the moment

        # Change the location of the paddle by adding the corresponding 
        # speed values to the x and y coordinate of its center
        # - self is the paddle

        for i in range(0,2):
            self.center[i] = (self.center[i] + self.velocity[i])
    
    def draw(self):
        # Draw the paddle on the surface
        # - self is the Paddle

        pygame.draw.rect(self.surface, self.color, self.center)

# main function call
main()
