from turtle import Screen, Turtle
#forward avanza de pasos
#backward retrosede pasos
#left gira a la izquierda
#rigth gira a la derecha 
# penup levanta el lapiz
# pendown baja el lapiz

pantalla = Screen()
pantalla.setup(825,445)
pantalla.screensize(400,800)

tortuga = Turtle()
tortuga.hideturtle()
tortuga.pensize(5)
tortuga.forward(200)
tortuga.left(120)
tortuga.forward(200)
tortuga.left(120)
tortuga.forward(200)
tortuga.left(120)

tortuga.penup()
tortuga.forward(50)
tortuga.left(5)
tortuga.left(85)
tortuga.forward(15)
tortuga.right (90)
tortuga.pendown()

tortuga.forward(150)
tortuga.left(120)
tortuga.forward(150)
tortuga.left(120)
tortuga.forward(150)
tortuga.left(120)

tortuga.penup()
tortuga.forward(50)
tortuga.left(5)
tortuga.left(85)
tortuga.forward(25)
tortuga.right (90)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)
tortuga.forward(100)
tortuga.left(120)

tortuga.penup()
tortuga.forward(20)
tortuga.left(5)
tortuga.left(85)
tortuga.forward(10)
tortuga.right (90)
tortuga.pendown()

tortuga.forward(80)
tortuga.left(120)
tortuga.forward(80)
tortuga.left(120)
tortuga.forward(80)
tortuga.left(120)

tortuga.hideturtle()
tortuga.pendown()

pantalla.exitonclick()
