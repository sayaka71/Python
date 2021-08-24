# classの継承
import pygame
class MyRect(pygame.Rect):
    def flip(self):
        self.width, self.height = (self.height, self.width)

r = MyRect(10,20,30,40)
print(r.size)
r.flip()
print(r.size)