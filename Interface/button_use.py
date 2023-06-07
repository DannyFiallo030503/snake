# pylint: disable=no-member
# pylint: disable=all
import pygame
import sys

#clase que crea botones
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action

    def draw(self, surface, fontd):
        pygame.draw.rect(surface, self.color, self.rect)
        text = fontd.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self, evente):
        if evente.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(evente.pos):
            if self.action:
                 return self.action()
        return None