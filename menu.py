import pygame
import requests

RNGServer = 'http://localhost:8000/api/rng/provider/'

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

    enemy_health_val = 100
    enemy_health_max = 100
    hero_health_val = 0
    hero_health_max = 0
    #Create health status
    match hero_class:
        case "fighter":
            hero_health_val = 150
            hero_health_max = 150
        case "whitemage":
            hero_health_val = 100
            hero_health_max = 100
        case "blackmage":
            hero_health_val = 100
            hero_health_max = 100
    hero_health_text = pygame.font.Font(None,48).render("HP: "+str(hero_health_val)+"/"+str(hero_health_max), True, (255,0,0))
    enemy_health_text = pygame.font.Font(None,48).render("HP: "+str(enemy_health_val)+"/"+str(enemy_health_max), True, (255,0,0))
    screen.blit(hero_health_text, (850,125))
    screen.blit(enemy_health_text, (325,125))

    return menu_items
    # Function to handle menu item selection

def mouse_button_handler(menu_items):
    mouse_position_offset = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 420)
    for item in menu_items:
        if item["rect"].collidepoint(mouse_position_offset):
            match item["action"]:
                case "fight_button":
                    result = requests.get(RNGServer, {'min': 50, 'max': 100})
                    print("You damaged the Foe!", result.json()["random_number"], " damage.")
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