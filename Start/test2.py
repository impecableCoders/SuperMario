import pygame, sys, random, time

def exitGame():
    pygame.quit()
    sys.exit()
def Keep_The_Opj_On_Screen(Opj_rect):
    if Opj_rect.bottom > screen_height:
        Opj_rect.bottom = screen_height
    if Opj_rect.right > screen_width:
        Opj_rect.right = screen_width
    if Opj_rect.top < 0:
        Opj_rect.top = 0
    if Opj_rect.top < 0:
        Opj_rect.top = 0
    if Opj_rect.left < 0:
        Opj_rect.left = 0

def move_stone(stone, stone_rect, speed=2):

    if random.random() < 0.1:
        directions = ["S", "SW", "W", "NW", "N", "NE", "E", "SE"]
        direction = random.choice(directions)


        if direction == "S":
            move_x, move_y = 0, speed
        elif direction == "SW":
            move_x, move_y = -speed, speed
        elif direction == "W":
            move_x, move_y = -speed, 0
        elif direction == "NW":
            move_x, move_y = -speed, -speed
        elif direction == "N":
            move_x, move_y = 0, -speed
        elif direction == "NE":
            move_x, move_y = speed, -speed
        elif direction == "E":
            move_x, move_y = speed, 0
        elif direction == "SE":
            move_x, move_y = speed, speed

        # Add the relative coordinates to the stone's coordinates
        stone_rect.left += move_x
        stone_rect.top += move_y

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

Plyer_speed = 5
Stein_speed = 5
Shock_speed = 50

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

    # Plyer Movement
    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:playerAnimationCurrentKey = "unten"
    if keys[pygame.K_UP]:
        playerAnimationCurrentKey = "oben"
        plyer_rect.move_ip(0, -Plyer_speed)
    if keys[pygame.K_DOWN]:
        playerAnimationCurrentKey = "unten"
        plyer_rect.move_ip(0, Plyer_speed)



    # Plyer Animation
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if pygame.time.get_ticks() % 100 < 50:
            playerAnimationCurrentKey = "rechts"
        else:
            playerAnimationCurrentKey = "right1"
        plyer_rect.move_ip(Plyer_speed, 0)
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if pygame.time.get_ticks() % 100 < 50:
            playerAnimationCurrentKey = "links"
        else:
            playerAnimationCurrentKey = "left1"
        plyer_rect.move_ip(-Plyer_speed, 0)

    # The Plyer Shock
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_RIGHT]:
        stein_rect.x += Stein_speed
        plyer_rect.x = plyer_rect.x - Shock_speed
        activateDamageAnimationPlayer()
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_LEFT]:
        stein_rect.x -= Stein_speed
        plyer_rect.x = plyer_rect.x + Shock_speed
        activateDamageAnimationPlayer()
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_DOWN]:
        stein_rect.y += Stein_speed
        plyer_rect.y = plyer_rect.y - Shock_speed
        activateDamageAnimationPlayer()
    if plyer_rect.colliderect(stein_rect) and keys[pygame.K_UP]:
        stein_rect.y -= Stein_speed
        plyer_rect.y = plyer_rect.y + Shock_speed
        activateDamageAnimationPlayer()

    # Keep the plyer and the Stone on The Screen
    Keep_The_Opj_On_Screen(plyer_rect)
    Keep_The_Opj_On_Screen(stein_rect)

    # Update Player Damage Animation
    if pygame.time.get_ticks() - lastDamageActiveTime < 300:  # Damage flickering on
        if pygame.time.get_ticks() % 100 < 50:
            damaged_animation = True
        else:
            damaged_animation = False
    else:
        damaged_animation = False

    plyer = getPlayerSprite()

    # Move the stone in a random direction
    move_stone(stein, stein_rect, 20)

    # Clear the screen and draw the background and player
    screen.blit(background, (0, 0))
    screen.blit(plyer, plyer_rect)
    screen.blit(stein, stein_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)
