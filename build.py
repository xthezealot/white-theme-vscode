#!/usr/bin/env python3
"""Generate White and White Night themes."""

import copy
import definitions
import json


class Color(object):
    """Color defines a color."""

    def __init__(self, hex6, alpha=1):
        """Make a Color.

        :param hex6: the 6 digits hexadecimal representation
        :param alpha: the alpha value between 0 and 1
        """
        if hex6.startswith('#'):
            hex6 = hex6[1:]
        if len(hex6) != 6:
            raise ValueError('Hexadecimal value must have 6 chars')
        hex6 = hex6.lower()

        self._rgb = int(hex6, 16)
        self.alpha = alpha

    @property
    def alpha(self):
        """Get the alpha of the color, always between 0 and 1."""
        return self._alpha

    @alpha.setter
    def alpha(self, v):
        if not 0 <= v <= 1:
            raise ValueError('Alpha must be between 0 and 1')
        self._alpha = v

    def __str__(self):
        """Get the shortest hexadecimal color value."""
        s = '{:06x}'.format(self._rgb)
        if self.alpha < 1:
            s += '{:02x}'.format(int(self.alpha*255))
        if s[0] == s[1] and s[2] == s[3] and s[4] == s[5]:
            if len(s) == 6:
                s = s[0] + s[2] + s[4]
            elif s[6] == s[7]:
                s = s[0] + s[2] + s[4] + s[6]
        return '#'+s


class ColorSplit(object):
    """Contains colors for White and White Night themes."""

    def __init__(self, white, white_night=None):
        """Make a color split for White and White Night themes."""
        if isinstance(white, ColorSplit):
            self.white = copy.deepcopy(white.white)
        else:
            self.white = Color(white)

        if white_night:
            if isinstance(white_night, ColorSplit):
                self.white_night = copy.deepcopy(white_night.white_night)
            else:
                self.white_night = Color(white_night)
        else:
            self.white_night = copy.deepcopy(self.white)

    def set_alpha(self, white, white_night=None):
        """Set alpha values of colors.

        :rtype: ColorSplit
        """
        self.white.alpha = white
        self.white_night.alpha = white_night if white_night else white
        return self

    def with_alpha(self, white, white_night=None):
        """Set alpha values of colors on a color split copy.

        :rtype: ColorSplit
        """
        color_split = copy.deepcopy(self)
        color_split.set_alpha(white, white_night)
        return color_split


def forge(defs, night=False):
    """Replace color splits with plain strings."""
    for d in defs:
        if isinstance(defs[d], dict):
            forge(defs[d], night)
        elif isinstance(defs[d], list):
            for i, v in enumerate(defs[d]):
                if isinstance(v, dict):
                    forge(defs[d][i], night)
        elif isinstance(defs[d], definitions.ColorSplit):
            defs[d] = str(defs[d].white) if not night else str(
                defs[d].white_night)


def dump(night=False):
    """Write definitions to JSON files."""
    filepath = 'themes/White'
    if night:
        filepath += '-Night'
    filepath += '-color-theme.json'

    with open(filepath, 'w') as f:
        dd = copy.deepcopy(definitions.definitions)
        forge(dd, night)
        json.dump(dd, f, indent=4)


if __name__ == '__main__':
    dump()
    dump(True)
