# Factorial For Loop Function Explanation

## Function Overview

The `factorial_forloop(n)` function calculates the factorial of a number using an iterative approach with a for loop.

## How It Works

The function multiplies all integers from `n` down to 1 to compute `n!`.

```python
def factorial_forloop(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result
```

## Dry Run with n = 3

Let's trace through the execution step by step when `n = 3`:

### Initial State
- **Input**: `n = 3`
- **Variable initialization**: `result = 1`

### Loop Iterations

The loop uses `range(n, 0, -1)`, which generates numbers from `n` down to 1 (stopping before 0).

For `n = 3`, the range is: `range(3, 0, -1)` → generates `[3, 2, 1]`

#### Iteration 1
- **Loop variable**: `i = 3`
- **Operation**: `result = result * i` → `result = 1 * 3`
- **New result**: `result = 3`

#### Iteration 2
- **Loop variable**: `i = 2`
- **Operation**: `result = result * i` → `result = 3 * 2`
- **New result**: `result = 6`

#### Iteration 3
- **Loop variable**: `i = 1`
- **Operation**: `result = result * i` → `result = 6 * 1`
- **New result**: `result = 6`

### Final State
- **Return value**: `6`
- **Mathematical verification**: 3! = 3 × 2 × 1 = 6 ✓

## Summary Table

| Iteration | i | result before | Operation | result after |
|-----------|---|---------------|-----------|--------------|
| Start     | - | 1             | -         | 1            |
| 1         | 3 | 1             | 1 × 3     | 3            |
| 2         | 2 | 3             | 3 × 2     | 6            |
| 3         | 1 | 6             | 6 × 1     | 6            |
| End       | - | 6             | -         | **6**        |

## Key Points

- The loop counts **down** from `n` to 1 using `range(n, 0, -1)`
- Each iteration multiplies the current result by the loop variable
- The initial value of `result = 1` serves as the identity element for multiplication
- The final result is returned after all iterations complete