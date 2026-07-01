import sources as JarEngine
import random
import math

# --------------------
# Init engine
# --------------------
JarEngine.Init()

# --------------------
# Game setup
# --------------------
game = JarEngine.Games.JEGame(use_clock=True, use_input=True)
game.set_window(
    JarEngine.Games.JEWindow(
        size=(1280, 720),
        fps=120,
        title="JarEngine - ECS Stress Test (Collision Heavy)",
        flags=0,
        depth=0,
        display=0,
        vsync=0
    )
)

# --------------------
# Resources
# --------------------
font = JarEngine.Resources.JEFont("Default", "Nasalization.otf", 20)
game.ressource.font.add(font)

# --------------------
# Systems
# --------------------
JarEngine.Games.Systems.JEMovementSystem(game)
JarEngine.Games.Systems.JEAccelerationSystem(game)
JarEngine.Games.Systems.JERenderSystem(game)

# --------------------
# CONFIG
# --------------------
ENTITY_COUNT = 2000
WIDTH = 1280
HEIGHT = 720

SPEED_MIN = -200
SPEED_MAX = 200

RADIUS = 5
RADIUS_SQ = (RADIUS * 2) ** 2

BOUNCE_BORDER = True

CELL_SIZE = 25
GRID_W = WIDTH // CELL_SIZE + 1
GRID_H = HEIGHT // CELL_SIZE + 1

entities = []

# --------------------
# FPS TEXT
# --------------------
fps_text = JarEngine.Entities.JEEntity(name="fps_text")
game.add_entity(fps_text)

JarEngine.Entities.Transforms.JEPositionComponent(fps_text, (10, 10))
JarEngine.Entities.Graphics.JELayerComponent(fps_text, 100)
JarEngine.Entities.Graphics.JETextComponent(fps_text, "FPS: 0")
JarEngine.Entities.Graphics.JEFontComponent(fps_text, font)

# --------------------
# RANDOM VELOCITY
# --------------------
def random_velocity():
    return (
        random.uniform(SPEED_MIN, SPEED_MAX),
        random.uniform(SPEED_MIN, SPEED_MAX)
    )

# --------------------
# CREATE ENTITIES
# --------------------
for i in range(ENTITY_COUNT):
    e = JarEngine.Entities.JEEntity(name=f"particle_{i}")
    game.add_entity(e)

    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    vx, vy = random_velocity()

    JarEngine.Entities.Transforms.JEPositionComponent(e, (x, y))
    JarEngine.Entities.Transforms.JEVelocityComponent(e, (vx, vy))
    JarEngine.Entities.Transforms.JESizeComponent(e, (5, 5))

    JarEngine.Entities.Graphics.JEColorComponent(
        e,
        (
            random.randint(120, 255),
            random.randint(120, 255),
            random.randint(120, 255),
            255
        )
    )

    JarEngine.Entities.Graphics.JELayerComponent(e, 1)

    entities.append(e)

# --------------------
# BORDER COLLISION
# --------------------
def handle_border(e):
    pos = e.get_position()
    vel = e.get_velocity()

    x, y = pos.x, pos.y
    vx, vy = vel.x, vel.y

    if BOUNCE_BORDER:
        if x < 0 or x > WIDTH:
            vx *= -1
        if y < 0 or y > HEIGHT:
            vy *= -1

        e.set_velocity((vx, vy))

# --------------------
# PARTICLE COLLISION
# --------------------
def handle_collisions():
    grid = {}

    def get_cell(x, y):
        return int(x // CELL_SIZE), int(y // CELL_SIZE)

    for e in entities:
        pos = e.get_position()
        cx, cy = get_cell(pos.x, pos.y)

        key = (cx, cy)
        if key not in grid:
            grid[key] = []
        grid[key].append(e)

    checked = set()

    for (cx, cy), cell_entities in grid.items():

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):

                neighbor_key = (cx + dx, cy + dy)
                if neighbor_key not in grid:
                    continue

                neighbor_entities = grid[neighbor_key]

                for a in cell_entities:
                    pa = a.get_position()
                    va = a.get_velocity()

                    ax, ay = pa.x, pa.y
                    avx, avy = va.x, va.y

                    asize = a.get_size()
                    ar = asize.x * 0.5

                    for b in neighbor_entities:

                        if a is b:
                            continue

                        pair = (id(a), id(b))
                        if pair in checked:
                            continue
                        checked.add(pair)

                        pb = b.get_position()
                        vb = b.get_velocity()

                        bx, by = pb.x, pb.y

                        bsize = b.get_size()
                        br = bsize.x * 0.5

                        dx = ax - bx
                        dy = ay - by

                        min_dist = ar + br
                        dist_sq = dx * dx + dy * dy

                        if dist_sq == 0 or dist_sq > min_dist * min_dist:
                            continue

                        dist = math.sqrt(dist_sq)

                        nx = dx / dist
                        ny = dy / dist

                        overlap = min_dist - dist

                        ax += nx * (overlap * 0.5)
                        ay += ny * (overlap * 0.5)
                        bx -= nx * (overlap * 0.5)
                        by -= ny * (overlap * 0.5)

                        a.set_position((ax, ay))
                        b.set_position((bx, by))

                        a.set_velocity((vb.x, vb.y))
                        b.set_velocity((avx, avy))

# --------------------
# UPDATE
# --------------------
def update():
    for e in entities:
        handle_border(e)

    handle_collisions()

# --------------------
# INPUT
# --------------------
def handle_input():
    if game.is_key_down(JarEngine.JEKey_Escape):
        game.close()

# --------------------
# EVENTS
# --------------------
game.event.add(JarEngine.Events.Event.JEEventWatcher(
    JarEngine.JEEvtQuit,
    lambda g, e: g.close()
))

game.event.add(JarEngine.Events.EventKeyboard.JEKeyWatcher(
    JarEngine.JEKey_Escape | JarEngine.JEKey_Delete,
    lambda g, e: g.close()
))

# --------------------
# MAIN LOOP
# --------------------
while game.is_open:
    handle_input()
    update()

    fps_text.set_text(f"FPS: {int(game.clock.fps)}")

    game.wdw.fill((10, 10, 10))

    game.update()
    game.display()

# --------------------
# SHUTDOWN
# --------------------
JarEngine.Quit()
