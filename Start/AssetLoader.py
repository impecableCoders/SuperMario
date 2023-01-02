import pygame


def load_image_plyer(image, default_width_scale=30, default_height_scale=50) -> pygame.Surface | pygame.SurfaceType:
    plyer_image = pygame.image.load('Bilder/' + image + '.png').convert_alpha()
    pygame.transform.scale(plyer_image, (default_width_scale, default_height_scale))
    return plyer_image


def image_stein() -> pygame.Surface | pygame.SurfaceType:
    Stein_img = pygame.image.load("Bilder/Steine/1.png").convert_alpha()
    stein = pygame.transform.smoothscale(Stein_img, (30, 30))
    return stein


def image_background(screen_width, screen_height) -> pygame.Surface | pygame.SurfaceType:
    o_background1 = pygame.image.load("Bilder/background1.jpg").convert_alpha()
    background1 = pygame.transform.scale(o_background1, (screen_width, screen_height))
    return background1


def loadPlayerImages() -> dict:
    return {"left1": load_image_plyer("left1"),
            "links": load_image_plyer("links"),
            "oben": load_image_plyer("oben"),
            "rechts": load_image_plyer("rechts"),
            "right1": load_image_plyer("right1"),
            "unten": load_image_plyer("unten")}
