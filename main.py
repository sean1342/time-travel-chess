import pygame
from valid_moves import is_valid_move

pygame.init()

SIZE = (640, 640)

screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Chess Board')

square_size = 80

white_move = True

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

    def get_square(self, pos):
        x, y = pos
        x -= self.pos[0]
        y -= self.pos[1]
        col = x // (square_size * self.size)
        row = y // (square_size * self.size)
        return (row, col)

valid_moves = []

def draw(boards):
    for l in boards:
        for board in l:
            board.draw()
    for (b, valid_move) in valid_moves:
        pygame.draw.circle(screen, (0,255,7), (valid_move[0] * square_size * b.size + b.pos[0] + square_size / 2 * b.size, valid_move[1] * square_size * b.size + b.pos[1] + square_size / 2 * b.size), 10 * b.size)
    pygame.display.update()

board1 = Board(0.3, (20, 20))
board2 = Board(0.3, (220, 20))
board3 = Board(0.3, (420, 20))
board4 = Board(0.3, (20, 220))
board5 = Board(0.3, (220, 220))
board6 = Board(0.3, (420, 220))
board7 = Board(0.3, (20, 420))
board8 = Board(0.3, (220, 420))
board9 = Board(0.3, (420, 420))

boards = [[board1, board2, board3],
          [board4, board5, board6],
          [board7, board8, board9]]

draw(boards)

clicking = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down_pos = pygame.mouse.get_pos()
            s_board = None
            for l in boards:
                for board in l:
                    if mouse_down_pos[0] > board.pos[0] and mouse_down_pos[0] < board.pos[0] + square_size * 8 * board.size and \
                       mouse_down_pos[1] > board.pos[1] and mouse_down_pos[1] < board.pos[1] + square_size * 8 * board.size:
                        s_board = board

            if not s_board:
                clicking = True
                break

            start_pos = s_board.get_square(mouse_down_pos)
            for l in boards:
                for board in l:
                    for i in range(8):
                        for j in range(8):
                            if is_valid_move(boards, white_move, s_board, board, start_pos, (i, j)):
                                valid_moves.append((board, (j, i)))

        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = False
            valid_moves = []
            draw(boards)
            mouse_up_pos = pygame.mouse.get_pos()

            e_board = None
            for l in boards:
                for board in l:
                    if mouse_up_pos[0] > board.pos[0] and mouse_up_pos[0] < board.pos[0] + square_size * 8 * board.size and \
                       mouse_up_pos[1] > board.pos[1] and mouse_up_pos[1] < board.pos[1] + square_size * 8 * board.size:
                        e_board = board

            if not e_board or not s_board:
                break

            mouse_up_pos = pygame.mouse.get_pos()
            start_pos = s_board.get_square(mouse_down_pos)
            end_pos = e_board.get_square(mouse_up_pos)

            if is_valid_move(boards, white_move, s_board, e_board, start_pos, end_pos):
                x = round(start_pos[0], 0)
                y = round(start_pos[1], 0)
                p = s_board.board_state[int(start_pos[0])][(int(start_pos[1]))]
                s_board.board_state[int(start_pos[0])][(int(start_pos[1]))] = "."
                x = round(end_pos[0], 0)
                y = round(end_pos[1], 0)
                e_board.board_state[int(end_pos[0])][int(end_pos[1])] = p
                white_move = not white_move

            s_board = None
            e_board = None

        if clicking:
            # code for moving board positions based off mouse input
            pass

        draw(boards)