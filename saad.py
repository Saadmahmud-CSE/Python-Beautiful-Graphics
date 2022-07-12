import turtle

wn = turtle.Screen()
wn.bgcolor('black')
s = turtle.Turtle()
s.speed(0)
s.color('cyan')
rotate = int(180)


def Circles(t, size):
    for i in range(12):
        t.circle(size)
        size = size - 4


def saad(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


saad(s, 200, 10)

t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate = int(90)


def Circles(t, size):
    for i in range(6):
        t.circle(size)
        size = size - 10


def saad(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


saad(t1, 160, 10)

t2 = turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate = int(90)


def Circles(t, size):
    for i in range(6):
        t.circle(size)
        size = size - 5


def saad(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


saad(t2, 120, 10)

t3 = turtle.Turtle()
t3.speed(0)
t3.color('red')
rotate = int(90)


def Circles(t, size):
    for i in range(6):
        t.circle(size)
        size = size - 19


def saad(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


saad(t3, 80, 10)

t4 = turtle.Turtle()
t4.speed(0)
t4.color('black')
rotate = int(90)


def Circles(t, size):
    for i in range(6):
        t.circle(size)
        size = size - 20


def saad(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


saad(t4, 40, 10)
turtle.done()