import pygame
import os
import sys

"""
COLLISION X -168 861.1587511929691 758.3562057974046 0.02643910750532541
756.7169811320745, 856.7169811320745
UPDATED X -62 856.7169811320745 756.7169811320745 0.0005712925175203054

COLLISION Y -19
353.64705882352933, 453.64705882352933

COLLISION Y -159
470.65436241610723, 570.6543624161072

COLLISION Y -100
0.0, 1.0"""

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