# Find the cube root of a perfect cube

def print_cubed_root():
    x = int(input('Enter an integer: '))
    ans = 0
    while ans**3 < abs(x):
        ans = ans + 1
    if ans**3 != abs(x):
        print(x, 'is not a perfect cube')
    else:
        if x < 0:
            ans = -ans
        print(f"Cube root of {x} is {ans}")


def is_prime():
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


def main():
    # print_cubed_root()
    is_prime()


main()
