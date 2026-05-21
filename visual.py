import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import partial


class Visualizer:
    def __init__(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect("equal")
