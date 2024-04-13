from simpanda import Container
from simpanda import cube

container = Container(sim_time_to_real_time_ratio=1)

container.app.disableMouse()
container.app.camera.setPos(0, -20, 0)

cube1 = cube(1, 0, 0)
cube1.reparentTo(container.app.render)
cube1.setPos(-5, 0, 0)
cube1.hprInterval(15, (360, 0, 0)).loop()

cube2 = cube(0, 1, 0)
cube2.reparentTo(container.app.render)
cube2.setPos(0, 0, 0)
cube2.hprInterval(15, (360, 0, 0)).loop()

cube3 = cube(0, 0, 1)
cube3.reparentTo(container.app.render)
cube3.setPos(5, 0, 0)
cube3.hprInterval(15, (360, 0, 0)).loop()

container.run(sim_time_duration=10)