import sources as JarEngine

pg = JarEngine.Systems.JEIntern_PyGame

JE = JarEngine.Engine.JE_Game()

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("JarEngine - Minimal Window")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pg.display.flip()

pg.quit()
