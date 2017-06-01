'''
   Demonstrates how to create a mesh from scratch and to set color per vertex data. 
'''
import MaxPlus

def makePyramidMesh(mesh, side = 20.0):
    mesh.SetNumVerts(4)
    mesh.SetNumFaces(4)
    halfside = side / 2.0
    mesh.SetVert(0, MaxPlus.Point3(0.0,  0.0,  side))
    mesh.SetVert(1, MaxPlus.Point3(-halfside, -halfside,  0.0))
    mesh.SetVert(2, MaxPlus.Point3(-halfside, halfside,  0.0)) 
    mesh.SetVert(3, MaxPlus.Point3(halfside,  0.0,  0.0)) 
    mesh.GetFace(0).SetVerts(0, 1, 2)
    mesh.GetFace(0).SetEdgeVisFlags(1,1,0)
    mesh.GetFace(1).SetVerts(0, 2, 3)
    mesh.GetFace(1).SetEdgeVisFlags(1,1,0)
    mesh.GetFace(2).SetVerts(0, 3, 1)
    mesh.GetFace(2).SetEdgeVisFlags(1,1,0)
    mesh.GetFace(3).SetVerts(1, 2, 3)
    mesh.GetFace(3).SetEdgeVisFlags(1,1,0)
    mesh.InvalidateGeomCache()
    mesh.InvalidateTopologyCache()

def outputChannel(mc, name):
    MaxPlus.Core.WriteLine("Channel " + name)
    if not mc.Enabled:
        MaxPlus.Core.WriteLine("Not enabled");
        return

    MaxPlus.Core.WriteLine("Number of texture vertices %d" % mc.NumTextureVertices)
    for tv in mc.TextureVertices:
        MaxPlus.Core.WriteLine("Texture vertex %f, %f, %f" % (tv.X, tv.Y, tv.Z))

    MaxPlus.Core.WriteLine("Number of faces %d" % mc.NumFaces)
    for tf in mc.TextureFaces:
        MaxPlus.Core.WriteLine("Texture vertex indices %d, %d, %d" % (tf.A, tf.B, tf.C));

def outputChannels(mesh):
    outputChannel(mesh.DefaultMap, "default")
    outputChannel(mesh.AlphaMap, "alpha")
    outputChannel(mesh.ColorPerVertexMap, "color per vertex")
    outputChannel(mesh.ShadingMap, "shading")

def main():
    geom = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.TriMeshGeometry)
    tri = MaxPlus.TriObject._CastFrom(geom)
    mesh = tri.GetMesh()
    makePyramidMesh(mesh)
    node = MaxPlus.Factory.CreateNode(tri)
    outputChannels(mesh)
    MaxPlus.Core.WriteLine("Updating the color per vertex channel")
    mesh.ColorPerVertexMap.SetNumTextureVertices(2)
    mesh.ColorPerVertexMap.SetTextureVertex(0, MaxPlus.Point3(1, 0, 0))
    mesh.ColorPerVertexMap.SetTextureVertex(1, MaxPlus.Point3(0, 0, 1))
    mesh.ColorPerVertexMap.SetTextureFace(0, 0, 1, 1)
    mesh.ColorPerVertexMap.SetTextureFace(1, 0, 1, 1)
    mesh.ColorPerVertexMap.SetTextureFace(2, 0, 1, 1)
    mesh.ColorPerVertexMap.SetTextureFace(3, 1, 1, 1)
    outputChannels(mesh)
    node.VertexColorMode = True
    
if __name__ == "__main__":
    main()
