import sources as JarEngine

JarEngine.Init()

game: JarEngine.JEGame
sprite: JarEngine.JEEntity

def init_game():
    global game
    game = JarEngine.JEGame()
    game.set_window(JarEngine.JEWindow(size=(800, 600), fps=100, title="JarEngine - Minimal Window"))

    texture = JarEngine.JETexture("JarEngineLogo.png")
    game.ressource.texture.add(texture)

    JarEngine.Systems.JERenderSystem(game)

def init_events():
    def ext(je_game, evt):
        je_game.close()

    game.event.add(JarEngine.Event.JEEventWatcher(
        JarEngine.JEEvtQuit,
        ext
    ))
    game.event.add(JarEngine.EventKeyboard.JEKeyWatcher(
        JarEngine.JEKey_Escape | JarEngine.JEKey_Delete,
        ext
    ))

def init_sprite():
    global sprite
    sprite = JarEngine.JEEntity(name="sprite")

    JarEngine.Components.JETextureComponent(sprite, game.ressource.texture.get(name="JarEngineLogo.png"))
    JarEngine.Components.JEPositionComponent(sprite, (350, 250))
    JarEngine.Components.JESizeComponent(sprite, (100, 100))

    game.entities.add(sprite)

def move():
    if game.is_key_down(JarEngine.JEKey_Up):
        sprite.modify_position(y=-100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Down):
        sprite.modify_position(y=100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Left):
        sprite.modify_position(x=-100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Right):
        sprite.modify_position(x=100 * game.dt)

init_game()
init_events()
init_sprite()

while game.is_open:
    move()
    game.wdw.fill((0, 0, 0))
    game.update()
    game.display()

print(game.dump(is_colored=True))

JarEngine.Quit()
