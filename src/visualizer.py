import math
import pygame

from lindenmayer_system import LindenmayerSystem


class Visualizer:
    def __init__(
        self,
        window_size: tuple[int, int],
        start_position: tuple[int, int],
        line_length: int,
        ratio: float,
        dtheta: float,
    ) -> None:
        self._start_position = start_position
        self._x = start_position[0]
        self._y = start_position[1]
        self._line_length = line_length
        self._ratio = ratio
        self._theta = math.pi / 2
        self._dtheta = dtheta
        self._screen = pygame.display.set_mode(window_size)
        self._states: list[dict[str, float]] = []

        pygame.init()

    def _draw(self, lindenmayer_system: LindenmayerSystem) -> None:
        for character in lindenmayer_system.get_sentence():
            if character == "F" or character == "G":
                x, x_new = (self._x, self._x - self._line_length * math.cos(self._theta))
                y, y_new = (self._y, self._y - self._line_length * math.sin(self._theta))
                pygame.draw.line(self._screen, (255, 255, 255), (x, y), (x_new, y_new))
                self._x = x_new
                self._y = y_new
            elif character == "+":
                self._theta += math.radians(self._dtheta)
            elif character == "-":
                self._theta -= math.radians(self._dtheta)
            elif character == "[":
                self._states.append({"x": self._x, "y": self._y, "theta": self._theta})
            elif character == "]":
                current_state = self._states.pop()
                self._x = current_state["x"]
                self._y = current_state["y"]
                self._theta = current_state["theta"]
            else:
                continue

    def run(self, lindenmayer_system: LindenmayerSystem) -> None:
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._screen.fill((0, 0, 0))
                    self._draw(lindenmayer_system)
                    lindenmayer_system.iterate()

                    # reset x, y, theta and update line_length
                    self._x = self._start_position[0]
                    self._y = self._start_position[1]
                    self._theta = math.pi / 2
                    self._line_length *= self._ratio

            pygame.display.flip()

        pygame.quit()
