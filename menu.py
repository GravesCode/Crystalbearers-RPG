import pygame
import requests
import time
RNGServer = 'http://localhost:8000/api/rng/provider/'

class enemy_health:
    val = 100
    max = 100
    text = 0

class hero_health:
    val = 0
    max = 0

def create_menu(hero_class, screen):
    match hero_class:
        case "fighter":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'fight_button'},
                { "text": "Technique", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'technique_button'},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'defend_button'},
            ]
        case "whitemage":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'fight_button'},
                { "text": "Heal", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'heal_button'},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'defend_button'},
            ]
        case "blackmage":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'fight_button'},
                { "text": "Magic", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'magic_button'},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'defend_button'},
            ]
        case _:
            #Default selection. Should not resolve here
            menu_items = [
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'fight_button'},
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'magic_button'},
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": 'defend_button'},
            ]

    item_spacing = 50  # Adjust spacing between items
    y_offset = 50  # Adjust starting vertical position
    menu_width = 1280
    menu_height = 300
    menu_surface = pygame.Surface((menu_width, menu_height))
    menu_surface.fill((0, 0, 0))
    for item in menu_items:
        text_surface = item["font"].render(item["text"], True, item["color"])
        text_rect = text_surface.get_rect(center=(850, y_offset))
        menu_surface.blit(text_surface, text_rect)
        item["rect"] = text_rect  # Store rectangle for click detection
        y_offset += text_rect.height + item_spacing
    screen.blit(menu_surface, (0,420))

    #Create health status
    match hero_class:
        case "fighter":
            hero_health.val = 150
            hero_health.max = 150
        case "whitemage":
            hero_health.val = 100
            hero_health.max = 100
        case "blackmage":
            hero_health.val = 100
            hero_health.max = 100
    hero_health_text = pygame.font.Font(None,48).render("HP: "+str(hero_health.val)+"/"+str(hero_health.max), True, (255,0,0))
    enemy_health.text = pygame.font.Font(None,48).render("HP: "+str(enemy_health.val)+"/"+str(enemy_health.max), True, (255,0,0))
    screen.blit(hero_health_text, (850,125))
    screen.blit(enemy_health.text, (325,125))

    return menu_items
    # Function to handle menu item selection

def mouse_button_handler(menu_items, screen):
    mouse_position_offset = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 420)
    for item in menu_items:
        if item["rect"].collidepoint(mouse_position_offset):
            match item["action"]:
                case "fight_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("You damaged the Foe!", result.json()["random_number"], " damage.")
                    damage_handler("enemy", result.json()["random_number"], screen)
                case "technique_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("You used a special skill!", result, "damage")
                case "heal_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("You healed your party for", result, "damage!")
                case "magic_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("Cast a fireball!", result, " damage.")
                case "defend_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("Successfully defended against the strong foe! Reduced damage by ", result, ".")
            #Enter combat
            result = requests.get(RNGServer, {'min': 25, 'max': 50})
            damage_handler("hero", result.json()["random_number"], screen)
            print("The foe damaged you! ", result.json()["random_number"], " damage.")
            pygame.display.update()

def mouse_hover_handler(menu_items, screen):
    mouse_position_offset = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 420)
    for item in menu_items:
        if item["rect"].collidepoint(mouse_position_offset):
            match item["action"]:
                case "fight_button":
                    pygame.draw.rect(screen, (0, 255, 0), [775, 440, 150, 50], 5)
                    pygame.display.update()
                    #Draw rectangle
                case "technique_button":
                    pygame.draw.rect(screen, (0, 255, 0), [775, 515, 150, 50], 5)
                    pygame.display.update()
                    #Draw rectangle
                case "heal_button":
                    print("NOP")
                    #Draw rectangle
                case "magic_button":
                    print("NOP")
                    #Draw rectangle
                case "defend_button":
                    pygame.draw.rect(screen, (0, 255, 0), [775, 590, 150, 50], 5)
                    pygame.display.update()
                    #Draw rectangle
            break
        else:
            #Remove triangle
            pygame.draw.rect(screen, (0, 0, 0), [775, 440, 150, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [775, 515, 150, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [775, 590, 150, 50], 5)

def damage_handler(target, adjustment, screen):
    if(target == "hero"):
        hero_health.val = hero_health.val - adjustment
        hero_health.text = pygame.font.Font(None,48).render("HP: "+str(hero_health.val)+"/"+str(hero_health.max), True, (255,0,0))
        screen.fill((000,255,255), (825,125,300, 40))
        screen.blit(hero_health.text, (825,125))
    elif(target == "enemy"):
        if(adjustment > enemy_health.val):
            enemy_health.val = 0
        else:
            enemy_health.val = enemy_health.val - adjustment
        enemy_health.text = pygame.font.Font(None,48).render("HP: "+str(enemy_health.val)+"/"+str(enemy_health.max), True, (255,0,0))
        screen.fill((000,255,255), (325,125,300, 40))
        screen.blit(enemy_health.text, (325,125))
        if(enemy_health.val == 0):
            endgame_handler("win", screen)

def endgame_handler(condition, screen):
    match(condition):
        case "win":
            enemy_skull = pygame.transform.scale(
                    pygame.image.load('images\\skull.png'),
                    (250,250))
            screen.blit(enemy_skull, (260,160))
            pygame.display.update()
            print("You win!")
        case "lose":
            print("You lose!")
    time.sleep(5)
    pygame.quit()
    exit()