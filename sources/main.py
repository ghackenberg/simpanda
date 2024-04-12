from simpanda import Container
from simpanda import cubeNodePath

container = Container(sim_time_to_real_time_ratio=1)

container.app.disableMouse()
container.app.camera.setPos(0, -20, 0)

cube = cubeNodePath()
cube.reparentTo(container.app.render)
cube.hprInterval(15, (360, 0, 0)).loop()

container.run(sim_time_duration=10)