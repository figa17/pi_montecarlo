import random


def estimate_pi(n_points: int) -> int:

    in_circle = 0

    for _ in range(n_points):
        x, y = (random.uniform(-1, 1) for v in range(2))
        rad_square = x**2 + y**2

        if rad_square <= 1:
            in_circle += 1

    return 4 * (in_circle / n_points)
