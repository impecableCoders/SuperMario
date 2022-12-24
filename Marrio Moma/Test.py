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

def move_stone(x, y, plyer_rect):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    y -= speed
  if keys[pygame.K_DOWN]:
    y += speed
  if keys[pygame.K_LEFT]:
    x -= speed
  if keys[pygame.K_RIGHT]:
    x += speed

    # Calculate the distance between the player and the stone
  distance = plyer_rect.right - x

  # If the player is on the left of the stone, the distance is 5 or lower, and the player is moving to the right, move the stone to the right as well
  if plyer_rect.x < x and distance <= 5 and keys[pygame.K_d]:
      x += speed
Stein_img =        pygame.image.load("Bilder/Steine/1.png").convert_alpha()
stein =        pygame.transform.smoothscale(Stein_img,(30,30))
stein_rect = stein.get_rect(x=200, y=200)

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

    dist_rl1 = plyer_rect.top - stein_rect.top
    dist_r2 = plyer_rect.right - stein_rect.left
    dist_l2 = plyer_rect.left - stein_rect.right

    dist_tb1 = plyer_rect.left - stein_rect.left
    dist_t2 = plyer_rect.bottom - stein_rect.top
    dist_b2 = plyer_rect.top - stein_rect.bottom


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Here the plyer gltiches, we have to play with the nums to fix it
    if dist_rl1 >= -50 and dist_rl1 <= 20 and dist_r2 >-5 and dist_r2 <5 and keys[pygame.K_RIGHT]:
        stein_rect.x += speed

    if dist_rl1 >= -50 and dist_rl1 <= 20 and dist_l2 == 0  and keys[pygame.K_LEFT]:
        stein_rect.x -= speed

    if dist_tb1 >= -20 and dist_tb1 <= 20 and dist_t2 < 5 and dist_t2 >-4  and keys[pygame.K_DOWN]:
        stein_rect.y += speed

    if dist_tb1 >= -20 and dist_tb1 <= 20 and dist_b2 <= 0 and dist_b2 >-5  and keys[pygame.K_UP]:
        stein_rect.y -= speed

    if pygame.time.get_ticks()%1000 < 50/3:
       print(dist_t2)

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
    screen.blit(stein, stein_rect)


    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)



