import pygame
from valid_moves import is_valid_move

pygame.init()

SIZE = (640, 640)

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Chess Board')

square_size = 80

class Board:
    def __init__(self, size=1, pos=(0, 0)):
        self.board_surface = pygame.Surface((square_size * 8 * size, square_size * 8 * size))
        self.pos = pos
        self.size = size
        self.board_state = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                            ['.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.'],
                            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

        self.piece_images = {}
        self.load_images()

    def load_images(self):
        for color in ['w', 'b']:
            for piece_type in ['p', 'r', 'n', 'b', 'q', 'k']:
                filename = f'images/{color}{piece_type}.png'
                self.piece_images[f'{color}{piece_type}'] = pygame.image.load(filename)

    def draw(self):
        for row in range(8):
            for col in range(8):
                x = col * square_size * self.size
                y = row * square_size * self.size

                if (row + col) % 2 == 0:
                    color = (210, 180, 140)
                else:
                    color = (140, 80, 30)

                pygame.draw.rect(self.board_surface, color, [x, y, square_size * self.size, square_size * self.size])

                piece = self.board_state[row][col]
                if piece != '.':
                    if piece == piece.lower():
                        piece = "b" + piece
                    else:
                        piece = "w" + piece.lower()
                    piece_image = self.piece_images[f'{piece}']
                    piece_image = pygame.transform.scale(piece_image, (square_size * self.size, square_size * self.size))
                    piece_rect = piece_image.get_rect()
                    piece_rect.x = x
                    piece_rect.y = y
                    self.board_surface.blit(piece_image, piece_rect)

        screen.blit(self.board_surface, self.pos)
        pygame.display.update()

    def get_square(self, pos):
        x, y = pos
        x -= self.pos[0]
        y -= self.pos[1]
        col = x // (square_size * self.size)
        row = y // (square_size * self.size)
        return (row, col)

board = Board(1, (0, 0))

mouse_down_pos = None
mouse_up_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down_pos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_up_pos = pygame.mouse.get_pos()
            start_pos = board.get_square(mouse_down_pos)
            end_pos = board.get_square(mouse_up_pos)

            if is_valid_move(board, start_pos, end_pos):
                x = round(start_pos[0], 0)
                y = round(start_pos[1], 0)
                p = board.board_state[int(start_pos[0])][(int(start_pos[1]))]
                board.board_state[int(start_pos[0])][(int(start_pos[1]))] = "."
                x = round(end_pos[0], 0)
                y = round(end_pos[1], 0)
                board.board_state[int(end_pos[0])][int(end_pos[1])] = p

    board.draw()