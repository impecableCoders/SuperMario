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


def move_stone(x, y, plyer_rect1):
    key_s = pygame.key.get_pressed()
    if key_s[pygame.K_UP]:
        y -= speed
    if key_s[pygame.K_DOWN]:
        y += speed
    if key_s[pygame.K_LEFT]:
        x -= speed
    if key_s[pygame.K_RIGHT]:
        x += speed

        # Calculate the distance between the player and the stone
    distance = plyer_rect1.right - x

    # If the player is on the left of the stone, the distance is 5 or lower, and the player is moving to the right,
    # move the stone to the right as well
    if plyer_rect1.x < x and distance <= 5 and keys[pygame.K_d]:
        x += speed


def line(x_start, y_start, x_end, y_end):
    pygame.draw.line(screen, "black", (x_start, y_start), (x_end, y_end), width=5)


Stein_img = pygame.image.load("Bilder/Steine/1.png").convert_alpha()
stein = pygame.transform.smoothscale(Stein_img, (30, 30))
stein_rect = stein.get_rect(x=200, y=200)

# Load the background image and scale it to fit the screen
o_background = pygame.image.load("Bilder/background.jpg").convert_alpha()
background = pygame.transform.scale(o_background, (screen_width, screen_height))

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

    # Here is the movement of the stone
    dist_bottom = plyer_rect.bottom - stein_rect.top
    dist_top = plyer_rect.top - stein_rect.bottom
    dist_right = plyer_rect.right - stein_rect.left
    dist_left = plyer_rect.left - stein_rect.right

    if 0 <= dist_bottom <= 80 and 10 <= dist_right <= 30 and keys[pygame.K_RIGHT]: stein_rect.x += speed
    if 0 <= dist_bottom <= 80 and -30 <= dist_left <= 0 and keys[pygame.K_LEFT]:   stein_rect.x -= speed
    if 0 <= dist_bottom <= 20 and -60 <= dist_left <= -5 and keys[pygame.K_DOWN]:  stein_rect.y += speed
    if -20 <= dist_top <= 0 and -60 <= dist_left <= -5 and keys[pygame.K_UP]:      stein_rect.y -= speed

    # print to help
    if pygame.time.get_ticks() % 1000 < 50 / 3:
        print("line: 118", "bottom:", dist_bottom)

    # The line movement
    if keys[pygame.K_e]:
        if line_x < 50:
            line_x += 1
    if keys[pygame.K_q]:
        if line_x > 0:
            line_x -= 1

    if line_x+plyer_rect.left+30 >= stein_rect.x and 31 < dist_bottom < 56:
        if keys[pygame.K_f]:
            stein_rect.x = plyer_rect.x+line_x+20
            stein_rect.y = plyer_rect.centery-10
            print("hey")
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
    line(plyer_rect.centerx + 15, plyer_rect.centery, plyer_rect.centerx + line_x + 15, plyer_rect.centery)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)



