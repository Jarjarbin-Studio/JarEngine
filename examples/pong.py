import sources as JarEngine

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
        title="JarEngine - Pong",
        flags=0,
        depth=0,
        display=0,
        vsync=0
    )
)

WIDTH = 800
HEIGHT = 600

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
# SCORE
# --------------------
score_left = 0
score_right = 0

# --------------------
# CENTER SCORE TEXT
# --------------------
score_text = JarEngine.Entities.JEEntity(name="score_text")
game.entities.add(score_text)

JarEngine.Entities.Transforms.JEPositionComponent(score_text, (WIDTH // 2, 20))
JarEngine.Entities.Graphics.JELayerComponent(score_text, 100)

JarEngine.Entities.Graphics.JETextComponent(score_text, "0 : 0")
JarEngine.Entities.Graphics.JEFontComponent(score_text, font)

# --------------------
# FPS TEXT
# --------------------
fps_text = JarEngine.Entities.JEEntity(name="fps_text")
game.entities.add(fps_text)

JarEngine.Entities.Transforms.JEPositionComponent(fps_text, (10, 10))
JarEngine.Entities.Graphics.JELayerComponent(fps_text, 100)

JarEngine.Entities.Graphics.JETextComponent(fps_text, "FPS: 0")
JarEngine.Entities.Graphics.JEFontComponent(fps_text, font)

# --------------------
# CONFIG
# --------------------
PADDLE_SPEED = 400

BALL_BASE_SPEED = 300
BALL_MAX_SPEED = 900
BALL_ACCELERATION = 20
ball_speed_multiplier = 1.0

# --------------------
# PADDLES
# --------------------
left_paddle = JarEngine.Entities.JEEntity(name="left_paddle")
game.entities.add(left_paddle)

JarEngine.Entities.Transforms.JEPositionComponent(left_paddle, (30, 250))
JarEngine.Entities.Transforms.JEVelocityComponent(left_paddle, (0, 0))
JarEngine.Entities.Transforms.JESizeComponent(left_paddle, (15, 100))
JarEngine.Entities.Graphics.JEColorComponent(left_paddle, (255, 255, 255, 255))
JarEngine.Entities.Graphics.JELayerComponent(left_paddle, 10)

right_paddle = JarEngine.Entities.JEEntity(name="right_paddle")
game.entities.add(right_paddle)

JarEngine.Entities.Transforms.JEPositionComponent(right_paddle, (755, 250))
JarEngine.Entities.Transforms.JEVelocityComponent(right_paddle, (0, 0))
JarEngine.Entities.Transforms.JESizeComponent(right_paddle, (15, 100))
JarEngine.Entities.Graphics.JEColorComponent(right_paddle, (255, 255, 255, 255))
JarEngine.Entities.Graphics.JELayerComponent(right_paddle, 10)

# --------------------
# BALL
# --------------------
ball = JarEngine.Entities.JEEntity(name="ball")
game.entities.add(ball)

JarEngine.Entities.Transforms.JEPositionComponent(ball, (400, 300))
JarEngine.Entities.Transforms.JEVelocityComponent(ball, (BALL_BASE_SPEED, BALL_BASE_SPEED))
JarEngine.Entities.Transforms.JESizeComponent(ball, (15, 15))
JarEngine.Entities.Graphics.JEColorComponent(ball, (255, 255, 255, 255))
JarEngine.Entities.Graphics.JELayerComponent(ball, 20)

# --------------------
# RESET BALL
# --------------------
def reset_ball(direction=1):
    global ball_speed_multiplier

    ball_speed_multiplier = 1.0

    ball.set_position((400, 300))
    ball.set_velocity((BALL_BASE_SPEED * direction, BALL_BASE_SPEED * 0.6))

# --------------------
# INPUT
# --------------------
def handle_input():
    left_vy = 0
    right_vy = 0

    if game.is_key_down(JarEngine.JEKey_Z):
        left_vy -= PADDLE_SPEED
    if game.is_key_down(JarEngine.JEKey_S):
        left_vy += PADDLE_SPEED

    if game.is_key_down(JarEngine.JEKey_Up):
        right_vy -= PADDLE_SPEED
    if game.is_key_down(JarEngine.JEKey_Down):
        right_vy += PADDLE_SPEED

    left_paddle.set_velocity((0, left_vy))
    right_paddle.set_velocity((0, right_vy))

# --------------------
# COLLISIONS
# --------------------
def clamp_paddle(paddle):
    pos = paddle.get_position()

    if pos.y < 0:
        paddle.set_position((pos.x, 0))
    elif pos.y > HEIGHT - 100:
        paddle.set_position((pos.x, HEIGHT - 100))

def check_ball_collision():
    global score_left, score_right

    b = ball.get_position()
    bv = ball.get_velocity()

    lp = left_paddle.get_position()
    rp = right_paddle.get_position()

    if b.y <= 0 or b.y >= HEIGHT:
        ball.set_velocity((bv.x, -bv.y))

    if lp.x < b.x < lp.x + 15 and lp.y < b.y < lp.y + 100:
        ball.set_velocity((abs(bv.x), bv.y))

    if rp.x < b.x < rp.x + 15 and rp.y < b.y < rp.y + 100:
        ball.set_velocity((-abs(bv.x), bv.y))

    if b.x < 0:
        score_right += 1
        reset_ball(direction=1)

    if b.x > WIDTH:
        score_left += 1
        reset_ball(direction=-1)

# --------------------
# BALL ACCELERATION
# --------------------
ball_timer = 0.0
BALL_ACCEL_PER_SEC = 0.05

def update_ball_speed():
    global ball_speed_multiplier, ball_timer

    ball_timer += game.dt

    if ball_timer < 1.0:
        return

    ball_timer = 0.0

    ball_speed_multiplier += BALL_ACCEL_PER_SEC

    max_multiplier = BALL_MAX_SPEED / BALL_BASE_SPEED
    if ball_speed_multiplier > max_multiplier:
        ball_speed_multiplier = max_multiplier

    v = ball.get_velocity()
    length = (v.x ** 2 + v.y ** 2) ** 0.5

    if length == 0:
        return

    nx = v.x / length
    ny = v.y / length

    speed = BALL_BASE_SPEED * ball_speed_multiplier
    ball.set_velocity((nx * speed, ny * speed))

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

    clamp_paddle(left_paddle)
    clamp_paddle(right_paddle)

    update_ball_speed()

    check_ball_collision()

    score_text.set_text(f"{score_left} : {score_right}")
    fps_text.set_text(f"FPS: {int(game.clock.fps)}")

    game.wdw.fill((0, 0, 0))

    game.update()
    game.display()

# --------------------
# SHUTDOWN
# --------------------
JarEngine.Quit()
