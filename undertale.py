from src import cliEngine
import random
import time
import os

def clear():
    os.system("cls" if os.name == 'nt' else "clear")

class Scenes:
    def menu():
        while True:
            clear()
            print("""

Undertale for the Terminal
Version 1.0.0
minaroblox

Input 'start' to begin.
Input 'exit' to quit.

Made in CLI-Engine

            """)

            menuInput = input(">>> ")

            if menuInput == "start":
                break

            elif menuInput == "exit":
                exit()

        Scenes.scene1()

    def scene1():
        clear()
        game = cliEngine.Game(11, 11)
        player = cliEngine.Player(game, "1", 5, 5)

        borderPositions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 9), (0, 8), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (7, 10), (8, 10), (9, 10), (10, 10), (6, 10), (5, 10), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0), (9, 0), (8, 0), (7, 0), (6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (10, 6), (9, 6), (8, 6), (8, 5), (8, 4), (8, 3), (8, 1), (9, 1), (8, 2), (9, 2), (9, 3), (9, 4), (9, 5), (1, 9), (1, 8), (1, 6), (1, 7), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        game.drawBorders(borderPositions, "2")

        class Teleport():
            def __init__(self):
                self.teleporter1 = cliEngine.Specials(game, "3", 10, 9, "teleporter", player)
                self.teleporter2 = cliEngine.Specials(game, "3", 10, 8, "teleporter", player)
                self.teleporter3 = cliEngine.Specials(game, "3", 10, 7, "teleporter", player)
        
            def draw(self):
                self.teleporter1.draw()
                self.teleporter2.draw()
                self.teleporter3.draw()

        teleporter = Teleport()
        
        while True:
            clear()
            player.draw()
            teleporter.draw()
            game.printBoard()
            
            playerInput = cliEngine.getInput()

            if player.detectCollision("3", playerInput):
                break
            
            if player.detectCollision("2", playerInput):
                pass

            else:
                player.move(playerInput)
            
            if playerInput == "q":
                exit()

        Scenes.scene2()

    def scene2():
        clear()
        print("Scene 2!")
        
if __name__ == "__main__":
    Scenes.menu()
