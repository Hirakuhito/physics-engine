import matplotlib.pyplot as plt
import matplotlib.animation as animation
from field import Field
from typing import Literal
from functools import partial


class Visualizer:
    def __init__(self, field: Field, origin: Literal["tc", "cc", "bc", "bl"] = "cc"):
        # Figure Size
        self.width = field.width
        self.height = field.height
        self.origin = origin

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_aspect("equal")

        self._set_origin(origin)

    def _set_origin(self, origin: str):
        match origin:
            case "tc":
                self.w_offset = self.width / 2
                self.h_offset = self.height
                self.ax.set_xlim(-self.w_offset, self.w_offset)
                self.ax.set_ylim(-self.h_offset, 0)

            case "cc":
                self.w_offset = self.width / 2
                self.h_offset = self.height / 2
                self.ax.set_xlim(-self.w_offset, self.w_offset)
                self.ax.set_ylim(-self.h_offset, self.h_offset)

            case "bc":
                self.w_offset = self.width / 2
                self.h_offset = self.height
                self.ax.set_xlim(-self.w_offset, self.w_offset)
                self.ax.set_ylim(0, self.h_offset)

            case "bl":
                self.w_offset = self.width
                self.h_offset = self.height
                self.ax.set_xlim(0, self.w_offset)
                self.ax.set_ylim(0, self.h_offset)

            case _:
                self.w_offset = self.width / 2
                self.h_offset = self.height / 2
                self.ax.set_xlim(-self.w_offset, self.w_offset)
                self.ax.set_ylim(-self.h_offset, self.h_offset)

    def _init_visualizer(self):
        self.ax.cla()
        self.ax.set_aspect("equal")
        self._set_origin(self.origin)

    def show_image(self):
        print("This is test message")

    def update(self, field: Field):
        pass
