# Panda3D dependencies
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import AntialiasAttrib
from panda3d.core import loadPrcFileData
from panda3d.core import WindowProperties

# SimPy dependencies
from simpy.rt import SimTime
from simpy.rt import RealtimeEnvironment

# Other dependencies
from threading import Thread
from time import time

class Container:

    def __init__(self, sim_time_to_real_time_ratio: float):

        # Remember ratio between simulation and real time
        self.sim_time_to_real_time_ratio = sim_time_to_real_time_ratio

        # Remember simulation time
        self.sim_time_until: float = None

        # Remember real times
        self.real_time_start: float = None
        self.real_time_end: float = None
        self.real_time_now: float = None

        # Create simulation
        self.env = RealtimeEnvironment(factor=sim_time_to_real_time_ratio, strict=False)

        # Define window properties
        props = WindowProperties()
        props.setTitle('SimPanda')

        # Define render properties
        loadPrcFileData('', 'framebuffer-multisample 1\nmultisamples 64')

        # Create visualization
        self.app = ShowBase()
        self.app.win.requestProperties(props)
        self.app.render.setAntialias(AntialiasAttrib.MMultisample)
        self.app.taskMgr.add(self._update, "update")
    
    def run(self, sim_time_duration: SimTime):

        # Remember simulation time
        self.sim_time_until = sim_time_duration

        # Start simulation
        Thread(target=self._run).start()

        # Start visualization
        self.app.run()

    def _run(self):

        # Remember real time before starting
        self.real_time_start = time()

        # Start discrete event processing
        self.env.run(until=self.sim_time_until)
        
        # Remember real time after finishing
        self.real_time_end = time()

    # Visualization update function executed every frame
    def _update(self, task):

        # Update current real time
        self.real_time_now = time()

        # Calculate real time maximum
        realtime_maximum = self.sim_time_until / self.sim_time_to_real_time_ratio

        # Calculate real time current
        realtime_current = self.real_time_now - self.real_time_start
        
        # Calculate progress from difference and maximum
        progress = realtime_current / realtime_maximum

        # Continue updating the visualization or stop
        return Task.cont if progress < 1 else Task.done