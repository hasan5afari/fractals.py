from visualizer import Visualizer
from lindenmayer_system import LindenmayerSystem


def main() -> None:
    WINDOW_SIZE = (1200, 800)

    system, dtheta = LindenmayerSystem.from_json(".\\lindenmayer_systems\\triangle.json")
    visualizer = Visualizer(WINDOW_SIZE, (600, 400), 250, 0.65, dtheta)

    visualizer.run(system)


if __name__ == "__main__":
    main()
