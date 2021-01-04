from projectile import Projectile


def getInputs():
    a = float(input("Input the angle in degrees: "))
    v = float(input("Input initial velocity in m/s: "))
    h = float(input("Input the initial hight on meters: "))
    t = float(input("enter the time interval between position calculations: "))
    return a, v, h, t


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance Traveled: {0:0.1f}meters.".format(cball.getX()))


main()
