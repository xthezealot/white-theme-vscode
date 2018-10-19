#!/usr/bin/env python3
"""Generate White and White Night themes."""

from __future__ import annotations
from copy import deepcopy
from typing import Any, Dict, Union, Type
import definitions
import json


class Color(object):
    """Color defines a color.

    Args:
        hex6 (str): The 6 digits hexadecimal representation.
        alpha (float, optional): The alpha value between 0 and 1. Defaults to
            1.

    Raises:
        ValueError: The representation is not a 6 digits hexadecimal number.
    """

    def __init__(self, hex6: str, alpha: float = 1):
        if hex6.startswith("#"):
            hex6 = hex6[1:]
        if len(hex6) != 6:
            raise ValueError("Hexadecimal value must have 6 chars")
        hex6 = hex6.lower()

        self._rgb = int(hex6, 16)
        self.alpha = alpha

    @property
    def alpha(self) -> float:
        """Get the alpha of the color, always between 0 and 1.

        Returns:
            float: The alpha value.
        """
        return self._alpha

    @alpha.setter
    def alpha(self, v: float):
        """Get the alpha of the color.

        Args:
            v (float): The alpha value.

        Raises:
            ValueError: The value is not between 0 and 1.
        """
        if not 0 <= v <= 1:
            raise ValueError("Alpha must be between 0 and 1")
        self._alpha = v

    def __str__(self) -> str:
        """Get the shortest hexadecimal color value.

        Returns:
            str: The hexadecimal representation.
        """
        s = "{:06x}".format(self._rgb)
        if self.alpha < 1:
            s += "{:02x}".format(int(self.alpha * 255))
        if s[0] == s[1] and s[2] == s[3] and s[4] == s[5]:
            if len(s) == 6:
                s = s[0] + s[2] + s[4]
            elif s[6] == s[7]:
                s = s[0] + s[2] + s[4] + s[6]
        return "#" + s


class ColorSplit(object):
    """Contains colors for White and White Night themes.

    Args:
        white (Union[str, ColorSplit]): The White theme color from an
            hexadecimal representation or another color split.
        white_night (Union[str, ColorSplit], optional): The White Night theme
            color from an hexadecimal representation or another color split. If
            None, the White version is used. Defaults to None.
    """

    def __init__(self,
                 white: Union[str, ColorSplit],
                 white_night: Union[str, ColorSplit] = None):
        if isinstance(white, ColorSplit):
            self.white: Color = deepcopy(white.white)
        else:
            self.white = Color(white)

        if white_night:
            if isinstance(white_night, ColorSplit):
                self.white_night: Color = deepcopy(white_night.white_night)
            else:
                self.white_night = Color(white_night)
        else:
            self.white_night = deepcopy(self.white)

    def set_alpha(self, white: float, white_night: float = None) -> ColorSplit:
        """Set alpha values of colors.

        Args:
            white (float): The alpha value for the White theme.
            white_night (float, optional): The alpha value for the White Night
                theme. If None, the White version is used. Defaults to None.

        Returns:
            ColorSplit: The same color split.
        """
        self.white.alpha = white
        self.white_night.alpha = white_night if white_night else white
        return self

    def with_alpha(self, white: float,
                   white_night: float = None) -> ColorSplit:
        """Copy colors split and set alpha values of colors.

        Args:
            white (float): The alpha value for the White theme.
            white_night (float, optional): The alpha value for the White Night
                theme. If None, the White version is used. Defaults to None.

        Returns:
            ColorSplit: A color split copy.
        """
        color_split = deepcopy(self)
        color_split.set_alpha(white, white_night)
        return color_split


def forge(defs: Dict[str, Any], night: bool = False):
    """Replace color splits with plain strings.

    Args:
        defs (Dict[str, Any]): The definitions needed to be forged.
        night (bool, optional): Wether forge for the normal theme or its night
            version. Defaults to False.
    """
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


def dump(night: bool = False):
    """Write definitions to JSON files.

    Args:
        night (bool, optional): Wether dump for the normal theme or its night
            version. Defaults to False.
    """
    filepath = "themes/White"
    if night:
        filepath += "-Night"
    filepath += "-color-theme.json"

    with open(filepath, "w") as f:
        defs = deepcopy(definitions.definitions)
        forge(defs, night)
        json.dump(defs, f, indent=4)


if __name__ == "__main__":
    dump()
    dump(True)
