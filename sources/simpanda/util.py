from panda3d.core import Geom
from panda3d.core import GeomNode
from panda3d.core import GeomTriangles
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexData
from panda3d.core import GeomVertexWriter
from panda3d.core import LVector3
from panda3d.core import NodePath
from panda3d.core import PandaNode

def _normalize(x: float, y: float, z: float):

    myVec = LVector3(x, y, z)
    myVec.normalize()

    return myVec

def quadGeom(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):

    format = GeomVertexFormat.getV3n3cpt2()
    data = GeomVertexData('quad', format, Geom.UHDynamic)

    vertex = GeomVertexWriter(data, 'vertex')
    normal = GeomVertexWriter(data, 'normal')
    color = GeomVertexWriter(data, 'color')
    texcoord = GeomVertexWriter(data, 'texcoord')

    if x1 != x2:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y1, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y2, z2)

        normal.addData3(_normalize(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(_normalize(2 * x2 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(_normalize(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
        normal.addData3(_normalize(2 * x1 - 1, 2 * y2 - 1, 2 * z2 - 1))

    else:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y2, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y1, z2)

        normal.addData3(_normalize(2 * x1 - 1, 2 * y1 - 1, 2 * z1 - 1))
        normal.addData3(_normalize(2 * x2 - 1, 2 * y2 - 1, 2 * z1 - 1))
        normal.addData3(_normalize(2 * x2 - 1, 2 * y2 - 1, 2 * z2 - 1))
        normal.addData3(_normalize(2 * x1 - 1, 2 * y1 - 1, 2 * z2 - 1))

    color.addData4f(0.5, 0.0, 0.0, 1.0)
    color.addData4f(0.0, 0.5, 0.0, 1.0)
    color.addData4f(0.0, 0.0, 0.5, 1.0)
    color.addData4f(0.5, 0.0, 0.5, 1.0)

    texcoord.addData2f(0.0, 1.0)
    texcoord.addData2f(0.0, 0.0)
    texcoord.addData2f(1.0, 0.0)
    texcoord.addData2f(1.0, 1.0)

    triangles = GeomTriangles(Geom.UHDynamic)
    triangles.addVertices(0, 1, 3)
    triangles.addVertices(1, 2, 3)

    geom = Geom(data)
    geom.addPrimitive(triangles)

    return geom

def cubeGeomNode():

    quadTriangles0 = quadGeom(-1, -1, -1, 1, -1, 1)
    quadTriangles1 = quadGeom(-1, 1, -1, 1, 1, 1)
    quadTriangles2 = quadGeom(-1, 1, 1, 1, -1, 1)
    quadTriangles3 = quadGeom(-1, 1, -1, 1, -1, -1)
    quadTriangles4 = quadGeom(-1, -1, -1, -1, 1, 1)
    quadTriangles5 = quadGeom(1, -1, -1, 1, 1, 1)

    node = GeomNode('cube-triangles')

    node.addGeom(quadTriangles0)
    node.addGeom(quadTriangles1)
    node.addGeom(quadTriangles2)
    node.addGeom(quadTriangles3)
    node.addGeom(quadTriangles4)
    node.addGeom(quadTriangles5)

    return node

def cubeNodePath():
    
    # Make cube geometry nodes
    cubeTriangles = cubeGeomNode()

    # Make parent panda node
    cube = PandaNode("cube")
    
    # Make parent nodepath handle and attach cube geometry nodes
    parent = NodePath(cube)
    parent.attachNewNode(cubeTriangles).setTwoSided(True)

    return parent

def sphereNodePath(radius: float):
    pass

def cylinderNodePath(radius_bottom: float, radius_top: float, height: float):
    pass