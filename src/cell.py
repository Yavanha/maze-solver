from point import Point
from window import Window
from line import Line


class Cell():

    def __init__(self, win: Window, visited=False, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._win = win
        self.visited = visited
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")

        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white")

        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"

        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        to_cell_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_center_y = (to_cell._y1 + to_cell._y2) / 2
        self._win.draw_line(Line(Point(center_x, center_y), Point(
            to_cell_center_x, to_cell_center_y)), fill_color)
