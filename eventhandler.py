import pygame
from menu import *

#Code to handle all of the game eventsfor event in pygame.event.get():
def eventhandler(event, menu_items):
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Get mouse position relative to screen
        mouse_position = event.pos 
        #Have to manually reduce 420 to adjust from Y axis.. Don't know how to do this cleaner
        mouse_position_on_menu = (mouse_position[0], mouse_position[1] - 420)
        mouse_button_handler(menu_items, mouse_position_on_menu)  # Pass adjusted position
    return True