#Author: Michael Graves
#main.py - main program for running battle simulator
import pygame
import os
import time
#Infrastructure for microservice architecture
import pika
import requests
from menu import *

#pygame initialization - mandatory
pygame.init()
clock = pygame.time.Clock()
running = True

#CRPG_INTRO_SCREEN
# fill the screen with a color to wipe away anything from last frame
#Screen setup - can be abstracted to another file
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((000,000,0xFF))

#Introduction Screen
intro_line_1 = pygame.font.Font(None,32).render("Welcome to the game.", True, (255,255,255))
intro_line_2 = pygame.font.Font(None,32).render("The objective of the game is to defeat the enemy.", True, (255,255,255))
intro_line_3 = pygame.font.Font(None,32).render("You will be given the choice of a character.", True, (255,255,255))
intro_line_4 = pygame.font.Font(None,32).render("Please choose between Black Mage, White Mage, or Fighter classes.", True, (255,255,255))
intro_line_5 = pygame.font.Font(None,32).render("Your choice of character will determine the options of playing.", True, (255,255,255))
intro_line_6 = pygame.font.Font(None,32).render("Consider trying new classes to fit the monster that you will be facing.", True, (255,255,255))
intro_line_7 = pygame.font.Font(None,32).render("Press Okay to acknowledge.", True, (255,255,255))
intro_line_8 = pygame.font.Font(None,32).render("Okay", True, (255,255,255))
screen.blit(intro_line_1, (425,100))
screen.blit(intro_line_2, (425,150))
screen.blit(intro_line_3, (425,200))
screen.blit(intro_line_4, (425,250))
screen.blit(intro_line_5, (425,300))
screen.blit(intro_line_6, (425,350))
screen.blit(intro_line_7, (425,400))
screen.blit(intro_line_8, (425,450))
okay_button_rect = pygame.draw.rect(screen, (255, 0, 0), [400, 440, 100, 50], 5)
pygame.display.update()
is_okay_pressed = False
while(False == is_okay_pressed):
    for event in pygame.event.get():
        if(okay_button_rect.collidepoint(pygame.mouse.get_pos())):
            okay_button_rect = pygame.draw.rect(screen, (0, 255, 0), [400, 440, 100, 50], 5)
            pygame.display.update()
        else:
            okay_button_rect = pygame.draw.rect(screen, (255, 0, 0), [400, 440, 100, 50], 5)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(okay_button_rect.collidepoint(pygame.mouse.get_pos())):
                is_okay_pressed = True
                screen.fill((000,000,0xFF))
                pygame.display.update()

#Character class initialization
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
fighter_intro_text = pygame.font.Font(None,32).render("Fighter", True, (255,255,255))
blackmage_intro_text = pygame.font.Font(None,32).render("Black Mage", True, (255,255,255))
whitemage_intro_text = pygame.font.Font(None,32).render("White Mage", True, (255,255,255))
screen.blit(fighter_intro_text, (275,375))
screen.blit(whitemage_intro_text, (575,375))
screen.blit(blackmage_intro_text, (875,375))
screen.blit(fighter_image, (250,200))
screen.blit(whitemage_image, (550,200))
screen.blit(blackmage_image, (850,200))
pygame.display.update()

character_selected = False
#wait in an infinite loop waiting for player to select character image
while(character_selected is False):
    if(fighter_intro_rect.collidepoint(pygame.mouse.get_pos())):
        pygame.draw.circle(screen, (255, 0, 0), fighter_intro_rect.center, fighter_intro_rect.width // 2, 5)
        pygame.display.update()
    elif(whitemage_intro_rect.collidepoint(pygame.mouse.get_pos())):
        pygame.draw.circle(screen, (255, 0, 0), whitemage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.display.update()
    elif(blackmage_intro_rect.collidepoint(pygame.mouse.get_pos())):
        pygame.draw.circle(screen, (255, 0, 0), blackmage_intro_rect.center, whitemage_intro_rect.width // 2, 5)
        pygame.display.update()
    else:
        pygame.draw.circle(screen, (0, 0, 0xFF), fighter_intro_rect.center, fighter_intro_rect.width // 2, 5)
        pygame.draw.circle(screen, (0, 0, 0xFF), whitemage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.draw.circle(screen, (0, 0, 0xFF), blackmage_intro_rect.center, blackmage_intro_rect.width // 2, 5)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(fighter_intro_rect.collidepoint(pygame.mouse.get_pos())):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\fighter.png'),
                    (150,150))
                hero_class = "fighter"
            elif(whitemage_intro_rect.collidepoint(pygame.mouse.get_pos())):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\whitemage.png'),
                    (150,150))
                hero_class = "whitemage"
            elif(blackmage_intro_rect.collidepoint(pygame.mouse.get_pos())):
                character_selected = pygame.transform.scale(
                    pygame.image.load('images\\blackmage.png'),
                    (150,150))
                hero_class = "blackmage"
#Display selected character image

#Introduce a prompt for the user to name their character
char_class_prompt = pygame.font.Font(None,32).render("Name your character:", True, (255,255,255))
screen.fill((000,000,0xFF))
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
screen.fill((000,255,255))
screen.blit(enemy, (300,200))
screen.blit(hero, (800,200))
menu_items = create_menu(hero_class, screen)
screen.blit(name_surface, (825, 180))
pygame.display.update()

#Main game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        mouse_hover_handler(menu_items, screen)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_handler(menu_items, screen)  # Pass adjusted position

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60) / 1000

pygame.quit()