script = "
import math
def CreateSphere(x,y,z):
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    obj.ParameterBlock.Radius.Value = 1.0
    node = MaxPlus.Factory.CreateNode(obj)
    node.Position = MaxPlus.Point3( x, y, z )

def CreateBox(x,y,z):
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
    obj.ParameterBlock.Width.Value = 1.0
    obj.ParameterBlock.Height.Value = 1.0
    obj.ParameterBlock.Length.Value = 1.0
	for p in obj.ParameterBlock.Parameters:
		print p.Name, p.Value
	
    node = MaxPlus.Factory.CreateNode(obj)
    node.Position = MaxPlus.Point3( x, y, z )

pattern = [
    '1111111',
    '0000000',
    '1111111',
    '1010101'
]
y = 0
for p in pattern:
    x = 0
    step = 2
    for c in p:
		if c == '1':
			CreateSphere( x, y, 0 )
		else:
			CreateBox( x, y, 0 )
		x += step
    y += step
"

python.execute script