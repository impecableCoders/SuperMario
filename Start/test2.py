import pygame
import sys


def exitGame():
    pygame.quit()
    sys.exit()


# Initialize Pygame and create a window
pygame.init()
screen_width, screen_height = 600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()


def load_image_plyer(image, defualt_width_sacle=30, defualt_height_sacle=50):
    plyer_image = pygame.image.load('Bilder/' + image + '.png').convert_alpha()
    pygame.transform.scale(plyer_image, (defualt_width_sacle, defualt_height_sacle))
    return plyer_image


def image_stein():
    Stein_img = pygame.image.load("Bilder/Steine/1.png").convert_alpha()
    stein = pygame.transform.smoothscale(Stein_img, (30, 30))
    return stein


def line(x_start, y_start, x_end, y_end):
    pygame.draw.line(screen, "black", (x_start, y_start), (x_end, y_end), width=5)


def image_background():
    o_background1 = pygame.image.load("Bilder/background1.jpg").convert_alpha()
    background1 = pygame.transform.scale(o_background1, (screen_width, screen_height))
    return background1


stein = image_stein()
stein_rect = stein.get_rect(x=200, y=200)
background = image_background()

playerAnimations = {"left1": load_image_plyer("left1"),
                    "links": load_image_plyer("links"),
                    "oben": load_image_plyer("oben"),
                    "rechts": load_image_plyer("rechts"),
                    "right1": load_image_plyer("right1"),
                    "unten": load_image_plyer("unten")}


def createPlayerDamagedAnimations():
    keys = ["left1", "links", "oben", "rechts", "right1", "unten"]
    res = {}
    for k in keys:
        img = load_image_plyer(k)
        img.fill((255, 0, 0, 128), special_flags=pygame.BLEND_ADD)
        res[k] = img
    return res


playerDamagedAnimations = createPlayerDamagedAnimations()
playerAnimationCurrentKey = "unten"
def activateDamageAnimationPlayer():
    global lastDamageActiveTime
    lastDamageActiveTime = pygame.time.get_ticks()
def getPlayerSprite():
    if damaged_animation:
        return playerDamagedAnimations[playerAnimationCurrentKey]
    return playerAnimations[playerAnimationCurrentKey]


speed = 5
line_x = 0
hertz = 5

damaged_animation = False
lastDamageActiveTime = 0

plyer = getPlayerSprite()
plyer_rect = plyer.get_rect(x=100, y=200)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame()

    # Update the player's position based on key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: exitGame()

    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
        playerAnimationCurrentKey = "unten"

    if keys[pygame.K_UP]:
        playerAnimationCurrentKey = "oben"
        plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(0, -speed)

    if keys[pygame.K_DOWN]:
        playerAnimationCurrentKey = "unten"
        plyer_rect.move_ip(0, speed)

    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if pygame.time.get_ticks() % 100 < 50:
            playerAnimationCurrentKey = "rechts"
        else:
            playerAnimationCurrentKey = "right1"
        plyer_rect.move_ip(speed, 0)

    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if pygame.time.get_ticks() % 100 < 50:
            playerAnimationCurrentKey = "links"
        else:
            playerAnimationCurrentKey = "left1"
            plyer = pygame.transform.scale(plyer, (30, 50))
        plyer_rect.move_ip(-speed, 0)

    # Here is the movement of the stone
    dist_bottom = plyer_rect.bottom - stein_rect.top
    dist_top = plyer_rect.top - stein_rect.bottom
    dist_right = plyer_rect.right - stein_rect.left
    dist_left = plyer_rect.left - stein_rect.right

    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_RIGHT]:
        stein_rect.x += speed
        plyer_rect.x = plyer_rect.x - 50
        activateDamageAnimationPlayer()

    #     # Zeige Mario rot an
    #     plyer = playerDamagedAnimations["unten"]
    #     plyer = pygame.transform.scale(plyer, (30, 50))
    # else:
    #     # Zeige Mario in seiner normalen Farbe an
    #     plyer = getPlayerSprite["unten"]
    #     plyer = pygame.transform.scale(plyer, (30, 50))

    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_LEFT]:
        stein_rect.x -= speed
        plyer_rect.x = plyer_rect.x + 50
        activateDamageAnimationPlayer()
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_DOWN]:
        stein_rect.y += speed
        plyer_rect.y = plyer_rect.y - 50
        activateDamageAnimationPlayer()
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_UP]:
        stein_rect.y -= speed
        plyer_rect.y = plyer_rect.y + 50
        activateDamageAnimationPlayer()

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

    if stein_rect.x <= line_x + plyer_rect.left + 30 and 31 < dist_bottom < 56:
        if keys[pygame.K_f]:
            stein_rect.x = plyer_rect.x + line_x + 20
            stein_rect.y = plyer_rect.centery - 10

    # Keep the player within the screen boundaries
    if plyer_rect.bottom > screen_height:
        plyer_rect.bottom = screen_height

    if plyer_rect.right > screen_width:
        plyer_rect.right = screen_width

    if plyer_rect.top < 0:
        plyer_rect.top = 0

    if plyer_rect.top < 0:
        plyer_rect.top = 0
    if plyer_rect.left < 0:
        plyer_rect.left = 0

    # Update Player Damage Animation
    if pygame.time.get_ticks() - lastDamageActiveTime < 300:  # Damage flickering on
        if pygame.time.get_ticks() % 100 < 50:
            damaged_animation = True
        else:
            damaged_animation = False
    else:
        damaged_animation = False

    plyer = getPlayerSprite()

    # Clear the screen and draw the background and player
    screen.blit(background, (0, 0))
    screen.blit(plyer, plyer_rect)
    screen.blit(stein, stein_rect)
    line(plyer_rect.centerx + 15, plyer_rect.centery, plyer_rect.centerx + line_x + 15, plyer_rect.centery)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
