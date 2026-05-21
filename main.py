import matplotlib

matplotlib.use("QtAgg")

from field import Field
from engine import Engine
from visual import Visualizer
from rigid_body import RigidBody


def show_status():
    print("STATUS")
    print(matplotlib.get_backend())


def main():
    show_status()

    # --- def simu env ---
    width = 800
    height = 600
    field = Field(width, height)
    visualizer = Visualizer(width, height, origin="cc")
    engine = Engine(field=field, visualizer=visualizer)

    engine.field.set_gravity()

    circle = RigidBody(0, 0, 10)
    engine.field.add_body(circle)

    engine.run()


if __name__ == "__main__":
    main()
