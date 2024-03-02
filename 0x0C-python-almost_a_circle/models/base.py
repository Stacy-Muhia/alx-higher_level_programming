#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json


class Base:
    """
    ...
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        color_size = len(color_list)
        color_index = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(90)
        turtle.forward(screen_height/2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()
