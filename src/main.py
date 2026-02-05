from visualizer import Visualizer
from lindenmayer_system import LindenmayerSystem


def main() -> None:
    WINDOW_SIZE = (1200, 800)
    START_POSITION = (600, 400)
    LINE_LENGTH = 250
    RATIO = 0.65

    system, dtheta = LindenmayerSystem.from_json(".\\lindenmayer_systems\\triangle.json")
    visualizer = Visualizer(WINDOW_SIZE, START_POSITION, LINE_LENGTH, RATIO, dtheta)

    visualizer.run(system)


if __name__ == "__main__":
    main()
