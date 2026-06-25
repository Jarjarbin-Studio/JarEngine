import sources as JarEngine

# ----------
# JarEngine initialization
# ----------
JarEngine.Init()

# ----------
# Game & Window creation
# ----------
game = JarEngine.Games.JEGame()
game.set_window(JarEngine.Games.JEWindow(size=(800, 600), fps=100, title="JarEngine - Minimal Window"))

# ----------
# Texture creation & registration
# ----------
texture = JarEngine.Graphics.JETexture("JarEngineLogo.png")
game.ressource.texture.add(texture)

# ----------
# System-Addon registration
# ----------
JarEngine.Games.Systems.JERenderSystem(game)

# ----------
# Event registration
# ----------
game.event.add(JarEngine.Events.Event.JEEventWatcher(
    JarEngine.JEEvtQuit,
    lambda je_game, evt: je_game.close()
))
game.event.add(JarEngine.Events.EventKeyboard.JEKeyWatcher(
    JarEngine.JEKey_Escape | JarEngine.JEKey_Delete,
    lambda je_game, evt: je_game.close()
))

# ----------
# Sprite creation & registration
# ----------
sprite = JarEngine.Entities.JEEntity(name="sprite")
game.entities.add(sprite)

# ----------
# Sprite Component-Addon registration
# ----------
JarEngine.Entities.Components.JETextureComponent(sprite, game.ressource.texture.get(name="JarEngineLogo.png"))
JarEngine.Entities.Components.JEPositionComponent(sprite, (350, 250))
JarEngine.Entities.Components.JESizeComponent(sprite, (100, 100))

# ----------
# Input handler function
# ----------
def input_handler():
    if game.is_key_down(JarEngine.JEKey_Up):
        sprite.update_position(y=-100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Down):
        sprite.update_position(y=100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Left):
        sprite.update_position(x=-100 * game.dt)
    if game.is_key_down(JarEngine.JEKey_Right):
        sprite.update_position(x=100 * game.dt)

# ----------
# Main loop
# ----------
while game.is_open:
    input_handler()
    game.wdw.fill((0, 0, 0))
    game.update()
    game.display()

# ----------
# Game recursive dump (colored)
# ----------
print(game.dump(is_colored=True))

# ----------
# JarEngine reset
# ----------
JarEngine.Quit()
