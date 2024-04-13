from panda3d.core import LVector3
from panda3d.core import Geom
from panda3d.core import GeomNode
from panda3d.core import GeomLines
from panda3d.core import GeomTriangles
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexData
from panda3d.core import GeomVertexWriter
from panda3d.core import PandaNode
from panda3d.core import NodePath

def _normalize(x: float, y: float, z: float):

    myVec = LVector3(x, y, z)
    myVec.normalize()

    return myVec

def _quadLineGeom(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, a: float = 1.0):

    format = GeomVertexFormat.getV3n3cpt2()
    data = GeomVertexData('quad', format, Geom.UHDynamic)

    vertex = GeomVertexWriter(data, 'vertex')
    color = GeomVertexWriter(data, 'color')

    if x1 != x2:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y1, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y2, z2)

    else:
        vertex.addData3(x1, y1, z1)
        vertex.addData3(x2, y2, z1)
        vertex.addData3(x2, y2, z2)
        vertex.addData3(x1, y1, z2)

    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)

    lines = GeomLines(Geom.UHDynamic)
    lines.addVertices(0, 1)
    lines.addVertices(1, 2)
    lines.addVertices(2, 3)
    lines.addVertices(3, 0)

    geom = Geom(data)
    geom.addPrimitive(lines)

    return geom

def _quadTriangleGeom(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, r: float, g: float, b: float, a: float = 1.0):

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

    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)
    color.addData4f(r, g, b, a)

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

def _cubeLineGeom(r: float, g: float, b: float, a: float = 1):

    quadLines0 = _quadLineGeom(-1, -1, -1, 1, -1, 1, r, g, b, a)
    quadLines1 = _quadLineGeom(-1, 1, -1, 1, 1, 1, r, g, b, a)
    quadLines2 = _quadLineGeom(-1, 1, 1, 1, -1, 1, r, g, b, a)
    quadLines3 = _quadLineGeom(-1, 1, -1, 1, -1, -1, r, g, b, a)
    quadLines4 = _quadLineGeom(-1, -1, -1, -1, 1, 1, r, g, b, a)
    quadLines5 = _quadLineGeom(1, -1, -1, 1, 1, 1, r, g, b, a)

    node = GeomNode('cube-lines')
    
    node.addGeom(quadLines0)
    node.addGeom(quadLines1)
    node.addGeom(quadLines2)
    node.addGeom(quadLines3)
    node.addGeom(quadLines4)
    node.addGeom(quadLines5)

    return node

def _cubeTriangleGeom(r: float, g: float, b: float, a: float = 1):

    quadTriangles0 = _quadTriangleGeom(-1, -1, -1, 1, -1, 1, r, g, b, a)
    quadTriangles1 = _quadTriangleGeom(-1, 1, -1, 1, 1, 1, r, g, b, a)
    quadTriangles2 = _quadTriangleGeom(-1, 1, 1, 1, -1, 1, r, g, b, a)
    quadTriangles3 = _quadTriangleGeom(-1, 1, -1, 1, -1, -1, r, g, b, a)
    quadTriangles4 = _quadTriangleGeom(-1, -1, -1, -1, 1, 1, r, g, b, a)
    quadTriangles5 = _quadTriangleGeom(1, -1, -1, 1, 1, 1, r, g, b, a)

    node = GeomNode('cube-triangles')

    node.addGeom(quadTriangles0)
    node.addGeom(quadTriangles1)
    node.addGeom(quadTriangles2)
    node.addGeom(quadTriangles3)
    node.addGeom(quadTriangles4)
    node.addGeom(quadTriangles5)

    return node

def cube(r: float, g: float, b: float, a: float = 1):
    
    # Make cube geometry nodes
    cubeLines = _cubeLineGeom(1, 1, 1, 1)
    cubeTriangles = _cubeTriangleGeom(r, g, b, a)

    # Make parent panda node
    cube = PandaNode("cube")
    
    # Make parent nodepath handle and attach cube geometry nodes
    parent = NodePath(cube)
    parent.attachNewNode(cubeLines)
    parent.attachNewNode(cubeTriangles).setTwoSided(True)

    return parent

def sphere(radius: float):
    pass

def cylinder(radius_bottom: float, radius_top: float, height: float):
    pass