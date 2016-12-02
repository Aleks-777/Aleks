__author__ = 'student'
import turtle

def curve(l, n):
    turtle.speed('fastest')
    if n == 0:
        turtle.forward(l)
    else:
        x = l/4
        curve(x,n-1)
        turtle.left(90)
        curve(x,n-1)
        turtle.right(90)
        curve(x,n-1)
        turtle.right(90)
        curve(x,n-1)
        curve(x,n-1)
        turtle.left(90)
        curve(x,n-1)
        turtle.left(90)
        curve(x,n-1)
        turtle.right(90)
        curve(x,n-1)

curve(400,3)
