import time
import turtle

window = turtle.Screen()
window.screensize(400, 400)
window.bgcolor("lightgreen")
window.title("Hello, Tess!")

time.sleep(5)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.forward(50)
tess.left(120)

time.sleep(2)
alex = turtle.Turtle()

alex.forward(150)
alex.left(90)
alex.forward(30)

time.sleep(2)
tess.penup()
size = 20
for _ in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

window.mainloop()