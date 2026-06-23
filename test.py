from random import randint
import sources as JarEngine

JarEngine.Init()

def show_evt(je_game, evt):
    print(f"event triggered: {evt.dump()}")

def handle_exit(je_game, evt):
    je_game.close()

game = JarEngine.JEGame()
game.set_window(JarEngine.JEWindow(size=(800, 600), title="JarEngine - Minimal Window"))
game.ressource.texture.add(JarEngine.JETexture("JarEngineLogo.png"))

sprite = JarEngine.JESprite(game.ressource.texture.get("JarEngineLogo.png"))
sprite.size = (600, 600)
sprite.position = (100, 0)
game.drawable.sprite.add(sprite)

sprite1 = JarEngine.JESprite(game.ressource.texture.get("JarEngineLogo.png"))
sprite1.size = (100, 100)
sprite1.position = (0, 0)
game.drawable.sprite.add(sprite1)

sprite2 = JarEngine.JESprite(game.ressource.texture.get("JarEngineLogo.png"))
sprite2.size = (100, 100)
sprite2.position = (700, 500)
game.drawable.sprite.add(sprite2)

exit_watcher = JarEngine.Event.JEEventWatcher(JarEngine.Event.JEEvtQuit, handle_exit)
game.event.add(exit_watcher)

print(game.dump(is_colored=True))

while game.is_open:
    game.update()
    sprite1.position = (randint(0, 700), randint(0, 500))
    sprite2.position = (randint(0, 700), randint(0, 500))
    game.wdw.fill((0, 0, 0))
    game.draw()
    game.display()

JarEngine.Quit()
