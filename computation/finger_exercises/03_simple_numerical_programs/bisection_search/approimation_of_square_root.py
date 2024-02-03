import matplotlib.pyplot as plt


def print_approximation_of_square_root(x):
    epsilon = 0.01
    num_guesses, low = 0, 0
    high = max(1, x)
    ans = (high + low) / 2
    guesses = [ans]  # List to store the values for plotting

    while abs(ans**2 - x) >= epsilon:
        num_guesses += 1
        if ans**2 < x:
            low = ans  # Adjust the low bound
        else:
            high = ans  # Adjust the high bound
        ans = (high + low) / 2  # Recalculate the midpoint
        guesses.append(ans)  # Store the value for plotting

    print(ans, 'is close to square root of', x)
    print('Number of guesses:', num_guesses)

    # Plotting the iterations
    plt.plot(guesses, marker='o')
    plt.axhline(y=(ans), color='r', linestyle='--', label='Final Approximation')
    plt.xlabel('Iteration')
    plt.ylabel('Approximation Value')
    plt.title('Square Root Approximation Convergence')
    plt.legend()
    plt.show()

print_approximation_of_square_root(25)
# print_approximation_of_square_root(0.25)
