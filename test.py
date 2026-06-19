import sources as JarEngine

JarEngine.init()

game = JarEngine.JEGame()
game.set_window(JarEngine.JEWindow(size=(800, 600), title="JarEngine - Minimal Window"))

s = JarEngine.Interns.JEInternClasses.JEInternGraphicalObject("my object")
game.wdw.ressource.font.add(s)

def show_evt(je_game, evt):
    print(f"event triggered: {evt.dump()}")

def handle_exit(je_game, evt):
    je_game.close()

events: list[JarEngine.JEEvent.JEEventCode] = [getattr(JarEngine.JEEvent, evt) for evt in JarEngine.JEEvent.__dict__ if isinstance(getattr(JarEngine.JEEvent, evt), JarEngine.JEEvent.JEEventCode)]

exit_watcher = JarEngine.JEEvent.JEEventWatcher(JarEngine.JEEvent.JEEvtQuit, handle_exit)
game.event.add(exit_watcher)

event_watcher = JarEngine.JEEvent.JEEventWatcher(events, show_evt)
game.event.add(event_watcher)

while game.is_open:
    game.wdw.fill((0, 0, 0))
    game.update()

JarEngine.quit()
