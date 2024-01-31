import pygame

def create_menu(hero_class):
    match hero_class:
        case "fighter":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
                { "text": "Technique", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": technique_button},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
            ]
        case "whitemage":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
                { "text": "Heal", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": heal_button},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
            ]
        case "blackmage":
            menu_items = [
                { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
                { "text": "Magic", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": magic_button},
                { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
            ]
        case _:
            #Default selection. Should not resolve here
            menu_items = [
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": magic_button},
                { "text": "Error", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
            ]
    return menu_items

def create_menu_surface(menu_items):
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
    # Function to handle menu item selection
    return menu_surface

def mouse_button_handler(menu_items, mouse_pos):
    for item in menu_items:
        if item["rect"].collidepoint(mouse_pos):
            item["action"]()  # Call the associated action function

def fight_button():
    print("You struck the foe! 37 damage")

def technique_button():
    print("You used a special skill! 100 damage")

def heal_button():
    print("You healed your party for 49 damage!")

def magic_button():
    print("Cast a fireball! 28 damage")

def defend_button():
    print("Successfully defended against the strong foe!")

#Define distance between top and bottom to place menu position
menu_vertical_offset = 420

#When user is able to choose a class, scalable towards other choices of menu items

