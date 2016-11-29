"""Plotting a graph using matplotlib"""

from matplotlib import pyplot as plt
import numpy as np


def draw_graph():
    x = np.array(range(10))
    y = np.array(range(10))

    plt.plot(x, y)
    plt.xlabel("Size of rooms")
    plt.ylabel("Price of rooms")
    plt.show()

draw_graph()
