import pygame
class Ship():
    def __init__(self,screen,ai_settings):
        self.screen = screen
        # Rectification
        self.image = pygame.image.load('images/ship.png') 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.ai_settings = ai_settings
        # Setting co-ordinates
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # For faster movement 
        self.center = float(self.rect.centerx)
        # Setting Flag for(holding)
        self.moving_right = False
        self.moving_left = False 
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        # Reassigning centerx co-ordinates
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx
        
