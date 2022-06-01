from time import perf_counter
import pygame
import sys
from objects import Object, MoveableObject
import _menu

pygame.init()

WIN = pygame.display.set_mode((1600, 1000), flags=pygame.RESIZABLE)
pygame.display.set_caption("GamingX Framework")
WIDTH, HEIGHT = pygame.display.get_window_size()
FULLSCREEN = True
FULLSCREEN_SIZE = WIDTH, HEIGHT
WINDOW_SIZE = WIDTH * 0.8, HEIGHT * 0.8
SIZE_LINK = True

WHITE = (255, 255, 255)
LIGHT_GREY = (120, 120, 120)
MEDIUM_GREY = (60, 60, 60)
DARK_GREY = (30, 30, 30)
BLACK = (0, 0, 0)


def update_screen_size():
    """Updates objects size and position with new screen size"""
    "Adjust any constants"

    if SIZE_LINK:
        "Adjust objects size"


def update_playing_screen_size(menu: "_menu.Menu"):
    """Updates live objects positions"""

    global WIDTH, HEIGHT

    "Get objects position on screen by ratio e.g. 20% of the screen"

    WIDTH, HEIGHT = pygame.display.get_window_size()
    menu.resize()

    "Set the x and y of objects based on new width and height, with ratios"

    "Clip the coords of any object out of bounds"

    
def draw_window(objects: list[Object]):
    """Draw window"""
    WIN.fill(BLACK)

    for object in objects:
        object.draw(WIN)

    pygame.display.update()


def handle_player_movement(keys_pressed, objects):
    """Adjust player velocity depnding on input. NOTE: Not for changing position"""
    # Example:
    if keys_pressed[pygame.K_UP]:
        "move_up()"


def handle_movement(objects: list[MoveableObject], static_objects: list[Object], delta_time):
    """Handles movement for all objects, adjusts positions based on velocity"""
    
    # Loop until every object has moved for the given time
    dt = delta_time
    while dt:
        # Find two objects closest to collision
        closest_time = dt
        closest_objects = None, None

        # For each object, find it's closest collision to every object
        for object1 in objects:
            for object2 in objects:

                dist_between = min(object2.x - (object1.x + object1.width), (object2.x + object2.width) - object1.x, key=abs) # Closest distance between two objects, adjust for width
                rel_vel = object1.vx - object2.vx # Relative velocity between two objects
                if rel_vel == 0 or dist_between == 0: continue # Two objects will never collide if moving at same velocity
                coll_time = dist_between / rel_vel # Time until the two objects collide

                if coll_time >= 0 and coll_time < closest_time and overlapping_y(object1, object2, coll_time): # Check that two objects will collide and that the time is closer than closest_time
                    closest_time = coll_time
                    closest_objects = object1, object2

        # Check for any closer collisions with immoveable_objects
        for object1 in objects:
            for object2 in static_objects:

                dist_between = min(object2.x - (object1.x + object1.width), (object2.x + object2.width) - object1.x, key=abs) # Closest distance between two objects, adjust for width
                rel_vel = object1.vx # Relative velocity between two objects
                if rel_vel == 0 or dist_between == 0: continue # Two objects will never collide if moving at same velocity and if touching, Moveable_Object will be moving away
                coll_time = dist_between / rel_vel # Time until the two objects collide

                if coll_time >= 0 and coll_time < closest_time: # Check that two objects will collide and that the time is closer than closest_time and that two objects are at overlapping x width
                    closest_time = coll_time
                    closest_objects = object1, object2

        if closest_objects[0]: # If the two objects collided

            # Move closest objects to collision point
            closest_objects[0].x += closest_time * closest_objects[0].vx
            if type(closest_objects[1]) == MoveableObject:
                closest_objects[1].x += closest_time * closest_objects[1].vx

            # Set the two objects velocity to the average of both
            if type(closest_objects[1]) == MoveableObject:
                closest_objects[0].vx, closest_objects[1].vx = closest_objects[1].vx, closest_objects[0].vx # Swap objects velocities, simulating 100% energy transfer
            else:
                closest_objects[0].vx *= -1

            # Move all other objects the same amount that the collision objects moved
            for object in objects:
                if object not in closest_objects:
                    object.x += closest_time * object.vx

            # Subtract closest_time from dt as the game time has advance by closest_time seconds
            dt -= closest_time

        # If no collision
        else:
            # Move objects the rest of the way, then break to move onto the y velocity
            for object in objects:
                object.x += dt * object.vx
            break


    # Do the same thing but with y axis
    dt = delta_time
    while dt:
        # Find two objects closest to collision
        closest_time = dt
        closest_objects = None, None

        # For each object, find it's closest collision to every object
        for object1 in objects:
            for object2 in objects:

                dist_between = min(object2.y - (object1.y + object1.width), (object2.y + object2.width) - object1.y, key=abs) # Closest distance between two objects, adjust for width
                rel_vel = object1.vy - object2.vy # Relative velocity between two objects
                if rel_vel == 0 or dist_between == 0: continue # Two objects will never collide if moving at same velocity
                coll_time = dist_between / rel_vel # Time until the two objects collide

                if coll_time >= 0 and coll_time < closest_time and overlapping_x(object1, object2, coll_time): # Check that two objects will collide and that the time is closer than closest_time and that two objects are at overlapping y height
                    closest_time = coll_time
                    closest_objects = object1, object2

        # Check for any closer collisions with immoveable_objects
        for object1 in objects:
            for object2 in static_objects:

                dist_between = min(object2.y - (object1.y + object1.width), (object2.y + object2.width) - object1.y, key=abs) # Closest distance between two objects, adjust for width
                rel_vel = object1.vy # Relative velocity between two objects
                if rel_vel == 0 or dist_between == 0: continue # Two objects will never collide if moving at same velocity and if touching, Moveable_Object will be moving away
                coll_time = dist_between / rel_vel # Time until the two objects collide

                if coll_time >= 0 and coll_time < closest_time: # Check that two objects will collide and that the time is closer than closest_time
                    closest_time = coll_time
                    closest_objects = object1, object2

        if closest_objects[0]: # If the two objects collided

            # Move closest objects to collision point
            closest_objects[0].y += closest_time * closest_objects[0].vy
            if type(closest_objects[1]) == MoveableObject:
                closest_objects[1].y += closest_time * closest_objects[1].vy

            # Set the two objects velocity to the average of both
            if type(closest_objects[1]) == MoveableObject:
                closest_objects[0].vy, closest_objects[1].vy = closest_objects[1].vy, closest_objects[0].vy # Swap objects velocities, simulating 100% energy transfer
            else:
                closest_objects[0].vy *= -1

            # Move all other objects the same amount that the collision objects moved
            for object in objects:
                if object not in closest_objects:
                    object.y += closest_time * object.vy

            # Subtract closest_time from dt as the game time has advance by closest_time seconds
            dt -= closest_time

        # If no collision
        else:
            # Move objects the rest of the way, then break to move onto the y velocity
            for object in objects:
                object.y += dt * object.vy
            break


