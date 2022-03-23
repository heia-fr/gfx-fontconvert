# GFX Font Converter

The code in this repository is based on the `fontconvert`folder of [Adafruit-GFX-Library
](https://github.com/adafruit/Adafruit-GFX-Library). It has been modified to work with
the "MbedOS" and "LibOpenCM3" frameworks. It has also been modified to enable Latin-1
characters.

This repository comes with a ".devcontainer" folder that allows you to run the
code without installing the dependencies yourself.

The `Makefile` and `makefonts.sh` are from Adafruit's code. Currently,
I use the `make_fonts.py` script to generate the fonts.