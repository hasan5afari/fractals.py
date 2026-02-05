from visualizer import Visualizer
from lindenmayer_system import LindenmayerSystem


def main() -> None:
    WINDOW_SIZE = (800, 800)

    system, dtheta = LindenmayerSystem.from_json(".\\lindenmayer_systems\\dragon_curve.json")
    visualizer = Visualizer(WINDOW_SIZE, (250, 250), 20, 0.9, dtheta)

    visualizer.run(system)



if __name__ == "__main__":
    main()
