# Computation

## Guess and Check

- A fundamental technique used in various algorithms and prblem-soving scenarios.

- A problem-solving approach where you guess a solution, check if it works,
and iterate until you find the correct solution or reach a stisfactory result.

### Exhaustive Enumeration

**Exhaustive Enumeration** is a basic form of the **Guess and Check** approach.

#### Find the cube root of a perfect cube

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

##### Test Walkthroughs

###### Perfect Cube Example

**Input**: Enter an integer: 27

**Execution:**

1. Initialize `ans = 0`.
2. Iteration 1:
   - `ans = 1` | since $1^3 < |27|$.
   - The loop continues.
3. Iteration 2:
   - `ans = 2` | since $2^3 < |27|$.
   - The loop continues.
4. Iteration 3:
   - `ans = 3` | since $3^3 = 27$.
   - The loop stops.
5. Check:
   - $3^3 = 27$, which is equal to the absolute value of the input.
6. Output: Cube root of 27 is 3.

###### Non-Perfect Cube Example

**Input**: Enter an integer: 16

**Execution:**

1. Initialize `ans = 0`.
2. Iteration 1:
   - `ans = 1` | since $1^3 < |16|$.
   - The loop continues.
3. Iteration 2:
   - `ans = 2` | since $2^3 < |16|$.
   - The loop continues.
4. Iteration 3:
   - `ans = 3` | since $3^3 < |16|$.
   - The loop continues.
5. Iteration 4:
   - `ans = 4` | since $4^3 > |16|$.
   - The loop stops.
6. Check:
   - $4^3 = 64$, which is not equal to the absolute value of the input.
7. Output: 16 is not a perfect cube.

#### Testing if an integer is prime

```python
 x = int(input('Enter an integer greater than 2: '))
    smallest_divisor = None
    for guess in range(2, x):
        if x % guess == 0:
            smallest_divisor = guess
            break
    if smallest_divisor is not None:
        largest_divisor = x // smallest_divisor
        print(f"Largest divisor of {x} is {largest_divisor}")
    else:
        print(f"{x} is a prime number")
```

##### Test Case 1: Prime Number

Input: `7`

Execution:

- The loop iterates from 2 to 6.
- 7 is not divisible by any number in this range.
- The program prints: "7 is a prime number."

##### Test Case 2: Non-Prime Number

Input: `12`

Execution:

- The loop iterates from 2 to 11.
- 12 is divisible by 2.
- The program prints: "Largest divisor of 12 is 6."

##### Test Case 3: Minimum Input

Input: `3`

Execution:

- The loop iterates from 2 to 2.
- 3 is not divisible by any number in this range.
- The program prints: "3 is a prime number."

##### Test Case 4: Maximum Input

Input: `100`

Execution:

- The loop iterates from 2 to 99.
- 100 is divisible by 2.
- The program prints: "Largest divisor of 100 is 50."

##### Test Case 5: Input with No Divisors

Input: `17`

Execution:

- The loop iterates from 2 to 16.
- 17 is not divisible by any number in this range.
- The program prints: "17 is a prime number."
