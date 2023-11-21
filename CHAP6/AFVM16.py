#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Les imports
import turtle
from turtle import Screen, Terminator, Turtle
# Une liste de couleurs pour que ce soit plus jolie
COLOR = ['red', 'green', 'blue', 'brown', 'violet', 'purple', 'yellow']
# Une astuce pour empêcher Turtle de se mettre en erreur
def spyder_bye():
    try:
        Screen().bye()
        turtle.TurtleScreen._RUNNING = True
    except Terminator:
        pass
turtle.bye = spyder_bye
# La fonction récursive
def draw_branch(n, longueur=30):
    t.down()
    if n <= 1 :
        t.forward(longueur//3)
        t.left(60)
        t.forward(longueur//3)
        t.right(120)
        t.forward(longueur//3)
        t.left(60)
        t.forward(longueur//3) # A compléter
    else :
        draw_branch(n-1, longueur//3)
        t.left(60)
        draw_branch(n-1, longueur//3)
        t.right(120)
        draw_branch(n-1, longueur//3)
        t.left(60)
        draw_branch(n-1, longueur//3)
    t.up()
# Le corps principal
# A noter : Il faut cliquer sur la fenêtre graphique pour quitter
t=Turtle()
t.speed(0)
distance = 300
profondeur = 5
t.up()
t.setpos(-300,100)
for i in range(3):
    t.color(COLOR[i])
    draw_branch(profondeur, distance) # Appel à la fonction récursive
    t.right(120)
t.hideturtle()
ts = turtle.getscreen()
ts.getcanvas().postscript(file="feur.eps")
t.screen.exitonclick() # A noter : Il faut cliquer sur la fenêtre graphique pour quitter
turtle.bye()