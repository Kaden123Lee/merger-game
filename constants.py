import pygame
pygame.init()

merge_pieces = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Eleven', 'Twelve']
merge_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1)]
valid_moves = []
One = pygame.image.load('numbers/One.png')
One = pygame.transform.scale(One, (200, 200))

Two = pygame.image.load('numbers/Two.png')
Two = pygame.transform.scale(Two, (200, 200))

Three = pygame.image.load('numbers/Three.png')
Three = pygame.transform.scale(Three , (200, 200))

Four = pygame.image.load('numbers/Four.png')
Four = pygame.transform.scale(Four, (200, 200))

Five = pygame.image.load('numbers/Five.png')
Five = pygame.transform.scale(Five, (200, 200))

Six = pygame.image.load('numbers/Six.png')
Six = pygame.transform.scale(Six, (200, 200))

Seven = pygame.image.load('numbers/Seven.png')
Seven = pygame.transform.scale(Seven, (200, 200))

Eight = pygame.image.load('numbers/Eight.png')
Eight = pygame.transform.scale(Eight, (200, 200))

Nine = pygame.image.load('numbers/Nine.png')
Nine = pygame.transform.scale(Nine, (200, 200))

Ten = pygame.image.load('numbers/Ten.png')
Ten = pygame.transform.scale(Ten, (200, 200))

Eleven = pygame.image.load('numbers/Eleven.png')
Eleven = pygame.transform.scale(Eleven, (200, 200))

Twelve = pygame.image.load('numbers/Twelve.png')
Twelve = pygame.transform.scale(Twelve, (200, 200))
