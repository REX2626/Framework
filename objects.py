import pygame
import os
import sys

"""STARTING COLLISION

overlapping-y:  375.43811100650146 273.28705106051075
OVERLAPPING Y:  False 372.7041640523821 271.2969699287787
overlapping-y:  375.43811100650146 273.28705106051075

overlapping-y:  273.28705106051075 375.43811100650146
OVERLAPPING Y:  False 271.2969699287787 372.7041640523821
overlapping-y:  273.28705106051075 375.43811100650146

overlapping-y:  371.7963592542801 272.5312659261981

ERROR
642.0907128599937 742.0574412852288 371.7963592542801 272.5312659261981
vy = -114 155

ERROR
742.0574412852288 642.0907128599937 272.5312659261981 371.7963592542801
vy = 155 -114
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