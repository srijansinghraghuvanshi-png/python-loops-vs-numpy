"""Compare Python list-comprehension squaring with NumPy vectorized squaring.

Run with: python benchmark.py
"""

from statistics import median
from time import perf_counter

import numpy as np

N = 1_000_000
REPETITIONS = 5
WARMUP_RUNS = 2


def python_squares(values: list[int]) -> list[int]:
    """Square values using a Python list comprehension."""
    return [value * value for value in values]


def numpy_squares(values: np.ndarray) -> np.ndarray:
    """Square values using NumPy vectorized multiplication."""
    return values * values


def measure(function, values, repetitions: int) -> list[float]:
    """Return elapsed times for repeated calls to function(values)."""
    timings = []
    for _ in range(repetitions):
        start = perf_counter()
        function(values)
        timings.append(perf_counter() - start)
    return timings


def main() -> None:
    python_values = list(range(N))
    numpy_values = np.arange(N, dtype=np.int64)

    # Warm up both implementations before collecting measurements.
    for _ in range(WARMUP_RUNS):
        python_result = python_squares(python_values)
        numpy_result = numpy_squares(numpy_values)

    # Confirm both approaches compute identical values.
    if not np.array_equal(np.asarray(python_result), numpy_result):
        raise RuntimeError("The Python and NumPy results do not match.")

    python_times = measure(python_squares, python_values, REPETITIONS)
    numpy_times = measure(numpy_squares, numpy_values, REPETITIONS)

    python_median = median(python_times)
    numpy_median = median(numpy_times)

    print(f"Elements: {N:,}")
    print(f"Measured repetitions: {REPETITIONS}")
    print(f"Python median: {python_median:.6f} seconds")
    print(f"NumPy median:  {numpy_median:.6f} seconds")

    if numpy_median > 0:
        print(f"Observed speedup: {python_median / numpy_median:.2f}x")
    else:
        print("Observed speedup: unavailable (NumPy timing was zero).")


if __name__ == "__main__":
    main()
