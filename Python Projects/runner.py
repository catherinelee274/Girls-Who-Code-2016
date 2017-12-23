import pygame
import random




    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

class Block(pygame.sprite.Sprite): #parentclass

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

#initializing the list containing black blocks
black_block_list = pygame.sprite.Group()

#initializing the list containing green blocks
green_block_list = pygame.sprite.Group()

#initializing the list containing ALL the blocks
all_sprites_list = pygame.sprite.Group()

#initialize the player block here!
"Code"
player =  Block(BLUE,10,10)

def make_blocks():

    #add the player to the list it should be in
    "CODE"
    all_sprites_list.add(player) 

    #make 50 black blocks and 50 green blocks
    for i in range(50):
        #initialize a black block
        black_block = Block(BLACK, 10, 10) #SYNTAXXXXXXXXX
        #initalize a green block
        green_block =  Block(GREEN, 10,10)  


        #initialize the x and y for the black block
        #code
        black_block.rect.x = random.randint(10,(screen_width-10))
        black_block.rect.y = random.randint(10,(screen_height-10)) 

        #initialize the x and y for the green block
        #code
        green_block.rect.x = random.randint(10,(screen_width-10))
        green_block.rect.y = random.randint(10,(screen_height-10)) 


        #add the blocks to ALL the lists they should be in
        "CODE"
        black_block_list.add(black_block)
        green_block_list.add(green_block)
        all_sprites_list.add(black_block)
        all_sprites_list.add(green_block) 


done = False

clock = pygame.time.Clock()

#initialize the value of score
score = 0

#initialize the number of lives
lives = 2



## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)


#Call the function here that will create the blocks you want
for blocks in all_sprites_list:
    make_blocks() 



# Variable to check if pressing r will restart game
can_restart = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                all_sprites_list.empty()
                make_blocks()
                can_restart = False
                


 
 
    # Clear the screen
    #logic STARTTTTT
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # Write the code to see if the player block has collided with anything
    # Check if it collides with black blocks DONE
    # Check if it collided with green blocks DONE
    # pygame.sprite.spritecollide might be VERY helpful. look at the example
    "CODE"
    green_collision = pygame.sprite.spritecollide(player, green_block_list, True)
    black_collision = pygame.sprite.spritecollide(player, black_block_list, True)
       

    # Write the code to move the blocks.
    "CODE"
    for elem in all_sprites_list:
        elem.update()

        
    # Update score here
    # Collision with a certain sprite means the score should go up
    "CODE"
    for elem in green_collision:
        score += 1 

    #Update lives here
    #Collision with a certain sprite means the lives should go down
    "CODE"
    for elem in black_collision:
        lives -= 1


    score_text = font.render("Score: " +str(score), True, BLACK)

    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    screen.blit(score_text, [500, 50])

    screen.blit(lives_text, [50, 50])

    ## Some logic to allow the game to be restarted
    if  len(green_block_list) == 0:
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(play_again, [250, 250])
        can_restart = True
    
    if lives < 1:
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(play_again, [250, 250])
        can_restart = True

    
    # Draw all the sprites  
    all_sprites_list.draw(screen)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

