import pygame

#Define distance between top and bottom to place menu position
menu_vertical_offset = 420

def menu_init():
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

    def magic_button():
        print("Cast a fireball! 28 damage")

    def defend_button():
        print("Successfully defended against the strong foe!")


    menu_items = [
        { "text": "Fight", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": fight_button},
        { "text": "Magic", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": magic_button},
        { "text": "Defend", "color": (255,255,255), "font": pygame.font.Font(None, 32), "action": defend_button},
    ]
    item_spacing = 50  # Adjust spacing between items
    y_offset = 50  # Adjust starting vertical position
    for item in menu_items:
        text_surface = item["font"].render(item["text"], True, item["color"])
        text_rect = text_surface.get_rect(center=(850, y_offset))
        menu_surface.blit(text_surface, text_rect)
        item["rect"] = text_rect  # Store rectangle for click detection
        y_offset += text_rect.height + item_spacing