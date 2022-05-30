from time import perf_counter
from objects import Ball, Padel, Powerup, PowerupEffect, BallPowerupEffect, PaddlePowerupEffect, GameEventType, pygame, random
import _menu
import sys

pygame.init()

WIN = pygame.display.set_mode(flags=pygame.FULLSCREEN+pygame.RESIZABLE)
pygame.display.set_caption("GamingX Pong")
WIDTH, HEIGHT = pygame.display.get_window_size()
FULLSCREEN = True
FULLSCREEN_SIZE = WIDTH, HEIGHT
WINDOW_SIZE = WIDTH * 0.8, HEIGHT * 0.8
SIZE_LINK = True

SPEED = 230
variable_speed = SPEED
last_collided = None

WHITE = (255, 255, 255)
LIGHT_GREY = (120, 120, 120)
MEDIUM_GREY = (60, 60, 60)
DARK_GREY = (30, 30, 30)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PADEL_WIDTH, PADEL_HEIGHT = 13, 55
PADEL_INDENT = 10
PADEL_SIDE_INDENT = 80

BALL_WIDTH, BALL_HEIGHT = 8, 8

def update_screen_size():
    global RED_PADEL_X, YELLOW_PADEL_X, PADEL_Y, DASHED_WIDTH, DASHED_X, DASHED_LENGTH, SCORE_FONT, TEXT_BAR_HEIGHT, BALL_WIDTH, BALL_HEIGHT, PADEL_WIDTH, PADEL_HEIGHT, SPEED, variable_speed
    SCORE_FONT = pygame.font.SysFont("comicsans", round(WIDTH / 45))
    TEXT_BAR_HEIGHT = SCORE_FONT.get_height()
    RED_PADEL_X = PADEL_SIDE_INDENT
    YELLOW_PADEL_X = WIDTH - PADEL_SIDE_INDENT - PADEL_WIDTH
    PADEL_Y = TEXT_BAR_HEIGHT + (HEIGHT - TEXT_BAR_HEIGHT) / 2 - PADEL_HEIGHT / 2
    DASHED_WIDTH = WIDTH / 225
    DASHED_X = round(WIDTH / 2 - DASHED_WIDTH / 2)
    DASHED_LENGTH = (HEIGHT - TEXT_BAR_HEIGHT - 2 * PADEL_INDENT) / 9

    if SIZE_LINK:
        BALL_WIDTH = BALL_HEIGHT = round(WIDTH / 112.5)
        PADEL_WIDTH = round(WIDTH / (900 / 13))
        PADEL_HEIGHT = round(HEIGHT / (500 / 55))
        SPEED = round(WIDTH / (900 / 230))
        variable_speed = SPEED


def update_playing_screen_size(menu: "_menu.Menu"):
    global WIDTH, HEIGHT
    #ratios'

    WIDTH, HEIGHT = pygame.display.get_window_size()
    menu.resize()
    # set x and y

    # clipping

    
def draw_window():
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, DARK_GREY, (0, 0, WIDTH, TEXT_BAR_HEIGHT)) # the background for the text bar at the top)

    pygame.display.update()


def handle_player_movement(keys_pressed, red: Padel, _, speed):
    red.moving_up = False
    red.moving_down = False
    if keys_pressed[pygame.K_w] and red.get_y() - speed > TEXT_BAR_HEIGHT + PADEL_INDENT:  # UP
        red.y -= speed
        red.moving_up = True
    if keys_pressed[pygame.K_s] and red.get_y() + speed + red.get_height() < HEIGHT - PADEL_INDENT:  # DOWN
        red.y += speed
        red.moving_down = True
    return red


def handle_movement(entities, speed, dt: "float"):
    
    for entity in entities:
        entity.update(dt, speed)


def quit():
    pygame.quit()
    sys.exit(0)


def main(menu: "_menu.Menu"):
    delta_time = 0

    example_object = Padel(RED_PADEL_X, PADEL_Y, PADEL_WIDTH, PADEL_HEIGHT)

    running = True
    not_paused = True
    while running:
        while not_paused:
            time1 = perf_counter()
            speed = variable_speed * delta_time

            keys_pressed = pygame.key.get_pressed()

            handle_movement([example_object], speed, delta_time)

            draw_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.VIDEORESIZE:
                    update_playing_screen_size(menu)

                elif event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE:
                    not_paused = False
                    menu.pause()

            time2 = perf_counter()
            delta_time = time2 - time1

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.VIDEORESIZE:
                update_playing_screen_size(menu)
                draw_window()
                menu.pause()

            elif event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE:
                not_paused = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                menu.mouse_click(mouse)


def main_menu():
    menu = _menu.Menu()
    menu.resize()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.VIDEORESIZE:
                menu.resize()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                menu.mouse_click(mouse)


if __name__ == "__main__":
    main_menu()