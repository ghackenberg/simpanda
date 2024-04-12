import panda3d
import simpy
import simpy.rt
import threading

# Simulation steps to make per second
steps_per_second = 30
# Duration of the simulation in seconds
duration_in_seconds = 10

# Simulation function executed in a thread
def run():

    # Define relation between steps and seconds
    factor = 1 / steps_per_second
    
    # Calculate number of steps to simulate
    until = duration_in_seconds * steps_per_second
    
    # Create and run real-time simulation environment
    env = simpy.rt.RealtimeEnvironment(factor=factor, strict=False)
    env.run(until=until)

# Start simulation thread
thread = threading.Thread(target=run)
thread.start()