from field import Field
from visual import Visualizer
import matplotlib.animation as animation
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
        self.anim = animation.FuncAnimation(
            self.visualizer.fig,
            self._update,
            interval=1,
            blit=False,
            cache_frame_data=False,
        )
        self.visualizer.show()

    def _update(self, _):
        self.field.step(method=self.config.method)
        self.visualizer.update(self.field)
