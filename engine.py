from field import Field
from visual import Visualizer
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Optional


@dataclass
class EngineConfig:
    max_steps: int = 1000
    method: str = "symplectic"


class Engine:
    def __init__(
        self,
        field: Field,
        visualizer: Visualizer,
        config: Optional[EngineConfig] = None,
    ):
        self.field = field
        self.visualizer = visualizer
        self.config = config or EngineConfig()

    def run(self):
        anim = animation.FuncAnimation(self.visualizer.fig, self._update, interval=10)
        plt.show()

    def _update(self, frame):
        self.field.step(method=self.config.method)
        self.visualizer.update(self.field)
