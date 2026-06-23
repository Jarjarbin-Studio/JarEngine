from random import randint
import sources as JarEngine

JarEngine.Init()

class Game:
    game: JarEngine.JEGame

    @staticmethod
    def init():
        Game.game = JarEngine.JEGame()
        Game.game.set_window(JarEngine.JEWindow(size=(800, 600), title="JarEngine - Minimal Window"))

        Game.game.ressource.texture.add(JarEngine.JETexture("JarEngineLogo.png"))

class Sprites:

    sprite: JarEngine.JESprite
    sprite1: JarEngine.JESprite
    sprite2: JarEngine.JESprite

    @staticmethod
    def init():
        Sprites.sprite = JarEngine.JESprite(Game.game.ressource.texture.get("JarEngineLogo.png"))
        Sprites.sprite.size = (600, 600)
        Sprites.sprite.position = (100, 0)
        Game.game.drawable.sprite.add(Sprites.sprite)

        Sprites.sprite1 = JarEngine.JESprite(Game.game.ressource.texture.get("JarEngineLogo.png"))
        Sprites.sprite1.size = (100, 100)
        Sprites.sprite1.position = (0, 0)
        Game.game.drawable.sprite.add(Sprites.sprite1)

        Sprites.sprite2 = JarEngine.JESprite(Game.game.ressource.texture.get("JarEngineLogo.png"))
        Sprites.sprite2.size = (100, 100)
        Sprites.sprite2.position = (700, 500)
        Game.game.drawable.sprite.add(Sprites.sprite2)

class Events:

    @staticmethod
    def init():
        Game.game.event.add(JarEngine.Event.JEEventWatcher(
            JarEngine.Event.JEEvtQuit,
            Events.exit
        ))
        Game.game.event.add(JarEngine.Keyboard.JEKeyWatcher(
            JarEngine.Keyboard.JEKey_Up |
            JarEngine.Keyboard.JEKey_Down |
            JarEngine.Keyboard.JEKey_Left |
            JarEngine.Keyboard.JEKey_Right,
            Events.move
        ))

    @staticmethod
    def exit(je_game, evt):
        je_game.close()

    @staticmethod
    def move(je_game, evt):
        if evt.key == JarEngine.Keyboard.JEKey_Up:
            Sprites.sprite2.move(0, -1)
        if evt.key == JarEngine.Keyboard.JEKey_Down:
            Sprites.sprite2.move(0, 1)
        if evt.key == JarEngine.Keyboard.JEKey_Left:
            Sprites.sprite2.move(-1, 0)
        if evt.key == JarEngine.Keyboard.JEKey_Right:
            Sprites.sprite2.move(1, 0)

Game.init()
Sprites.init()
Events.init()

while Game.game.is_open:
    Game.game.update()
    Sprites.sprite1.position = (randint(0, 700), randint(0, 500))
    Game.game.wdw.fill((0, 0, 0))
    Game.game.draw()
    Game.game.display()

print(Game.game.dump(is_colored=True))

JarEngine.Quit()
