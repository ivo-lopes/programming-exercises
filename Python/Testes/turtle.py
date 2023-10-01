from turtle import *

tartaruga = Turtle()
wn = Screen().bgcolor('black')
tartaruga.goto(0, 200)
a = 0
b = 0
tartaruga.speed(10)
tartaruga.pencolor('green')

while True:
    tartaruga.forward(a)
    tartaruga.right(b)
    a += 3
    b += 1
    if b == 120:
        break
    tartaruga.hideturtle()