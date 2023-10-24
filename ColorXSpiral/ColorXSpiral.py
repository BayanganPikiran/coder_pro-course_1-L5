import turtle as t

colors = ["red", "yellow", "blue", "orange", "green", "purple"]

t.bgcolor("black")
t.pen()

# You can choose between 2 and 6 sides for some cool shapes

sides = 6

for x in range(200):
    t.pencolor(colors[x % sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x * sides /200)

t.exitonclick()