import pygame  # Imports a game library that lets you use specific functions in your program.
import random  # Import to generate random numbers.

# Initialize the pygame modules to get everything started.

pygame.init()

# The screen that will be created needs a width and a height.
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))  # This creates the screen and gives it the width and
# height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image).
player = pygame.image.load("player1.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("blenemy.png")
enemy3 = pygame.image.load("grenemy.png")
prize = pygame.image.load("prize_1.png")

# Get the width and height of the images in order to do boundary detection (i.e. making sure the image stays within
# screen boundaries or know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy.get_height()
enemy2_width = enemy.get_width()
enemy3_height = enemy.get_height()
enemy3_width = enemy.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " + str(image_height))
print("This is the width of the player image: " + str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later.
playerXPosition = 100
playerYPosition = 50

# Make the enemies start off screen and at a random y position.
enemyXPosition = screen_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed. Right now they are not so make them equal to the boolean value (True
# or False) of False. Boolean values are True or False values that can be used to test conditions and test states
# that are binary, i.e. either one way or the other.

keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# This is the game loop.
# In games we need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1:  # This is a looping structure that will loop the indented code until you tell it to stop(in the event where
    # you exit the program by quitting).

    screen.fill(0)  # Clears the screen.
    screen.blit(player, (playerXPosition,
                         playerYPosition))  # This draws the player image to the screen at the position specified. I.e.
    # (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # This updates the screen.

    # This loops through events in the game.
    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # This event checks if the user press a key down.
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        if playerXPosition < 0:  # This makes sure that the user does not move the player beyond the left side of
            # the window
            playerXPosition += 1
        else:
            playerXPosition -= 1

    if pressed[pygame.K_RIGHT]:
        if playerXPosition > screen_height - image_height:  # This makes sure that the user does not move the
            # player beyond the right side of the window
            playerXPosition -= 1
        else:
            playerXPosition += 1

    if pressed[pygame.K_UP]:
        if playerYPosition < 0:  # This makes sure that the user does not move the player above the window.
            playerYPosition += 1
        else:
            playerYPosition -= 1

    if pressed[pygame.K_DOWN]:
        if playerYPosition > screen_height - image_height:  # This makes sure that the user does not move the
            # player below the window.
            playerYPosition -= 1
        else:
            playerYPosition += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.

    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Bounding box for the enemies:
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Bounding box for prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:

    # Collision test_1: if player has found the prize
    if playerBox.colliderect(prizeBox):
        # Display wining status to the user:
        print("You Win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box):
        # Display losing status to the user:
        print("You lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        # Display losing status to the user:
        print("You lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    # If the enemy is off the screen the user wins the game:
    if enemyXPosition < 0 - enemy_width and enemy2XPosition < 0 - enemy2_height:
        if enemy3XPosition < 0 - enemy3_height:
            # Display wining status to the user:
            print("You win!")

            # Quite game and exit window: 
            pygame.quit()

            exit(0)

    # Make enemy approach the player.
    enemyXPosition -= 0.20
    enemy2XPosition -= 0.3
    enemy3XPosition -= 0.52
    prizeXPosition -= 0.17

    # ================The game loop logic ends here. =============

# Reference:
# https://www.stackoverflow.com
# images used for enemies, player and the prize were obtained from https://www.pinclipart.com
