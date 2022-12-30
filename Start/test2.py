import pygame
import sys

# Initialize Pygame and create a window
pygame.init()
screen_width, screen_height = 600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario")

# Load the images of Mario running
plyer_image = [pygame.image.load('Bilder/oben.png').convert_alpha(),
               pygame.image.load('Bilder/unten.png').convert_alpha(),
               pygame.image.load("Bilder/rechts.png").convert_alpha(),
               pygame.image.load("Bilder/links.png").convert_alpha(),
               pygame.image.load("Bilder/left1.png").convert_alpha(),
               pygame.image.load("Bilder/right1.png").convert_alpha()]


Stein_img = pygame.image.load("Bilder/Steine/1.png").convert_alpha()
stein = pygame.transform.smoothscale(Stein_img, (30, 30))
stein_rect = stein.get_rect(x=200, y=200)

# Load the background image and scale it to fit the screen
o_background1 = pygame.image.load("Bilder/background.jpg").convert_alpha()
background1 = pygame.transform.scale(o_background1, (screen_width, screen_height))

o_background2 = pygame.image.load("Bilder/background1.jpg").convert_alpha()
background2 = pygame.transform.scale(o_background2, (screen_width, screen_height))

background = background1
# Set the player's initial position and speed
plyer = plyer_image[1].convert_alpha()
plyer = pygame.transform.scale(plyer, (30, 50))
plyer_rect = plyer_image[1].get_rect(x=100, y=200)

speed = 5
line_x = 0
# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the player's position based on key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        plyer = plyer_image[1]

    if keys[pygame.K_UP]:
        plyer = plyer_image[0]
        plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN]:
        plyer = plyer_image[1]
        plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(0, speed)
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if pygame.time.get_ticks() % 100 < 50:
            plyer = plyer_image[2]
            plyer = pygame.transform.scale(plyer, (30, 50))
        else:
            plyer = plyer_image[5]
            plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(speed, 0)
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if pygame.time.get_ticks() % 100 < 50:
            plyer = plyer_image[3]
            plyer = pygame.transform.scale(plyer, (30, 50))
        else:
            plyer = plyer_image[4]
            plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(-speed, 0)



    # Clear the screen and draw the background and player
    screen.blit(background, (0, 0))
    screen.blit(plyer, plyer_rect)
    screen.blit(stein, stein_rect)


    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)