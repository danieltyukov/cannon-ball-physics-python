from graphics import *
from shotsmth import ShotTracker
from buttons import Button


class InputDialog:
    # get angle,velocity,height
    def __init__(self, angle, vel, height):
        # display

        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0, 4.5, 4, 0.5)

        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Height").draw(win)
        self.height = Entry(Point(3, 3), 5).draw(win)
        self.height.setText(str(height))

        self.fire = Button(win, Point(1, 4), 1.25, 0.5, "Fire!")
        self.fire.activate()

        self.quit = Button(win, Point(3, 4), 1.25, 0.5, "Quit")
        self.quit.activate()

    def interact(self):
        # Returns which str was returned fire or quit
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    def getValues(self):
        # Return input values
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        h = float(self.height.getText())
        return a, v, h

    def close(self):
        # close input window
        self.win.close()

        """dialog = InputDialog(45, 40, 2)
        choice = dialog.interact()
        if choice == "Fire!":
            angle, vel, height = dialog.getValue()"""

