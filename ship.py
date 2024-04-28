import pygame

class Ship():
    def __init__(self, screen):
        self.screen= screen
        self.image = pygame.image.load(r'/home/mno/Desktop/Programas/python/python/a663cf0988f80daae67f7e6fd3db0cf3.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    