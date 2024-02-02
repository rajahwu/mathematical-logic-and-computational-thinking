# Graphics

## turtle

```python
import turtle

window = turtle.Screen()
window.screensize(400, 400)
window.bgcolor("lightgreen")
window.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.forward(50)
tess.left(120)

alex = turtle.Turtle()

alex.forward(150)
alex.left(90)
alex.forward(30)

tess.penup()
size = 20
for _ in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

window.mainloop()

```

![turtle hello program](/graphics/public/assets/turtle-hello.gif)

## tkinter


```python
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Python GUI")

def click_me():
    action.configure(text='Hello ' + name.get())

ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=1, row=1)
action.configure(state='disabled')

name_entered.focus()

window.mainloop()

```

![tkinter simple gui](/graphics/public/assets/tkinter-simple-gui.png)

## matplotlib

```python
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

```

![matplotlib cartesian](/graphics/public/assets/matplotlib-cartesian.png)
