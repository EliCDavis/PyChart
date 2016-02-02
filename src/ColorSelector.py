import math
import random


class ColorSelector:

    def __init__(self):

        self._colors_for_selection = ['F94F48', 'FF6A41', 'B4B4B4', 'D5D5D5', 'E973F5', '237FEA',
                                      'F2B838', '19EC5A', '2395DE', 'D4B57F', 'FFD700']

        self._colors_already_selected = []

    def get_random_color(self):

        index = math.floor(random.random()*len(self._colors_for_selection))

        index_has_been_found = False

        # Keep trying to find an index until we're successful
        # TODO this needs to be way more efficient
        while index_has_been_found is False:

            if index not in self._colors_already_selected:

                index_has_been_found = True

            else:

                index = math.floor(random.random()*len(self._colors_for_selection))

        # Finally get our color
        color = self._colors_for_selection[index]

        self._colors_already_selected.append(index)

        # If we've used all the colors then start all over
        if len(self._colors_already_selected) == len(self._colors_for_selection):
            self._colors_already_selected = []

        return color
