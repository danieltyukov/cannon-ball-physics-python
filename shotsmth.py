from graphics import *
from projectile import Projectile

# from inputsmth import InputDialog


class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        # displays initial projectile parameters
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """move the shot seconds further in its flight"""
        # update projectile
        self.proj.update(dt)
        # move circle to new location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        # current x coordinate
        return self.proj.getX()

    def getY(self):
        # return currect y coordinate
        return self.proj.getY()

    def undraw(self):
        # undraw the shot
        self.marker.undraw()

