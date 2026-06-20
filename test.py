import sources as JarEngine

JarEngine.init()

game = JarEngine.JEGame()
game.set_window(JarEngine.JEWindow(size=(800, 600), title="JarEngine - Minimal Window"))

s = JarEngine.Interns.JEInternClasses.JEInternGraphicalObject("my object")
game.wdw.ressource.font.add(s)

def show_evt(je_game, evt):
    print(f"event triggered: {evt.dump()}")
    pass

def handle_exit(je_game, evt):
    je_game.close()

exit_watcher = JarEngine.JEEvent.JEEventWatcher(JarEngine.JEEvent.JEEvtQuit, handle_exit)
game.event.add(exit_watcher)

key_watcher = JarEngine.JEKeyboard.JEKeyWatcher(JarEngine.JEKeyboard.JEKey_Escape, show_evt)
game.event.add(key_watcher)

mouse_watcher = JarEngine.JEMouse.JEMouseWatcher(JarEngine.JEMouse.JEMouse_Left, show_evt)
game.event.add(mouse_watcher)

while game.is_open:
    game.wdw.fill((0, 0, 0))
    game.update()

print(game.dump())

JarEngine.quit()
