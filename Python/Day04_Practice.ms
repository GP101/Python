script = "
import math
def CreateSphere(x,y,z, r):
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    obj.ParameterBlock.Radius.Value = r
    node = MaxPlus.Factory.CreateNode(obj)
    node.Position = MaxPlus.Point3( x, y, z )

zpos = 0
r = 1
for z in xrange(10):
	CreateSphere( 0, 0, zpos, r )
	zpos += r * 2
	r += 1
"

python.execute script