from src.two import GravityVersion as cliEngine
import os

game = cliEngine.Game(10, 10)
player = cliEngine.Player(game, "1", 3, 3)

while True:
    os.system("clear")
    player.draw()
    game.printBoard()

    moveKey = cliEngine.inputReceiver(0.25)
    if moveKey == None:
        player.move("s")

    elif moveKey == "w":
        player.move(moveKey)

    elif moveKey == "q":
        os.system("clear")
        break

    else:
        pass