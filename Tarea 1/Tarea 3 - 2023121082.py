##Tarea 3 - Alejandro Méndez Arias 2023121082

import time

from turtle import*
import turtle
drawing_area = turtle.Screen()
drawing_area.setup(width=1.0, height=1.0)
t = turtle.Turtle()

def menu():
    opp = 1
    while(opp != 0):
        print("¡Bienvenid@ al programa que realiza figuras geometricas!")
        print("Escoja una entre las siguientes opciones para empezar dibujo en turtle:")
        print("1. Escoger el tipo de figuras geometricas")
        print("2. Salir")
        op = int(input("Digite una de las opciones: "))
        print("")
        if op == 1:
            fig()
            opp -= 1
        elif op == 2:
            opp -= 1
        else:
            print("Opción incorrecta")
    return

def fig():
    t.penup()
    t.rt(180)
    t.fd(300)
    t.rt(180)
    print("Escoja 3 de las siguientes opciones de figuras geometricas:")
    print("1. Circulo")
    print("2. Cuadrado")
    print("3. Triangulo equilatero")
    print("4. Pentagono regular")
    print("5. Hexagono regular")
    f1 = int(input("Ingrese el número de su primer figura: "))
    f2 = int(input("Ingrese el número de su segunda figura: "))
    f3 = int(input("Ingrese el número de su tercer figura: "))
    print("Espere un momento para procesar los datos")
    time.sleep(2)
    print("")
    print("Las longitudes o radios no pueden exceder los 5 cm, si se excede no se ve en su totalidad")
    L1 = int(input("Ingrese la longitud del lado (o radio si es un circulo) en cm de su primer figura: "))
    L2 = int(input("Ingrese la longitud del lado (o radio si es un circulo) en cm de su segunda figura: "))
    L3 = int(input("Ingrese la longitud del lado (o radio si es un circulo) en cm de su tercer figura: "))
    print("Espere un momento para procesar los datos")
    time.sleep(2)
    print("")
    print("Finalmente, escoja un color para c/u de sus figuras respectivamente de la siguiente lista:")
    print("1. Rojo")
    print("2. Azul")
    print("3. Amarillo")
    print("4. Verde")
    print("5. Rosa")
    print("6. Morado")
    c1 = int(input("Ingrese el número del color para su primer figura: "))
    c2 = int(input("Ingrese el número del color para su segunda figura: "))
    c3 = int(input("Ingrese el número del color para su tercer figura: "))
    print("Espere un momento para procesar los datos")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("Dando ultimos retoques a sus bellas figuras")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("¡Listo! Puede revisar el lienzo de Turtle.")
    ##Inicio F1
    if f1 == 1: ##Circulo F1/INICIO
        Lpx = L1 * 38
        if c1 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c1 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c1 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c1 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c1 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c1 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        ##Circulo F1/FIN
        
    elif f1 == 2: ##Cuadrado F1/INICIO
        Lpx = L1 * 38
        if c1 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c1 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c1 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c1 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c1 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c1 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        ##Cuadrado F1/FIN
            
    elif f1 == 3: ##Triangulo F1/INICIO
        if c1 == 2: ##Color rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c1 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c1 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c1 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c1 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c1 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        ##Triangulo F1/FIN
        
    elif f1 == 4: ##Pentagono F1/INICIO
        Lpx = L1 * 38
        if c1 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c1 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c1 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c1 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c1 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c1 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
            ##Pentagono F1/FIN
            
    elif f1 == 5: ##Hexagono F1/INICIO
        Lpx = L1 * 38
        if c1 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c1 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c1 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c1 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c1 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c1 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
            ##Hexagono F1/FIN
    else:
        print("No se escogió ninguna opción valida para su primer figura")
    ##Fin F1

    ##Inicio F2
    if f2 == 1: ##Circulo F2/INICIO
        Lpx = L2 * 38
        spf2 = L1 * 38 + 200
        sub = L1 * 38
        t.fd(spf2)
        t.rt(90)
        t.fd(sub)
        if c2 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c2 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c2 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c2 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c2 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c2 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        ##Circulo F2/FIN
        
    elif f2 == 2: ##Cuadrado F2/INICIO
        Lpx = L2 * 38
        spf2 = L1 * 38 + 200
        sub = L1 * 38
        t.fd(spf2)
        t.rt(90)
        t.fd(sub)
        if c2 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c2 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c2 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c2 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c2 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c2 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        ##Cuadrado F2/FIN
            
    elif f2 == 3: ##Triangulo F2/INICIO
        Lpx = L2 * 38
        spf2 = L1 * 38 + 200
        sub = L1 * 38
        t.fd(spf2)
        t.rt(90)
        t.fd(sub)
        if c2 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c2 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c2 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c2 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c2 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c2 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        ##Triangulo F2/FIN
        
    elif f2 == 4: ##Pentagono F2/INICIO
        Lpx = L2 * 38
        spf2 = L1 * 38 + 200
        sub = L1 * 38
        t.fd(spf2)
        t.rt(90)
        t.fd(sub)
        if c2 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c2 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c2 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c2 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c2 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c2 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
            ##Pentagono F2/FIN
            
    elif f2 == 5: ##Hexagono F2/INICIO
        Lpx = L2 * 38
        spf2 = L1 * 38 + 200
        sub = L1 * 38
        t.fd(spf2)
        t.rt(90)
        t.fd(sub)
        if c2 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c2 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c2 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c2 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c2 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c2 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
            ##Hexagono F2/FIN
    else:
        print("No se escogió ninguna opción valida para su segunda figura")
    ##Fin F2

    ##Inicio F3
    if f3 == 1: ##Circulo F3/INICIO
        Lpx = L3 * 38
        spf3 = L1 * 38 + 200
        t.rt(180)
        t.fd(spf3)
        t.rt(180)
        if c3 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c3 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c3 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c3 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c3 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        elif c3 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            t.circle(Lpx)
            t.penup()
            t.end_fill()
        ##Circulo F3/FIN
        
    elif f3 == 2: ##Cuadrado F3/INICIO
        Lpx = L3 * 38
        spf3 = L1 * 38 + 200
        t.rt(180)
        t.fd(spf3)
        t.rt(180)
        if c3 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c3 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c3 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c3 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c3 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        elif c3 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(Lpx)
                t.rt(90)
            t.penup()
            t.end_fill()
        ##Cuadrado F3/FIN
            
    elif f3 == 3: ##Triangulo F3/INICIO
        Lpx = L3 * 38
        spf3 = L1 * 38 + 200
        t.rt(180)
        t.fd(spf3)
        t.rt(180)
        if c3 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c3 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c3 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c3 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c3 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        elif c3 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(Lpx)
                t.rt(120)
            t.penup()
            t.end_fill()
        ##Triangulo F3/FIN
        
    elif f3 == 4: ##Pentagono F3/INICIO
        Lpx = L3 * 38
        spf3 = L1 * 38 + 200
        t.rt(180)
        t.fd(spf3)
        t.rt(180)
        if c3 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c3 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c3 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c3 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c3 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
        elif c3 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(5):
                t.fd(Lpx)
                t.rt(72)
            t.penup()
            t.end_fill()
            ##Pentagono F3/FIN
            
    elif f3 == 5: ##Hexagono F3/INICIO
        Lpx = L3 * 38
        spf3 = L1 * 38 + 200
        t.rt(180)
        t.fd(spf3)
        t.rt(180)
        if c3 == 1: ##Color Rojo
            t.fillcolor("red")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c3 == 2: ##Color azul
            t.fillcolor("blue")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c3 == 3: ##Color amarrillo
            t.fillcolor("yellow")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c3 == 4: ##Color verde
            t.fillcolor("green")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c3 == 5: ##Color rosa
            t.fillcolor("pink")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
        elif c3 == 6: ##Color morado
            t.fillcolor("purple")
            t.pendown()
            t.begin_fill()
            for i in range(6):
                t.fd(Lpx)
                t.rt(60)
            t.penup()
            t.end_fill()
            ##Hexagono F3/FIN
    else:
        print("No se escogió ninguna opción valida para su tercer figura")
    ##Fin F3

    return
