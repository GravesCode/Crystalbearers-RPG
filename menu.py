import pygame

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
    return menu_items
    # Function to handle menu item selection

def mouse_button_handler(menu_items):
    mouse_position_offset = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 420)
    for item in menu_items:
        if item["rect"].collidepoint(mouse_position_offset):
            button_handler(item["action"])  # Call the associated action function

def button_handler(action_button):
    match action_button:
        case "fight_button":
            print("You struck the foe! 37 damage")
        case "technique_button":
            print("You used a special skill! 100 damage")
        case "heal_button":
            print("You healed your party for 49 damage!")
        case "magic_button":
            print("Cast a fireball! 28 damage")
        case "defend_button":
            print("Successfully defended against the strong foe!")
