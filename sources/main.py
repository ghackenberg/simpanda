from simpanda import Container
from simpanda import cubeNodePath

container = Container(1, 10)

container.app.disableMouse()
container.app.camera.setPos(0, -20, 0)

cube = cubeNodePath()
cube.reparentTo(container.app.render)
cube.hprInterval(15, (360, 0, 0)).loop()

container.run()