from pi_montecarlo import estimate_pi, estimate_pi_np
import time

NUM_POINTS = 10_000_000


def main():
    start = time.time()
    pi = estimate_pi(NUM_POINTS)
    end = time.time()

    print(f"python estimation: {pi} took: {(end-start)}")

    start = time.time()
    pi = estimate_pi_np(NUM_POINTS)
    end = time.time()

    print(f"numpy estimation: {pi} took: {(end-start)}")

if __name__ == "__main__":
    main()
