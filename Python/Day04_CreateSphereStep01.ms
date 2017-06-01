script = "
obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
#for p in obj.ParameterBlock.Parameters:
#    print p.Name, p.Value
obj.ParameterBlock.Radius.Value = 1.0
node = MaxPlus.Factory.CreateNode(obj)
node.Position = MaxPlus.Point3( 10, 0, 10 )
"

python.execute script