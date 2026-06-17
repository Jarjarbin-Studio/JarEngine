import sources as JarEngine

pg = JarEngine.Systems.JEInternPyGame

JarEngine.init()

game = JarEngine.Games.JEGame()
game.set_window(JarEngine.Games.JEWindow())

s = JarEngine.Systems.JEInternClasses.JEInternClassGraphicalObject("my object")
game.window.ressource.font.add(s)

print(game.dump())

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("JarEngine - Minimal Window")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pg.display.flip()

JarEngine.quit()
