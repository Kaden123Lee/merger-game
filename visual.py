import pygame
import board
import constants
# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((222, 184, 135))
valid_moves = []
color = (255,255,255) # white text color
color_light = (170,170,170) 
color_dark = (100,100,100) 
width = screen.get_width() 
height = screen.get_height() 
smallfont = pygame.font.SysFont('Corbel',35) 
quit = smallfont.render('Quit' , True , color) 
place = smallfont.render('Place', True, color)
temp_board = board.Board()

## Give number their image



    
            


# MAIN GAME
def draw_board():
    for i in range(8):
        ## 
        column = i % 2 # (0, 1, 0, 1, 0, 1)
        row = i // 2   # (0, 0, 1, 1, 2, 2)
        if row % 2 == 0: #                          position                 size 
            pygame.draw.rect(screen, (205,133,63), [400- column * 400, row * 200, 200, 200])
        else:
            pygame.draw.rect(screen, (205,133,63), [600 - column * 400, row * 200, 200, 200])
        
    
    for line in range(5):
        pygame.draw.line(screen, 'black', (0, 200 * line), (800, 200*line), 6)
        pygame.draw.line(screen, 'black', (200 * line, 0), (200 * line, 800), 6)
def draw_button(mouse, text, color, hover_color, width, height):
    pygame.draw.rect(screen,color,[width,height,140,40])  # Draws the rectangle with Quit
    if width <= mouse[0] <= width+140 and height <= mouse[1] <= height+40: 
        pygame.draw.rect(screen,hover_color,[width,height,140,40])        
    screen.blit(text, (width+50,height)) 
def button_function(mouse, width, height, function):
    if width <= mouse[0] <= width+140 and height <= mouse[1] <= height+40: # Quit button
        if function == "quit":
            pygame.quit() 
        if function == "place":
            temp_board.place_new_random()

temp_location = {0 : (0, 0), 1 : (1, 0), 2: (2, 0), 3: (3, 0), 
                4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (3, 1), 
                8: (0, 2), 9: (1, 2), 10: (2, 2), 11: (3, 2), 
                12: (0, 3), 13: (1, 3), 14: (2, 3), 15: (3, 3),}
def draw_pieces():
    numbers = temp_board.convert_to_1D()
    for i in range(len(numbers)):
        x = temp_location[i][0]
        y = temp_location[i][1]
        if numbers[i] == 1:
            screen.blit(constants.One, (x * 200, y * 200))
        elif numbers[i] == 2:
            screen.blit(constants.Two, (x * 200, y * 200))
        elif numbers[i] == 3:
            screen.blit(constants.Three, (x * 200, y * 200))
        elif numbers[i] == 4:
            screen.blit(constants.Four, (x * 200, y * 200))
        elif numbers[i] == 5:
            screen.blit(constants.Five, (x * 200, y * 200))
        elif numbers[i] == 6:
            screen.blit(constants.Six, (x * 200, y * 200))
        elif numbers[i] == 7:
            screen.blit(constants.Seven, (x * 200, y * 200))
        elif numbers[i] == 8:
            screen.blit(constants.Eight, (x * 200, y * 200))
        elif numbers[i] == 9:
            screen.blit(constants.Nine, (x * 200, y * 200))
        elif numbers[i] == 10:
            screen.blit(constants.Ten, (x * 200, y * 200))
        elif numbers[i] == 11:
            screen.blit(constants.Eleven, (x * 200, y * 200))
        elif numbers[i] == 12:
            screen.blit(constants.Twelve, (x * 200, y * 200))
            
            
def check_options(pieces, locations, turn):
    pass

        
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Tells what grid cell it is in and saves as a tuple
            x_coord = event.pos[0] // 200
            y_coord = event.pos[1] // 200
            click_coords = (x_coord, y_coord)
            if click_coords in temp_location[1]:
                selection = temp_location[1].index(click_coords)
            button_function(mouse, width/1.2, height/1.1, "quit")
            button_function(mouse, width/1.2, height/1.2, "place")

     
    mouse = pygame.mouse.get_pos() 
    #Quit Button: Hovering over & Non-Hovering -----------------------------------------
    draw_button(mouse, quit, color_dark, color_light, width/1.2, height/1.1)
    draw_button(mouse, place, color_dark, color_light, width/1.2, height/1.2)
    #------------------------------------------------------------------------------------
    draw_board()
    draw_pieces()
    pygame.display.flip()
pygame.quit()