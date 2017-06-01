import math
def CreateSpheresOnCircle(n, radius):
    step = math.pi * 2 / n
    r = 0.0
    for i in xrange(n):
        x = math.cos(r)
        y = math.sin(r)
        x *= radius
        y *= radius
        print x,y
        r += step

CreateSpheresOnCircle(20, 10)