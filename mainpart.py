from graphics import *
from inputsmth import InputDialog
from shotsmth import ShotTracker


def main():
    # animation window
    win = GraphWin("Projectile Animation", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)

    # draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)

    # draw labeled ticks every 50meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    # event loop each time fires new shot
    angle, vel, height = 45.0, 40.0, 2.0
    while True:
        # interact with users
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Quit":
            break  # exit
        # short track until hits ground or leaves window
        angle, wel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1 / 50)
            update(50)

    win.close()


main()
