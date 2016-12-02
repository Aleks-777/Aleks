import turtle
def curve(l,n, an=45):
    turtle.speed('fastest')
    if n==0:
        turtle.forward(l)
    else:
        turtle.right(an)
        curve(l/2,n-1,45)
        turtle.left(an*2)
        curve(l/2,n-1,-45)
        turtle.right(an)

curve(10000,10)
turtle.done()