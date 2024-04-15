"""Point CQ."""
__author__ = "730670116"
from __future__ import annotations
class Point:

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Init constructor."""
        self.x_init = x_init
        self.y_init = y_init

    def scale_by(self, factor: int) -> None:
        """Scale method, mutate list."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Scale method, do not mutate list."""
        update_x = self.x * factor
        update_y = self.y * factor
        return Point(update_x, update_y)