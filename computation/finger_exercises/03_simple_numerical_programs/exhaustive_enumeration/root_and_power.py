def root_and_power(x):
    # x = int(input("Enter an integer: "))

    for power in range(2, 6):
        for root in range(abs(x) + 1):
            if root ** power == abs(x):
                if x < 0 and power % 2 == 1:
                    print(f"{x} = -{root}^{power}")
                else:
                    print(f"{x} = {root}^{power}")
                return
    
    # If no such pair is found
    print(f"No pair of integers (root, power) exists for {x} with 1 < power < 6.")

# Example usage

for num in range(13):
    print(f"Root and power for {num}:", end=" ")
    root_and_power(num)
