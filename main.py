from pip import main
from pi_montecarlo import estimate_pi
import time

NUM_POINTS = 10_000


def main():
    start = time.time()

    pi = estimate_pi(NUM_POINTS)
    end = time.time()

    print(f"value: {pi} took: {(end-start)}")


if __name__ == "__main__":
    main()
