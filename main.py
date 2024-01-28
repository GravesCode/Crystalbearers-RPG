#Author: Michael Graves
#main.py - main program for running battle simulator
import pygame
import os
from menu import *

#Infrastructure for microservice architecture
import pika

#pygame library initialization - mandatory
pygame.init()

#Screen setup
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#Hero loading
hero_class = "fighter"
hero = pygame.transform.scale(
    pygame.image.load('images\\fighter.png'),
    (150,150))

#Enemy loading
enemy_name = "Lethal Weapon"
enemy = pygame.transform.scale(
    pygame.image.load('images\\Lethalweapon.png'),
    (150,150))

#Menu setup - different menus for different classes for create_menu param
menu_items = create_menu(hero_class)
menu_surface = create_menu_surface(menu_items)

clock = pygame.time.Clock()
running = True

# fill the screen with a color to wipe away anything from last frame
screen.fill((000,255,255))
screen.blit(enemy, (300,200))
screen.blit(hero, (800,200))
screen.blit(menu_surface, (0,420))
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
            mouse_position_on_menu = (mouse_position[0], mouse_position[1] - 420)  # Adjust for menu offset
            mouse_button_handler(menu_items, mouse_position_on_menu)  # Pass adjusted position

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60) / 1000

pygame.quit()