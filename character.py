"""
    Import os for file
"""
import os
from display import Display

class Character:
    """
        Class character
    """
    nb_object_get = 0

    def __init__(self, data_file, letter):
        """
            Loading character from file .txt
        """

        directory = os.path.dirname(__file__)
        path_to_file = os.path.join(directory, 'data', data_file)

        with open(path_to_file) as file:
            for (key_y, line) in enumerate(file):
                for (key_x, character) in enumerate(line):
                    if character == letter:
                        self.position_x = key_x
                        self.position_y = key_y

    def move(self, maps, direction, position):
        """
            Update the last and next position
        """
        display = Display.getInstance()

        position_x = int(position[0])
        position_y = int(position[1])

        position_x_general = 0
        position_y_general = 0

        # Commentaire
        if direction == 'l':
            position_x_general = position_x - 1
            position_y_general = position_y
        elif direction == 'r':
            position_x_general = position_x + 1
            position_y_general = position_y
        elif direction == 'u':
            position_x_general = position_x
            position_y_general = position_y - 1
        elif direction == 'd':
            position_x_general = position_x
            position_y_general = position_y + 1

        if maps[position_y_general][position_x_general] == 'X':
            display.set_text("WALL")
        elif maps[position_y_general][position_x_general] in ['N', 'E', 'T']:
            self.nb_object_get = self.nb_object_get + 1
            maps[position_y][position_x] = ' '
            maps[position_y_general][position_x_general] = 'M'
            display.set_text(str(self.nb_object_get)+' OBJECTS FOUND')
        elif (maps[position_y_general][position_x_general] == 'G' and self.nb_object_get < 3):
            exit()
        elif (maps[position_y_general][position_x_general] == 'G' and self.nb_object_get == 3):
            maps[position_y][position_x] = ' '
            maps[position_y_general][position_x_general] = 'M'
            display.set_text('WIN')
        else:
            maps[position_y][position_x] = ' '
            maps[position_y_general][position_x_general] = 'M'
            display.set_text('IN PROGRESS')

        return maps