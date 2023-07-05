# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:06:49 2023

@author: Gustavo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:34:42 2023

@author: Gustavo
"""

from turtle import Screen, Turtle
#forward avanza de pasos
#backward retrosede pasos
#left gira a la izquierda
#rigth gira a la derecha 
# penup levanta el lapiz
# pendown baja el lapiz

pantalla = Screen()
pantalla.setup(825,825)
pantalla.screensize(400,800)
pantalla.setworldcoordinates (-150, -150, 350, 300)

tortuga = Turtle()
tortuga.hideturtle()
tortuga.pencolor("red")
tortuga.pensize(5)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.goto(75,75)

tortuga.penup()
tortuga.forward(0)
tortuga.left(5)
tortuga.left(85)
tortuga.forward(0)
tortuga.right (90)
tortuga.pendown()

tortuga.pencolor("blue")
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.goto(0,0)

tortuga.penup()
tortuga.forward(0)
tortuga.left(5)
tortuga.left(85)
tortuga.forward(0)
tortuga.right (90)
tortuga.pendown()

tortuga.pencolor("orange")
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)


tortuga.hideturtle()
tortuga.pendown()

pantalla.exitonclick()
