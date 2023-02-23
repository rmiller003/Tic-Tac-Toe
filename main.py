# This is a Graphical Tic-Tac-Toe game generated by ChatGPT.

import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_SIZE = (300, 300)
WINDOW_TITLE = "Tic Tac Toe"
WINDOW_BACKGROUND_COLOR = (255, 255, 255)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

# Set up the game board
BOARD_SIZE = 3
BOARD_LINE_COLOR = (0, 0, 0)
BOARD_LINE_WIDTH = 2
BOARD_CELL_SIZE = WINDOW_SIZE[0] // BOARD_SIZE
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Set up the players
PLAYERS = ['X', 'O']
current_player = 0

# Set up the font
FONT_SIZE = 50
font = pygame.font.Font(None, FONT_SIZE)

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the row and column of the cell that was clicked
            row = event.pos[1] // BOARD_CELL_SIZE
            col = event.pos[0] // BOARD_CELL_SIZE
            if board[row][col] == ' ':
                # Mark the cell with the current player's symbol
                board[row][col] = PLAYERS[current_player]
                current_player = (current_player + 1) % 2

    # Draw the board
    window.fill(WINDOW_BACKGROUND_COLOR)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # Draw the cell
            cell_rect = pygame.Rect(j * BOARD_CELL_SIZE, i * BOARD_CELL_SIZE, BOARD_CELL_SIZE, BOARD_CELL_SIZE)
            pygame.draw.rect(window, BOARD_LINE_COLOR, cell_rect, BOARD_LINE_WIDTH)
            # Draw the symbol in the cell if there is one
            if board[i][j] != ' ':
                symbol = font.render(board[i][j], True, BOARD_LINE_COLOR)
                symbol_rect = symbol.get_rect(center=cell_rect.center)
                window.blit(symbol, symbol_rect)

    # Check for a win
    winner = None
    for i in range(BOARD_SIZE):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]
    if winner:
        # Display the winner
        winner_text = font.render(f"{winner} wins!", True, BOARD_LINE_COLOR)
        winner_rect = winner_text.get_rect(center=window.get_rect().center)
        window.blit(winner_text, winner_rect)
        # Disable the game
        game_running = False

    # Update the display
    pygame.display.update()

# Clean up Pygame
pygame.quit()