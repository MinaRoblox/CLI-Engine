# CLI-Engine, create games easily in the terminal!

```
# Example
import cliEngine # to be done like this soon

game = cliEngine.Game(9, 9) # width and height of game board
player = cliEngine.Player(game, "1", 4, 4) # game class, sprite, pos x and y

player.draw()
game.printBoard()

```
![code example result](example.png)

To import the engine, do this:
copy src/main.py to your current directory
and import with

```
import main as cliEngine
```