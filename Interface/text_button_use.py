# pylint: disable=no-member
# pylint: disable=all
import pygame
import sys

# Clase que crea cuadriculas de entrada de texto solo numeros
class TextInput:
    def __init__(self, x, y, w, h, font_size=32, text_color=(0, 0, 0), bg_color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.text = ''
        self.is_active = False
        self.text_surface = self.font.render('', True, self.text_color)

    def handle_event_text(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_active = True
            else:
                self.is_active = False
            self.bg_color = (200, 200, 200) if self.is_active else (255, 255, 255)
        if event.type == pygame.KEYDOWN:
            if self.is_active:
                if event.key == pygame.K_RETURN:
                    value = self.text
                    self.text = ''
                    self.text_surface = self.font.render(self.text, True, self.text_color)
                    return value
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.text_surface = self.font.render(self.text, True, self.text_color)
                else:
                    self.text += event.unicode
                    self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw_text(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, 2)
        screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))



# Class de entrada de texto solo letras
class TextInput_text(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, font_family, font_size):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.SysFont(font_family, font_size)
        self.text_color = (0, 0, 0)
        self.text = ""
        self.rendered_text = None
        self.active = True  # Hacer que la entrada de texto esté activa desde el inicio
        self.allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.position = (x, y)

    def validate_key(self, key):
        valido = False
        if key in self.allowed_chars:
            valido = True
        elif key == "\b":
            valido = True
        return valido

    def add_text(self, text):
        self.text += text
        self.rendered_text = self.font.render(self.text, True, self.text_color)

    def delete_text(self):
        if len(self.text) > 0:
            self.text = self.text[:-1]
            self.rendered_text = self.font.render(self.text, True, self.text_color)

    def get_text(self):
        if any(c.isalpha() for c in self.text):
            return self.text
        else:
            return ""

    def draw_txt(self, surface):
        if self.rendered_text is None:
            self.rendered_text = self.font.render(self.text, True, self.text_color)

        rect = self.rendered_text.get_rect()
        rect.topleft = self.position
        pygame.draw.rect(surface, self.image.get_at((0,0)), rect)
        surface.blit(self.rendered_text, self.position)

    def handle_event_txt(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                return self.text
            elif event.key == pygame.K_ESCAPE:
                self.active = False
                self.text = ""
            elif self.validate_key(event.unicode):
                self.add_text(event.unicode)    