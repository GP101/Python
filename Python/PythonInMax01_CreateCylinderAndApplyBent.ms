script = "
obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)

for p in obj.ParameterBlock.Parameters:
    print p.Name, p.Value


obj.ParameterBlock.Radius.Value = 10.0
obj.ParameterBlock.Height.Value = 30.0
obj.ParameterBlock.HeightSegs.Value = 10

node = MaxPlus.Factory.CreateNode(obj)
mod = MaxPlus.Factory.CreateObjectModifier(MaxPlus.ClassIds.Bend)
mod.ParameterBlock.BendAngle.Value = 45.0
node.AddModifier(mod)
"

python.execute script