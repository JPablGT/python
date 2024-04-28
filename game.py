import pygame
from setttings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))  
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        gf.check_events() 
        pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        
run_game()