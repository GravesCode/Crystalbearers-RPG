#Author: Michael Graves
#main.py - main program for running battle simulator
import pygame
import os
import menu
#Infrastructure for microservice architecture
import pika

# pygame setup
pygame.init()

#Define Overall Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
#Give user the option to choose a hero class
hero_class = "fighter"
enemy = pygame.transform.scale(
    pygame.image.load('images\\Lethalweapon.png'),
    (150,150))
hero = pygame.transform.scale(
    pygame.image.load('images\\fighter.png'),
    (150,150))

#MENU SETUP SECTION
menu_width = 1280
menu_height = 300
menu_surface = pygame.Surface((menu_width, menu_height))
menu_surface.fill((0, 0, 0))
# Function to handle menu item selection
def mouse_button_handler(menu_items, mouse_pos):
    for item in menu_items:
        if item["rect"].collidepoint(mouse_pos):

            item["action"]()  # Call the associated action function

def fight_button():
    print("You struck the foe! 37 damage")

def technique_button():
    print("You used a special skill! 100 damage")

def magic_button():
    print("Cast a fireball! 28 damage")

def defend_button():
    print("Successfully defended against the strong foe!")

#Define distance between top and bottom to place menu position
menu_vertical_offset = 420

#When user is able to choose a class, scalable towards other choices of menu items
match hero_class:
    case "fighter":
        menu_items = [
            { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
            { "text": "Magic", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": technique_button},
            { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
        ]
    case _:
        #Default selection. Should not resolve here
        menu_items = [
            { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
            { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": magic_button},
            { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
        ]
item_spacing = 50  # Adjust spacing between items
y_offset = 50  # Adjust starting vertical position
for item in menu_items:
    text_surface = item["font"].render(item["text"], True, item["color"])
    text_rect = text_surface.get_rect(center=(850, y_offset))
    menu_surface.blit(text_surface, text_rect)
    item["rect"] = text_rect  # Store rectangle for click detection
    y_offset += text_rect.height + item_spacing

clock = pygame.time.Clock()
running = True

# fill the screen with a color to wipe away anything from last frame
screen.fill((000,255,255))
screen.blit(enemy, (300,200))
screen.blit(hero, (800,200))
screen.blit(menu_surface, (0,menu_vertical_offset))
pygame.display.update()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position relative to screen
            mouse_position = event.pos 
            mouse_position_on_menu = (mouse_position[0], mouse_position[1] - menu_vertical_offset)  # Adjust for menu offset
            mouse_button_handler(menu_items, mouse_position_on_menu)  # Pass adjusted position

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60) / 1000

pygame.quit()