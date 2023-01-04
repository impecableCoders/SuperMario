import pygame, random
import EngineTools as ET

globalValues = {
    "screen_height": 0,
    "screen_width": 0,
    "keys": []
}


def damage_event_entities(victim_entity: ET.Entity, attack_entity: ET.Entity):
    ve_rect = victim_entity.rect
    ae_rect = attack_entity.rect

    distance_x = ae_rect.centerx - ve_rect.centerx
    distance_y = ae_rect.centery - ve_rect.centery

    if abs(distance_x/ve_rect.w) > abs(distance_y/ve_rect.h):
        if distance_x > 0:
            ae_rect.x += attack_entity.shock_speed / 3
            ve_rect.x -= attack_entity.shock_speed
            victim_entity.sprite.activate_damage_animation()
        elif distance_x < 0:
            ae_rect.x -= attack_entity.shock_speed / 3
            ve_rect.x += attack_entity.shock_speed
            victim_entity.sprite.activate_damage_animation()
    else:
        if distance_y > 0:
            ae_rect.y += attack_entity.shock_speed / 3
            ve_rect.y -= attack_entity.shock_speed
            victim_entity.sprite.activate_damage_animation()
        elif distance_y < 0:
            ae_rect.y -= attack_entity.shock_speed / 3
            ve_rect.y += attack_entity.shock_speed
            victim_entity.sprite.activate_damage_animation()


def Keep_The_Opj_On_Screen(entity: ET.Entity):
    Obj_rect = entity.rect
    screen_height = globalValues["screen_height"]
    screen_width = globalValues["screen_width"]

    if Obj_rect.bottom > screen_height:
        Obj_rect.bottom = screen_height
    if Obj_rect.right > screen_width:
        Obj_rect.right = screen_width
    if Obj_rect.top < 0:
        Obj_rect.top = 0
    if Obj_rect.left < 0:
        Obj_rect.left = 0


# STONE ##################################################################################

class NPC_AI:
    def __init__(self):
        self.movement_timer = ET.Timer(min_duration=600, max_duration=1600)
        self.idle_timer = ET.Timer(min_duration=100, max_duration=500)

        self.movement_timer.start_timer()
        self.idle_timer.start_timer()

    def move_entity(self, entity: ET.Entity):
        if self.movement_timer.hasStopped():
            self.movement_timer.stop_checked = True
            entity.vel_x, entity.vel_y = 0.0, 0.0

            self.idle_timer.start_with_random_duration()

        if self.idle_timer.hasStopped():
            self.idle_timer.stop_checked = True

            directions = ["S", "SW", "W", "NW", "N", "NE", "E", "SE"]
            direction = random.choice(directions)

            speed = entity.speed

            if direction == "S":
                entity.vel_x, entity.vel_y = 0, speed
            elif direction == "SW":
                entity.vel_x, entity.vel_y = -speed, speed
            elif direction == "W":
                entity.vel_x, entity.vel_y = -speed, 0
            elif direction == "NW":
                entity.vel_x, entity.vel_y = -speed, -speed
            elif direction == "N":
                entity.vel_x, entity.vel_y = 0, -speed
            elif direction == "NE":
                entity.vel_x, entity.vel_y = speed, -speed
            elif direction == "E":
                entity.vel_x, entity.vel_y = speed, 0
            elif direction == "SE":
                entity.vel_x, entity.vel_y = speed, speed

            self.movement_timer.start_timer()


# Player ##################################################################################

def move_player(entity: ET.Entity):
    keys = globalValues["keys"]
    plyer_speed = entity.speed

    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        entity.vel_x = plyer_speed
    elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        entity.vel_x = -plyer_speed
    else:
        entity.vel_x = 0

    if keys[pygame.K_UP]:
        entity.vel_y = -plyer_speed
    elif keys[pygame.K_DOWN]:
        entity.vel_y = plyer_speed
    else:
        entity.vel_y = 0


def set_player_image_key(entity: ET.Entity):
    keys = globalValues["keys"]
    player_sprite = entity.sprite

    if keys[pygame.K_UP]: player_sprite.current_animation_key = "oben"
    if keys[pygame.K_DOWN]: player_sprite.current_animation_key = "unten"

    if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]: player_sprite.current_animation_key = "unten"

    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        if pygame.time.get_ticks() % 100 < 50:
            player_sprite.current_animation_key = "rechts"
        else:
            player_sprite.current_animation_key = "right1"
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if pygame.time.get_ticks() % 100 < 50:
            player_sprite.current_animation_key = "links"
        else:
            player_sprite.current_animation_key = "left1"
