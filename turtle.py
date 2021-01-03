from turtle import *

screen = Screen()

screen.setup(500, 500)


move=Turtle()

L=[]
for x in range (12):
    fila=[]
    for y in range(12):
        fila.append(1)
    L.append(fila)



print L

def kl():
  move.forward(10)

def k2():
  move.left(45)

def k3():
  move.right(45)

def k4():
  move.backward(10)
  
screen.onkey(kl, "Up")
screen.onkey(k2,"Left")
screen.onkey(k3,"A")
screen.onkey(k4,"S")


screen.listen()

screen.exitonclick()


def cuadrado(x,y,relleno,lado):
    tracer(0,0)
    hideturtle()
    if relleno:
        color("black", "black")
        begin_fill()
    penup()
    goto(x,y)
    pendown()
    forward(lado)
    left(90)
    forward(lado)
    left(90)
    forward(lado)
    left(90)
    forward(lado)
    if relleno:
        end_fill()
    update()
    done()


def tablero(tamano): #x.y
    tablero=[]
    #generar laberinto
    for i in range(tamano):
        columna=[]
        for j in range(tamano):
            columna.append("1")
    
        tablero.append(columna)
    #mostrar laberinto
    for i in range(tamano):
        for j in range(tamano):
            if tablero[i][j]=="1":
                cuadrado((i * 10),(j*10),True,10)

    done()