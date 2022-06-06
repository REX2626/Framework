import pygame
import os
import sys

"""STARTING COLLISION

STARTING COLLISION
COLLISION <objects.MoveableObject object at 0x000002399C000D60> 357.2638200520337 458.36448793602244 0.003656703933517484
COLLISION X
357.7574750830585, 457.7574750830585
UPDATED -166 357.7574750830585 457.7574750830585 0.02702689606100038
COLLISION <objects.MoveableObject object at 0x000002399C9415A0> 1113.973421926911 1113.1661129568067 0.001685922546743431
COLLISION Y
UPDATED 122 1114.1791044776137 1113.1492537313393 0.02534097351425695
COLLISION <objects.MoveableObject object at 0x000002399C000D60> 357.47761194029914 0 0.004172684962278316
COLLISION Y
UPDATED -166 356.7849462365609 0 0.021168288551978633
COLLISION <objects.MoveableObject object at 0x000002399C001180> 1005.7849462365593 0 0.005166095993267362
COLLISION Y
UPDATED -73 1005.4078212290508 0 0.01600219255871127
COLLISION <objects.MoveableObject object at 0x000002399C002920> 785.7318435754273 831.2793296089345 0.005586592178760779
COLLISION Y
UPDATED -131 785.0000000000097 831.9999999999947 0.010415600379950492
COLLISION <objects.MoveableObject object at 0x000002399C003130> 1243.0000000000095 1188.9999999999948 0.008498583569421847
COLLISION Y
UPDATED -77 1242.3456090651641 1189.4249291784658 0.0019170168105286448
ERROR
Velocities: object1.vx=118 object2.vx=168
Velocities: object1.vy=99 object2.vy=137
Coordinates: object1.x=46.229040844837115 object2.x=9.749820863829719
Coordinates: object1.y=701.0311444376129 object2.y=601.426937252051
Object1: <objects.MoveableObject object at 0x000002399C001300>, Object2: <objects.MoveableObject object at 0x000002399C002770>
Delta time: 0.030683599994517863
ERROR
Velocities: object1.vx=168 object2.vx=118
Velocities: object1.vy=137 object2.vy=99
Coordinates: object1.x=9.749820863829719 object2.x=46.229040844837115
Coordinates: object1.y=601.426937252051 object2.y=701.0311444376129
Object1: <objects.MoveableObject object at 0x000002399C002770>, Object2: <objects.MoveableObject object at 0x000002399C001300>
Delta time: 0.030683599994517863
"""

#  974.7735831507136
#1,074.7735831507134
#  974.773583150713555205
#1,074.773583150713491041
class Dummy():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

one = Dummy(10, 10)
two = Dummy(20, 20)
print(1)

def get_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class Object():
    def __init__(self, x, y, width, height, image) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def draw(self, win: pygame.Surface):
        win.blit(self.image, (round(self.x), round(self.y)))



class MoveableObject(Object):
    def __init__(self, x, y, vx, vy, width, height, image) -> None:
        super().__init__(x, y, width, height, image)
        self.vx = vx
        self.vy = vy

    def update_posx(self, delta_time):
        self.x += self.vx * delta_time
    
    def update_posy(self, delta_time):
        self.y += self.vy * delta_time