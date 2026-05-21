from field import Field
from engine import Engine
from visual import Visualizer


def main():
    # --- def simu env ---
    field = Field(800, 600)
    visualizer = Visualizer(field)
    engine = Engine(field=field, visualizer=visualizer)

    engine.run()


if __name__ == "__main__":
    main()
