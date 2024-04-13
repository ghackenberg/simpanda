from simpanda import Container
from simpanda import cube

def process(container: Container, x: float, y: float, z: float, s: float, r: float, g: float, b: float):
    # Create 3D visualization object
    object = cube(r, g, b)
    object.reparentTo(container.app.render)
    object.setPos(x, y, z)
    object.setScale(s)
    # Generate simulation events and update visualization object
    pitch = 0.0
    while True:
        object.setHpr(pitch, 0.0, 0.0)
        yield container.env.timeout(1)
        pitch = pitch + 1

# Simulation and visualization container
container = Container(sim_time_to_real_time_ratio=0.1)

# Disable mouse interaction and set camera coordinates
container.app.disableMouse()
container.app.camera.setPos(0, -20, 0)

# Start simulation and visualization processes
container.env.process(process(container, -5.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0))
container.env.process(process(container, -2.5, 0.0, 0.0, 0.1, 0.5, 0.5, 0.0))
container.env.process(process(container,  0.0, 0.0, 0.0, 0.7, 0.0, 0.5, 0.0))
container.env.process(process(container, +2.5, 0.0, 0.0, 0.3, 0.0, 0.5, 0.5))
container.env.process(process(container, +5.0, 0.0, 0.0, 0.6, 0.0, 0.0, 0.5))

# Run the simulation and visualization threads
container.run(sim_time_duration=360)