import matplotlib.pyplot as plt
import numpy as np

# Define the inequality: x > 9
# We can rewrite it as x - 9 > 0
coefficients = np.array([1])
rhs = 9

# Generate x values for the plot
x_values = np.linspace(0, 15, 400)

# Create a boolean mask based on the inequality
inequality_mask = (coefficients[0] * x_values - rhs) > 0

# Plot the inequality
plt.figure(figsize=(8, 4))
plt.fill_between(x_values, 0, 1, where=inequality_mask, color='lightblue', alpha=0.3, label='x > 9')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Region')
plt.title('Inequality Plot: x > 9')

# Add a legend
plt.legend()

# Show the plot
plt.show()
