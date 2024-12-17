import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(72):
    t.color(colors[i % 6])
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.right(5)

turtle.done()
