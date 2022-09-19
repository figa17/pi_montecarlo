import random
import numpy as np


def estimate_pi(n_points: int) -> float:

    in_circle = 0

    for _ in range(n_points):
        x, y = (random.uniform(-1, 1) for v in range(2))
        rad_square = x**2 + y**2

        if rad_square <= 1:
            in_circle += 1

    return 4 * (in_circle / n_points)


def estimate_pi_np(n_points) -> float:
    x = np.random.uniform(low=-1, high=1, size=n_points)
    y = np.random.uniform(low=-1, high=1, size=n_points)

    dist = np.sqrt((x**2) + (y**2))

    return 4 * np.sum(dist <= 1) / n_points
