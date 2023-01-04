import pygame

collision_condition = lambda e1, e2: e1.rect.colliderect(e2)


def cross_check_entities(e1: list, e2: list, condition: callable, event: callable) -> None:
    for entity1 in e1:
        for entity2 in e2:
            if condition(entity1, entity2):
                event(entity1, entity2)
