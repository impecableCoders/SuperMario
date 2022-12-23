# import pygame
# import sys
#
# pygame.init()
#
# screen = pygame.display.set_mode((600,500))
# screenSize = screen.get_width(),screen.get_height()
# Clock = pygame.time.Clock()
#
# pygame.display.set_caption("Marrio")
# plyer = pygame.image.load("unten.png").convert_alpha()
# plyer_rect = plyer.get_rect()
# #plyer_rect = plyer.get_rect()
# #plyer1 = pygame.transform.scale(plyer, (50,50))
#
# plyer_image = [pygame.image.load("oben.png").convert_alpha(),
#                pygame.image.load("unten.png").convert_alpha(),
#                pygame.image.load("rechts.png").convert_alpha(),
#                pygame.image.load("links.png").convert_alpha(),
#                pygame.image.load("left1.png").convert_alpha(),
#                pygame.image.load("right1.png").convert_alpha()]
#
# o_background =   pygame.image.load("background.jpg").convert_alpha()
# background = pygame.transform.scale(o_background, screenSize)
#
# p_x, p_y = 100,200
# p_g = 0
# speed = 5
# while True:
#
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#
#
#     screen.blit(background,(0,0))
#
#
#
#
#     if pygame.key.get_pressed()[pygame.K_UP]:
#         plyer = plyer_image[0]
#
#         plyer_rect.y -= speed
#     if pygame.key.get_pressed()[pygame.K_DOWN]:
#         plyer = plyer_image[1]
#         plyer_rect.y += speed
#     if pygame.key.get_pressed()[pygame.K_RIGHT]:
#         if pygame.time.get_ticks() % 100 < 50:
#             plyer = plyer_image[2]
#         else:
#             plyer = plyer_image[5]
#         plyer_rect.x += speed
#     if pygame.key.get_pressed()[pygame.K_LEFT]:
#         if pygame.time.get_ticks() % 100 < 50:
#             plyer = plyer_image[3]
#         else:
#             plyer = plyer_image[4]
#         plyer_rect.x -= speed
#
#
#     if plyer_rect.bottom >= screen.get_height(): plyer_rect.bottom = screen.get_height()
#     if plyer_rect.right >= screen.get_width(): plyer_rect.right = screen.get_width()
#     if plyer_rect.top <= 0: plyer_rect.top = 0
#     if plyer_rect.left <= 0: plyer_rect.left = 0
#
#
#     screen.blit(plyer,plyer_rect)
#
#
#     pygame.display.update()
#     Clock.tick(60)




import pygame
import sys

# Initialize Pygame and create a window
pygame.init()
screen_width, screen_height = 600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario")

# Load the images of Mario running
plyer_image = [pygame.image.load("Bilder/oben.png").convert_alpha(),
               pygame.image.load("Bilder/unten.png").convert_alpha(),
               pygame.image.load("Bilder/rechts.png").convert_alpha(),
               pygame.image.load("Bilder/links.png").convert_alpha(),
               pygame.image.load("Bilder/left1.png").convert_alpha(),
               pygame.image.load("Bilder/right1.png").convert_alpha()]

# Load the background image and scale it to fit the screen
o_background = pygame.image.load("Bilder/background.jpg").convert_alpha()
background = pygame.transform.scale(o_background, (screen_width, screen_height))

# Set the player's initial position and speed
plyer = plyer_image[1]
plyer_rect = plyer_image[1].get_rect(x=100, y=200)
speed = 5

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
    if keys[pygame.K_UP]:
        plyer = plyer_image[0]
        plyer_rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN]:
        plyer = plyer_image[1]
        plyer_rect.move_ip(0, speed)
    if keys[pygame.K_RIGHT]:
        if pygame.time.get_ticks() % 100 < 50:
            plyer = plyer_image[2]
        else:
            plyer = plyer_image[5]
        plyer_rect.move_ip(speed, 0)
    if keys[pygame.K_LEFT]:
        if pygame.time.get_ticks() % 100 < 50:
            plyer = plyer_image[3]
        else:
            plyer = plyer_image[4]
        plyer_rect.move_ip(-speed, 0)

    # Keep the player within the screen boundaries
    if plyer_rect.bottom > screen_height:
        plyer_rect.bottom = screen_height
    if plyer_rect.right > screen_width:
        plyer_rect.right = screen_width
    if plyer_rect.top < 0:
        plyer_rect.top = 0
    if plyer_rect.left < 0:
        plyer_rect.left = 0

    # Clear the screen and draw the background and player
    screen.blit(background, (0, 0))
    screen.blit(plyer, plyer_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)



