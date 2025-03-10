import pygame
import board

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((222, 184, 135))
numbers = ['1']
temp_location = {'1' : (1, 2)}
valid_moves = []


## Give number their image
numberone = pygame.image.load('1number.jpg')
numberone = pygame.transform.scale(numberone, (160, 160))
number_pieces = ['1']

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

def draw_pieces():
    for i in range(len(numbers)):
        index = number_pieces.index(numbers[i])
        if number_pieces[i] == '1':



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 200
            y_coord = event.pos[1] // 200
            click_coords = (x_coord, y_coord)
            if click_coords in temp_location['1']:
                selection = temp_location['1'].index(click_coords)
                
    # Clear the screen
    draw_board()
    draw_pieces()
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()