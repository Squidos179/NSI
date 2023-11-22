import turtle
from turtle import Screen, Terminator, Turtle

t = Turtle()
t.speed(0)

def courbe_sierpinski(n, C, k):
    t.down()
    if n == 0:
        t.forward(C)
        print("J'avance")
    else:
        t.left(k*60)
        courbe_sierpinski(n - 1, C/2, -k) 
        t.right(k*60)
        print(k*60)
        courbe_sierpinski(n - 1, C/2, k) 
        t.right(k*60)
        print(k*60)
        courbe_sierpinski(n - 1, C/2, -k) 
        t.left(k*60)
    t.up()

courbe_sierpinski(10, 1000, 1)
t.hideturtle()
t.screen.exitonclick() # A noter : Il faut cliquer sur la fenêtre graphique pour quitter
turtle.bye()
#a completer