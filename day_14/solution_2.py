import numpy as np
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)

input_txt = open("input.txt").read()

W, H = 101, 103

robots = list()

for line in input_txt.split("\n"):
    p, v = line.split(" ")
    p = [int(x) for x in p.split("=")[1].split(',')]
    v = [int(x) for x in v.split("=")[1].split(',')]
    robots += [(p, v)]

min_safety_factor = 10000000000000000000

for i in range(10000):
    safety_factor = 0
    bathroom = np.zeros((H, W))

    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0]) % W
        robot[0][1] = (robot[0][1] + robot[1][1]) % H
        bathroom[robot[0][1], robot[0][0]] += 1

    quadrants = bathroom[:H//2, :W//2], bathroom[H//2 + 1:, :W//2], bathroom[:H//2, W//2 + 1:], bathroom[H//2 + 1:, W//2 + 1:]
    
    counts = list()

    for quadrant in quadrants:
        counts += [np.sum(quadrant)]

    safety_factor = np.prod(counts)

    if safety_factor < min_safety_factor:
        min_safety_factor = safety_factor
        plt.imsave(f"imgs/frame_{i}_{safety_factor}.png", bathroom)