def overlapping_y(object1: Object, object2: Object, coll_time: float = 0):
    """Check if two objects are overlapping in the y axis
    \nAdjusts y coords to collision positions"""
    object1.y += coll_time * object1.y
    object2.y += coll_time * object2.y
    return ((object2.y <= object1.y <= object2.y + object2.height) or # top object1 overlaps object2
            (object2.y <= object1.y + object1.height <= object2.y) or # bottom object1 overlaps object 2
            (object1.y <= object2.y <= object1.y + object1.height) or # top object2 overlaps object1
            (object1.y <= object2.y + object2.height <= object1.y)) # bottom object2 overlaps object 1


def overlapping_x(object1: Object, object2: Object, coll_time: float = 0):
    """Check if two objects are overlapping in the x axis
    \nAdjusts x coords to collision positions"""
    object1.x += coll_time * object1.x
    object2.x += coll_time * object2.x
    return ((object2.x <= object1.x <= object2.x + object2.height) or # top object1 overlaps object2
            (object2.x <= object1.x + object1.height <= object2.x) or # bottom object1 overlaps object 2
            (object1.x <= object2.x <= object1.x + object1.height) or # top object2 overlaps object1
            (object1.x <= object2.x + object2.height <= object1.x)) # bottom object2 overlaps object 1


def quit():
    """Stops the program"""
    pygame.quit()
    sys.exit(0)


def main(menu: "_menu.Menu"):
    """Main game loop"""
    delta_time = 0

    objects = []
    static_objects = []
    static_objects.append(Object(0, 0, 1, HEIGHT, None))
    static_objects.append(Object(WIDTH - 1, 0, 1, HEIGHT, None))
    static_objects.append(Object(0, 0, WIDTH, 1, None))
    static_objects.append(Object(0, HEIGHT - 1, WIDTH, 1, None))
    from random import randint
    for _ in range(10):
        while True:
            x, y = randint(0, WIDTH - 100), randint(0, HEIGHT - 100)
            overlapping = False
            for obj in objects:
                if overlapping_x(Object(x, y, 100, 100, None), obj) and overlapping_y(Object(x, y, 100, 100, None), obj):
                    overlapping = True
            if not overlapping:
                break
        objects.append(MoveableObject(x, y, randint(-200, 200), randint(-200, 200), 100, 100, pygame.transform.scale(pygame.image.load("./assets/example.png"), (100, 100))))

    running = True
    paused = False
    while running:
        while not paused:
            time1 = perf_counter()

            keys_pressed = pygame.key.get_pressed()

            handle_player_movement(keys_pressed, objects)
            handle_movement(objects, static_objects, delta_time)
            for object1 in objects:
                for object2 in objects:
                    if object1 != object2 and overlapping_x(object1, object2) and overlapping_y(object1, object2):
                        print("ERROR")
                        paused = True
                        menu.pause()

            draw_window(objects)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                elif event.type == pygame.VIDEORESIZE:
                    update_playing_screen_size(menu)

                elif event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE:
                    paused = True
                    menu.pause()

            time2 = perf_counter()
            delta_time = time2 - time1

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.VIDEORESIZE:
                update_playing_screen_size(menu)
                draw_window(objects)
                menu.pause()

            elif event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_ESCAPE:
                paused = False

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