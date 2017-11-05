#!/usr/bin/env python3
from fractals import translate, rotate, scale, compose
from fractals import render_fractal, render_fractal_np
from fractals import Animation
from fractals import flood_fill
from fractals import invert_colors
from fractals import transform_points
from fractals import rasterize_points
from PIL import Image
import numpy as np
from math import sin, cos, pi
import math

# golden ratio
phi = 1.618033988749894848204586834365638117720309179805762862135

r = (1 / phi)**(1 / phi)
a = math.acos((1 + r**2 - r**4) / (2 * r))
b = math.acos((1 + r**4 - r**2) / (2 * r**2))

wid = 0.4
mid = -0.1
# mats = [
#     compose([scale(mid - wid, 0, r),
#              rotate(mid - wid, 0, a)]),
#     compose([scale(mid + wid, 0, r**2),
#              rotate(mid + wid, 0, 180 - b)]),
# ]
# mats = [
#     compose([scale(0, 0, r), rotate(0, 0, a)]),
#     compose([scale(1, 0, r**2), rotate(1, 0, 180 - b)]),
# ]
# http://ecademy.agnesscott.edu/~lriddle/ifs/heighway/goldenDragon.htm
mats = [
    np.array([
        [0.62367, -0.40337, 0],
        [0.40337, 0.62367, 0],
        [0, 0, 1],
    ]),
    np.array([
        [-0.37633, -0.40337, 1],
        [0.40337, -0.37633, 0],
        [0, 0, 1],
    ]),
]

# width = 3840 * 2
width = 1000
xmid = 0.4
array = render_fractal_np(
    mats, width=width, depth=20, bounds=(xmid - 1, xmid + 1, -1, 1))
array = invert_colors(array)
img = Image.fromarray(array)
img.save("golden_dragon.png")
