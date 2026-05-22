from engine import Engine
from field import Field
from rigid_body import RigidBody
from visual import Visualizer
from rich.table import Table
from rich.console import Console


def show_status():
    console = Console()
    table = Table(title="CONFIGURATION")

    console.print(table)


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
