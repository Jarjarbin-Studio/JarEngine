import sources as JarEngine

JarEngine.init()

game = JarEngine.JEGame()
game.set_window(JarEngine.JEWindow(size=(800, 600), title="JarEngine - Minimal Window"))

s = JarEngine.Interns.JEInternClasses.JEInternGraphicalObject("my object")
game.wdw.ressource.font.add(s)

def handle_exit(je_game, evt):
    print(evt.dump())
    je_game.close()

exit_watcher = JarEngine.JEEvent.JEEventWatcher(JarEngine.JEEvent.JEEvtQuit, handle_exit)
game.event.add(exit_watcher)

while game.is_open:
    game.wdw.fill((0, 0, 0))
    game.update()

print(game.dump())

JarEngine.quit()
