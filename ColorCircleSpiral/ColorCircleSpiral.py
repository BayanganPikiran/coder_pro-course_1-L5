import turtle as t

colors = ["red", "yellow", "blue", "green"]

t.pen()
t.bgcolor("black")
for x in range(100):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
t.exitonclick()
