# Example file showing a circle moving on screen
import pygame
import os
import time

# pygame setup
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
enemy = pygame.image.load("C:\\Users\\mjgra\\OneDrive\\Documents\\CS361\\Project\\images\\Lethalweapon.png")
screen.blit(enemy, (400, 400))
screen.fill((000,255,255))
screen.blit(enemy, (400, 400))
pygame.display.update()
time.sleep(1)
screen.blit(enemy,(200,200))
pygame.display.update()
time.sleep(1)
screen.blit(enemy,(600,600))
pygame.display.update()
while(1):
    time.sleep(1)