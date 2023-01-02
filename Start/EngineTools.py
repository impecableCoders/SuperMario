import random
import pygame
from pygame.rect import Rect, RectType

class Timer:
    def __init__(self, duration=500, min_duration=0, max_duration=0):
        self.last_time = -1

        self.duration = duration
        self.min_duration = min_duration
        self.max_duration = max_duration

        self.stop_checked = False

    def start_timer(self):
        self.last_time = pygame.time.get_ticks()
        self.stop_checked = False

    def start_with_random_duration(self):
        self.duration = random.randint(self.min_duration, self.max_duration)
        self.start_timer()

    def hasStopped(self):
        return pygame.time.get_ticks() - self.last_time > self.duration and not self.stop_checked


class GameSprite:
    def __init__(self, images: dict, current_image_key: str):
        self.animations = images

        # Kopie von Animations-Dict mit Damage Animationsbilder
        self.damage_images = {}
        for key in self.animations.keys():
            new_image = self.animations[key].copy()
            # Färbe die Bilder in Rot
            new_image.fill((255, 0, 0, 128), special_flags=pygame.BLEND_ADD)
            self.damage_images[key] = new_image

        self.current_animation_key = current_image_key
        self.damage_timer = Timer(duration=300)

    def get_current_sprite(self) -> pygame.Surface:
        if self.is_damage_animation_on():
            return self.damage_images[self.current_animation_key]
        return self.animations[self.current_animation_key]

    def activate_damage_animation(self) -> None:
        self.damage_timer.start_timer()

    def is_damage_animation_on(self) -> bool:
        return not self.damage_timer.hasStopped() and pygame.time.get_ticks() % 100 < 50

    def get_surface_rect(self, x=0, y=0) -> Rect | RectType:
        return self.get_current_sprite().get_rect(x=x, y=y)


class Entity:
    def __init__(self,
                 sprite: GameSprite, x: float = 0.0, y: float = 0.0,
                 speed=5.0, shock_speed=50,
                 behave: list = None):

        self.speed = speed
        self.behave = behave
        self.shock_speed = shock_speed

        self.vel_x, self.vel_y = 0, 0

        self.sprite = sprite
        # Rect hat alle Werte, die ein Spielobject hat. Zb. Position, Top, left, .., Collision, usw...
        self.rect = self.sprite.get_surface_rect(x, y)

    def update(self):
        if self.behave is None or len(self.behave) == 0:
            return

        for function in self.behave:
            function(self)

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, screen: pygame.Surface | pygame.SurfaceType):
        screen.blit(self.sprite.get_current_sprite(), self.rect)
