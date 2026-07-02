import jarengine as JarEngine
import random

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
        size=(800, 600),
        fps=60,
        title="JarEngine - Snake Test",
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
# Config
# --------------------
CELL_SIZE = 20
GRID_W = 800 // CELL_SIZE
GRID_H = 600 // CELL_SIZE

direction = (1, 0)
next_direction = (1, 0)

move_timer = 0.0
move_delay = 0.12

WRAP_BORDER = True

# --------------------
# Score
# --------------------
score = 0

# --------------------
# HISTORY (FIXED: 1 entry = 1 cell move)
# --------------------
history = []

# --------------------
# Snake head
# --------------------
snake_head = JarEngine.Entities.JEEntity(name="snake_head")
game.add_entity(snake_head)

JarEngine.Entities.Transforms.JEPositionComponent(snake_head, (400, 300))
JarEngine.Entities.Transforms.JEVelocityComponent(snake_head, (0, 0))
JarEngine.Entities.Transforms.JESizeComponent(snake_head, (CELL_SIZE, CELL_SIZE))
JarEngine.Entities.Graphics.JEColorComponent(snake_head, (0, 255, 0, 255))
JarEngine.Entities.Graphics.JELayerComponent(snake_head, 10)

# --------------------
# Snake body
# --------------------
snake_body = []

def create_segment(pos):
    seg = JarEngine.Entities.JEEntity(name="snake_body")
    game.add_entity(seg)

    JarEngine.Entities.Transforms.JEPositionComponent(seg, pos)
    JarEngine.Entities.Transforms.JESizeComponent(seg, (CELL_SIZE, CELL_SIZE))
    JarEngine.Entities.Graphics.JEColorComponent(seg, (0, 180, 0, 255))
    JarEngine.Entities.Graphics.JELayerComponent(seg, 5)

    snake_body.append(seg)

for _ in range(3):
    create_segment((400, 300))

# --------------------
# Apple
# --------------------
apple = JarEngine.Entities.JEEntity(name="apple")
game.add_entity(apple)

JarEngine.Entities.Transforms.JEPositionComponent(apple, (200, 200))
JarEngine.Entities.Transforms.JESizeComponent(apple, (CELL_SIZE, CELL_SIZE))
JarEngine.Entities.Graphics.JEColorComponent(apple, (255, 0, 0, 255))
JarEngine.Entities.Graphics.JELayerComponent(apple, 1)

def spawn_apple():
    x = random.randint(0, GRID_W - 1) * CELL_SIZE
    y = random.randint(0, GRID_H - 1) * CELL_SIZE
    apple.set_position((x, y))

spawn_apple()

# --------------------
# TEXT (Score + FPS)
# --------------------
score_text = JarEngine.Entities.JEEntity(name="score_text")
game.add_entity(score_text)

JarEngine.Entities.Transforms.JEPositionComponent(score_text, (10, 10))
JarEngine.Entities.Graphics.JELayerComponent(score_text, 100)

JarEngine.Entities.Graphics.JETextComponent(score_text, "Score: 0")
JarEngine.Entities.Graphics.JEFontComponent(score_text, font)


fps_text = JarEngine.Entities.JEEntity(name="fps_text")
game.add_entity(fps_text)

JarEngine.Entities.Transforms.JEPositionComponent(fps_text, (10, 40))
JarEngine.Entities.Graphics.JELayerComponent(fps_text, 100)

JarEngine.Entities.Graphics.JETextComponent(fps_text, "FPS: 0")
JarEngine.Entities.Graphics.JEFontComponent(fps_text, font)

# --------------------
# Helpers
# --------------------
def is_opposite(a, b):
    return a[0] == -b[0] and a[1] == -b[1]


def handle_border(x, y):
    if WRAP_BORDER:
        if x < 0:
            x = (GRID_W - 1) * CELL_SIZE
        elif x >= 800:
            x = 0

        if y < 0:
            y = (GRID_H - 1) * CELL_SIZE
        elif y >= 600:
            y = 0
    else:
        if x < 0 or x >= 800 or y < 0 or y >= 600:
            game.close()

    return x, y


def check_collision():
    h = snake_head.get_position()
    a = apple.get_position()
    return h.x == a.x and h.y == a.y

# --------------------
# Input
# --------------------
def handle_input():
    global next_direction

    if game.is_key_down(JarEngine.JEKey_Up):
        next_direction = (0, -1)
    elif game.is_key_down(JarEngine.JEKey_Down):
        next_direction = (0, 1)
    elif game.is_key_down(JarEngine.JEKey_Left):
        next_direction = (-1, 0)
    elif game.is_key_down(JarEngine.JEKey_Right):
        next_direction = (1, 0)

# --------------------
# Snake update
# --------------------
def update_snake():
    global move_timer, direction, history, score

    move_timer += game.dt
    if move_timer < move_delay:
        return

    move_timer = 0.0

    if not is_opposite(next_direction, direction):
        direction = next_direction

    head = snake_head.get_position()

    new_pos = (
        head.x + direction[0] * CELL_SIZE,
        head.y + direction[1] * CELL_SIZE
    )

    new_pos = handle_border(new_pos[0], new_pos[1])
    snake_head.set_position(new_pos)

    history.insert(0, new_pos)

    max_len = len(snake_body) + 50
    if len(history) > max_len:
        history = history[:max_len]

    for i, seg in enumerate(snake_body):
        index = i + 1
        if index < len(history):
            seg.set_position(history[index])

    # --------------------
    # Apple collision
    # --------------------
    if check_collision():
        score += 1

        tail_index = len(snake_body)
        if tail_index < len(history):
            create_segment(history[tail_index])
        else:
            create_segment(history[-1])

        spawn_apple()

# --------------------
# Quit events
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
# Main loop
# --------------------
while game.is_open:
    handle_input()
    update_snake()

    score_text.set_text(f"Score: {score}")
    fps_text.set_text(f"FPS: {int(game.clock.fps)}")

    game.wdw.fill((0, 0, 0))

    game.update()
    game.display()

# --------------------
# Shutdown
# --------------------
JarEngine.Quit()
