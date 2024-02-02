# Computation

## Exhaustive Enumeration

**Exhaustive Enumeration** is a basic form of the **Guess and Check** approach.

### Guess and Check

- A fundamental technique used in various algorithms and prblem-soving scenarios.

- A problem-solving approach where you guess a solution, check if it works,
and iterate until you find the correct solution or reach a stisfactory result.

```python
# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1

if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
```

## Test Walkthrough

### Perfect Cube Example

**Input**: Enter an integer: 27

**Execution:**
1. Initialize `ans` to 0.
2. Iteration 1:
   - `ans = 1` (since \(1^3 < |27|\)).
   - The loop continues.
3. Iteration 2:
   - `ans = 2` (since \(2^3 < |27|\)).
   - The loop continues.
4. Iteration 3:
   - `ans = 3` (since \(3^3 = 27\)).
   - The loop stops.
5. Check:
   - \(3^3 = 27\), which is equal to the absolute value of the input.
6. Output: Cube root of 27 is 3.

### Non-Perfect Cube Example

**Input**: Enter an integer: 16

**Execution:**
1. Initialize `ans` to 0.
2. Iteration 1:
   - `ans = 1` (since \(1^3 < |16|\)).
   - The loop continues.
3. Iteration 2:
   - `ans = 2` (since \(2^3 < |16|\)).
   - The loop continues.
4. Iteration 3:
   - `ans = 3` (since \(3^3 < |16|\)).
   - The loop continues.
5. Iteration 4:
   - `ans = 4` (since \(4^3 > |16|\)).
   - The loop stops.
6. Check:
   - \(4^3 = 64\), which is not equal to the absolute value of the input.
7. Output: 16 is not a perfect cube.

