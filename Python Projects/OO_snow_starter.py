"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")

y_location = 0
y_speed = 3


# Your SnowFlake class


class snowflake():
    def __init__(self, x_location, y_location, y_speed, ball_size):
    #attributes
        self.x_location = x_location
        self.y_location=y_location
        self.y_speed = y_speed
        
    #move y down
    def move(self):
        self.y_location += y_speed
        pygame.draw.circle(screen, WHITE, [self.x_location, self.y_location], 5)
    
    
    



# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Speed
 

# Snow List
snow_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    screen.fill(BLACK)

    # --- Drawing code should go here
    # Begin Snow
    x_location= random.randint(0,700)
    snow = snowflake(x_location, y_location, y_speed,5)
    snow_list.append(snow)
    
    for elem in snow_list:        
        elem.move()
        
    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
