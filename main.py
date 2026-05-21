import matplotlib
from field import Field
from engine import Engine
from visual import Visualizer


def show_status():
    print(matplotlib.get_backend())


def main():
    show_status()

    # --- def simu env ---
    field = Field(800, 600)
    visualizer = Visualizer(800, 600)
    engine = Engine(field=field, visualizer=visualizer)

    engine.run()


if __name__ == "__main__":
    main()
