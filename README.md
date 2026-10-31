# Python Loops vs NumPy

A small, reproducible experiment comparing Python-level looping with NumPy vectorized arithmetic.

## What this project does

The benchmark computes the square of integers from 0 to 999,999 using two approaches:

1. A Python list comprehension.
2. NumPy array multiplication.

It checks that both approaches produce the same values, warms up each implementation, runs multiple timed repetitions, and reports median execution times and the observed speedup.

## Requirements

- Python 3.9 or newer
- NumPy

## Setup

Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python benchmark.py
```

The script prints the median time for each calculation and the measured speedup. It does not include list/array construction in the timed section.

## Benchmark methodology

- Uses the same input values and square operation in both implementations.
- Performs warm-up runs before collecting measurements.
- Collects five measurements per implementation.
- Reports the median rather than a single timing.
- Verifies the outputs are equal before reporting timings.
- Uses `time.perf_counter()` for elapsed-time measurement.

## Important caveats

- Results depend on CPU, operating system, Python and NumPy versions, system load, and memory conditions.
- The benchmark measures the calculation step; input construction and output allocation are outside the timed sections. NumPy's output allocation is part of the vectorized operation, while Python list-comprehension allocation is part of its operation, so the two approaches have different allocation behavior.
- This is a simple illustrative microbenchmark, not a universal ranking of Python and NumPy. For small inputs, NumPy call overhead may outweigh its benefits.
- No benchmark result is claimed in this README. Run the script on your own machine to obtain local measurements.

## Learning goals

- Understand Python loop overhead.
- Explore NumPy arrays and vectorized operations.
- Learn basic, repeatable performance measurement.
- Interpret benchmark results carefully.

## References

- [Python documentation](https://docs.python.org/3/)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [What is NumPy?](https://numpy.org/doc/stable/user/whatisnumpy.html)

## Author

Srijan Singh Raghuvanshi
