import pygame
import chess
import os

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (640, 640)

# Set the size of each square on the chessboard
square_size = window_size[0] // 8

# Set the size of the chess pieces
piece_size = square_size * 0.8

# Set the font for text on the window
font = pygame.font.Font(None, 36)

# Create the Pygame window
screen = pygame.display.set_mode(window_size)

# Load the chess piece images
piece_images = {}
for color in ("b", "w"):
    for piece in ("p", "n", "b", "r", "q", "k"):
        filename = os.path.join("images", f"{color}{piece}.png")
        piece_images[color, piece] = pygame.image.load(filename)

# Create the chess board
board = chess.Board()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Draw the board and pieces
    screen.fill(pygame.Color("white"))
    for rank in range(8):
        for file in range(8):
            square = chess.square(file, rank)
            color = "white" if (rank + file) % 2 == 0 else "dark gray"
            rect = pygame.Rect(file * square_size, rank * square_size, square_size, square_size)
            pygame.draw.rect(screen, pygame.Color(color), rect)
            piece = board.piece_at(square)
            if piece:
                if piece.color:
                    color = "w"
                else:
                    color = "b"
                img = piece_images[color, piece.symbol().lower()]
                img = pygame.transform.scale(img, (int(piece_size), int(piece_size)))
                img_rect = img.get_rect(center=rect.center)
                screen.blit(img, img_rect)
    
    # Display the window
    pygame.display.flip()
