#Author: Michael Graves
#main.py - main program for running battle simulator
import pygame
import os
import time
from menu import *

#Infrastructure for microservice architecture
import pika

#pygame library initialization - mandatory
pygame.init()

#CRPG_INTRO_SCREEN
# fill the screen with a color to wipe away anything from last frame
#Screen setup - can be abstracted to another file
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((000,000,0xFF))
char_class_prompt = pygame.font.Font(None,32).render("Choose your character!", True, (255,255,255))
screen.blit(char_class_prompt, (500,100))
fighter_image = pygame.transform.scale(
    pygame.image.load('images\\fighter.png'),
    (150,150))
whitemage_image = pygame.transform.scale(
    pygame.image.load('images\\whitemage.png'),
    (150,150))
blackmage_image = pygame.transform.scale(
    pygame.image.load('images\\blackmage.png'),
    (150,150))
fighter_intro_rect = fighter_image.get_rect(center=(320, 275))
whitemage_intro_rect = whitemage_image.get_rect(center=(620, 275))
blackmage_intro_rect = blackmage_image.get_rect(center=(920, 275))
screen.blit(fighter_image, (250,200))
screen.blit(whitemage_image, (550,200))
screen.blit(blackmage_image, (850,200))
pygame.display.update()

character_selected = False
#wait in an infinite loop waiting for player to select character image
while(character_selected is False):
    intro_mouse_position = pygame.mouse.get_pos()
    if(fighter_intro_rect.collidepoint(intro_mouse_position)):
        pygame.draw.circle(screen, (255, 0, 0), fighter_intro_rect.center, fighter_intro_rect.width // 2, 5)
        pygame.display.update()
    elif(whitemage_intro_rect.collidepoint(intro_mouse_position)):
        pygame.draw.circle(screen, (255, 0, 0), whitemage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.display.update()
    elif(blackmage_intro_rect.collidepoint(intro_mouse_position)):
        pygame.draw.circle(screen, (255, 0, 0), blackmage_intro_rect.center, whitemage_intro_rect.width // 2, 5)
        pygame.display.update()
    else:
        pygame.draw.circle(screen, (0, 0, 0xFF), fighter_intro_rect.center, fighter_intro_rect.width // 2, 5)
        pygame.draw.circle(screen, (0, 0, 0xFF), whitemage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.draw.circle(screen, (0, 0, 0xFF), blackmage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(fighter_intro_rect.collidepoint(intro_mouse_position)):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\fighter.png'),
                    (150,150))
                hero_class = "fighter"
            elif(whitemage_intro_rect.collidepoint(intro_mouse_position)):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\whitemage.png'),
                    (150,150))
                hero_class = "whitemage"
            elif(blackmage_intro_rect.collidepoint(intro_mouse_position)):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\blackmage.png'),
                    (150,150))
                hero_class = "blackmage"
#Display selected character image

#Introduce a prompt for the user to name their character
char_class_prompt = pygame.font.Font(None,32).render("Name your character:", True, (255,255,255))
screen.fill((000,000,000))
screen.blit(char_class_prompt, (500,100))
character_name_box = pygame.draw.rect(screen, (0Xff,0XFF,0XFF), pygame.Rect(500, 150, 250, 40))
screen.blit(character_selected, (500,350))
pygame.display.update()

#While the name has not been entered
character_name_flag = False
character_name_input = ''
while(character_name_flag == False):
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RETURN):
                character_name_flag = True
            elif(event.key == pygame.K_BACKSPACE):
                if(character_name_input != ''):
                    character_name_input = character_name_input[:-1]
            else:
                character_name_input += event.unicode
    name_surface = pygame.font.Font(None, 50).render(character_name_input, True, (0x22,0x49,0x7F))
    screen.blit(name_surface, (510, 155))
    pygame.display.update()
    pygame.display.flip()

#Splash window - introduce game and give instructions to player
#Could make up for heuristics of someone who needs process and a game walkthrough

#Hero loading - abstract to another file
#Link to previous user input
match hero_class:
    case "fighter":
        hero = pygame.transform.scale(
            pygame.image.load('images\\fighter.png'),
            (150,150))
    case "whitemage":
        hero = pygame.transform.scale(
            pygame.image.load('images\\whitemage.png'),
            (150,150))
    case "blackmage":
        hero = pygame.transform.scale(
            pygame.image.load('images\\blackmage.png'),
            (150,150))
    case "default":
        hero = None

#Enemy loading - abstract to another file
enemy_name = "Lethal Weapon"
enemy = pygame.transform.scale(
    pygame.image.load('images\\Lethalweapon.png'),
    (150,150))

#Menu setup - different menus for different classes for create_menu param
menu_items = create_menu(hero_class)
menu_surface = create_menu_surface(menu_items)

clock = pygame.time.Clock()
running = True

screen.fill((000,255,255))
screen.blit(enemy, (300,200))
screen.blit(hero, (800,200))
screen.blit(menu_surface, (0,420))
screen.blit(name_surface, (825, 180))
pygame.display.update()

#Main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_handler(menu_items)  # Pass adjusted position

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60) / 1000

pygame.quit()