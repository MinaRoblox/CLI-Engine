import sys
import select
import termios
import tty
import time
import os

def inputReceiver(timeout):
    # Save the original terminal settings
    original_settings = termios.tcgetattr(sys.stdin)
    try:
        # Set the terminal to raw mode to read single characters
        tty.setraw(sys.stdin)

        start_time = time.time()
        while time.time() - start_time < timeout:
            if select.select([sys.stdin], [], [], 0.1)[0]:  # Non-blocking check
                char = sys.stdin.read(1)  # Read exactly one character
                return char
    finally:
        # Restore the original terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)

    return None  # Timeout

def typewriter(text, delay=0.1):
    """
    Prints text with a typewriter effect.

    Parameters:
        text (str): The text to display.
        delay (float): The delay between each character in seconds. Default is 0.1.
    """
    for char in text:
        sys.stdout.write(char)  # Write each character without adding a newline
        sys.stdout.flush()  # Flush the output to display characters immediately
        time.sleep(delay)  # Wait for the specified delay
    print()  # Print a newline at the end

class Game():
    def __init__(self, boardWidth, boardHeight):
        self.width = boardWidth
        self.height = boardHeight
        self.board = [["0" for _ in range(boardWidth)] for _ in range(boardHeight)]

    def printBoard(self):
        for line in self.board:
            print(" ".join(line))

    def drawBorders(self, borders, borderSprite):
        for x, y in borders:
            self.board[y][x] = borderSprite

class Player():
    def __init__(self, gameClass, sprite, posX, posY):
        self.game = gameClass
        self.sprite = sprite
        self.posX = posX
        self.posY = posY
        self.jumpStage = 0

    def draw(self):
        self.game.board[self.posY][self.posX] = self.sprite

    def move(self, dir):
        if (dir == "w" or dir == "W") and self.posY > 0:
            self.game.board[self.posY][self.posX] = "0"
            self.posY -= 1
            self.game.board[self.posY][self.posX] = "1"

        elif (dir == "s" or dir == "S") and self.posY < len(self.game.board) - 1:  # Restrict "s" to bottom boundary
            self.game.board[self.posY][self.posX] = "0"
            self.posY += 1
            self.game.board[self.posY][self.posX] = "1"