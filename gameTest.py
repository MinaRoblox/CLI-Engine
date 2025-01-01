from src import main as g
import os
import random

os.system("clear")
game = g.Game(9, 9)

class Levels:
    def __init__(self, level):
        self.level = level

    def level1(self):
        player = g.Player(game, "1", 4, 7)

        dialoguer = g.Specials(game, "3", 2, 2, "dialogue", player)
        teleporter = g.Specials(game, "4", 7, 1, "teleporter", player)

        bordersPositions = [(2, 2), (3, 6), (3, 7), (5, 6), (5, 7), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (2, 8), (1, 8), (3, 8), (4, 8), (6, 8), (5, 8), (7, 8), (8, 8), (8, 7), (8, 5), (8, 6), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (6, 0), (5, 0), (7, 0), (4, 0), (3, 0), (2, 0), (1, 0), (6, 1), (6, 2), (6, 3), (1, 3), (2, 3), (3, 3)]
        game.drawBorders(bordersPositions, "2")

        def movement(key):
            player.draw()
            player.move(key)

        player.draw()

        dialogueActivatorSpecial1 = False
        teleportActivatorSpecial2 = False

        while True:
            os.system("clear")
            if dialogueActivatorSpecial1:
                dialoguer.sprite = dialoguer.changeSprite()
            else:
                dialoguer.sprite = "3"

            if teleportActivatorSpecial2:
                teleporter.sprite = teleporter.changeSprite()
            else:
                teleporter.sprite = "4"

            dialoguer.draw()
            teleporter.draw()
            game.printBoard()

            if dialogueActivatorSpecial1:
                dialoguer.dialogue("Hello, please enjoy your stay!")
                dialogueActivatorSpecial1 = False

            elif teleportActivatorSpecial2:
                leveerr = Levels(123)
                dialoguer.teleport(leveerr.level2())

            moveKey = g.getInput()

            if moveKey == "q":
                break

            if player.detectCollision("2", moveKey):
                pass

            else:
                dialogueActivatorSpecial1 = player.detectCollision("3", moveKey)
                teleportActivatorSpecial2 = player.detectCollision("4", moveKey)

                movement(moveKey)

    def level2(self):
        os.system("clear")
        print("Hello World!")
        exit()

level = Levels(random.randint(1, 100000))
level.level1()