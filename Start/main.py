import pygame, sys, time

import EngineTools as ET
import AssetLoader as AL
import EntitiesController as EC

if __name__ == "__main__":
    def exitGame():
        pygame.quit()
        sys.exit()


    # Initialize Pygame and create a window
    pygame.init()
    screen_width, screen_height = 600, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mario")
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()

    EC.globalValues = {
        "screen_width": screen_width,
        "screen_height": screen_height,
    }

    # Load Images
    stein_image = AL.image_stein()
    player_images = AL.loadPlayerImages()
    background_image = AL.image_background(screen_width, screen_height)

    # Create Sprites
    stein_sprite = ET.GameSprite({"default": stein_image}, "default")
    player_sprite = ET.GameSprite(player_images, "unten")

    # Create Entities
    stein_ai = EC.NPC_AI()
    stein = ET.Entity(stein_sprite, x=100, y=100, speed=2,

                      behave=[
                          EC.Keep_The_Opj_On_Screen,
                          stein_ai.move_entity
                      ])

    player = ET.Entity(player_sprite, x=100, y=200,

                       behave=[
                           EC.Keep_The_Opj_On_Screen,
                           EC.move_player,
                           EC.set_player_image_key
                       ])

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()

        # Update the player's position based on key input
        keys = pygame.key.get_pressed()
        EC.globalValues["keys"] = keys

        if keys[pygame.K_ESCAPE]: exitGame()

        player_rect = player.rect
        player.update()

        stein_rect = stein.rect
        stein_speed = stein.speed
        shock_speed = stein.shock_speed
        stein.update()

        # The Player Shock
        if player_rect.colliderect(stein_rect) and keys[pygame.K_RIGHT]:
            stein_rect.x += stein.shock_speed/3

            player_rect.x = player_rect.x - shock_speed
            player_sprite.activate_damage_animation()
        if player_rect.colliderect(stein_rect) and keys[pygame.K_LEFT]:
            stein_rect.x -= stein.shock_speed/3

            player_rect.x = player_rect.x + shock_speed
            player_sprite.activate_damage_animation()
        if player_rect.colliderect(stein_rect) and keys[pygame.K_DOWN]:
            stein_rect.y += stein.shock_speed/3

            player_rect.y = player_rect.y - shock_speed
            player_sprite.activate_damage_animation()
        if player_rect.colliderect(stein_rect) and keys[pygame.K_UP]:
            stein_rect.y -= stein.shock_speed/3

            player_rect.y = player_rect.y + shock_speed
            player_sprite.activate_damage_animation()

        screen.blit(background_image, (0, 0))
        player.draw(screen)
        stein.draw(screen)

        # Update the display
        pygame.display.update()

        # Limit the frame rate to 60 FPS
        clock.tick(60)
