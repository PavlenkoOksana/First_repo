# !/usr/bin/python3
import math
from tkinter import *
root = Tk()

xn = 750
yn = 750
step = 50
xlc = ((xn/step)%2)*step/2
ylc = ((yn/step)%2)*step/2


c = Canvas(root, width=xn+10, height=yn+10, bg='white') # Размер и цвет холста
c.pack()


# Вісь X
c.create_line(0, yn/2, xn, yn/2, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='#AA0000',
                arrowshape="10 20 10")

# Вісь Y
c.create_line( xn/2, yn, xn/2, 3, fill='gray',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

# Проміжні лінії
for i in range(max(int(xn/step),int(yn/step))):
    c.create_line(0, i*step+ylc, yn, i*step+ylc)
    c.create_line(i*step+xlc, 0, i*step+xlc, yn)

# Підпис координат
for y in range(max(int(xn/step),int(yn/step))):
    for x in range(int(xn/step)):
        c.create_text(xn+22+(x-int(xn/step))*step+xlc, 0+yn-10+(y-int(yn/step))*step+ylc, text=f"({x-int(xn/step/2)};{-y+int(yn/step/2)})",
                    justify=LEFT, font="Verdana 8")

# Функція для малювання вектору
def vector(x1,y1,x2,y2):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    
def vector_calc(x1,y1,x2,y2):
    #Малюємо вектор
    vector(x1,y1,x2,y2)
    #Створюємо прямокутник-підкладку під текст
    c.create_rectangle(xn-350, yn-20, xn, yn,outline="#fb0",fill="#ddd")
    # Робимо обрахунки
    modulo = math.sqrt((x2-x1)**2+(y2-y1)**2)
    cos_a = (x2-x1)/modulo
    cos_b = (y2-y1)/modulo
    # Виводимо текст на прямокутник-підкладку
    c.create_text(xn-350, yn, text=f"|a| = {format(modulo, '.3f')}, cos_a = {format(cos_a, '.3f')}, cos_b = {format(cos_b, '.3f')}",
                    anchor=SW, font="Verdana 8")

def vector_minus(x1,y1,x2,y2,x3,y3,x4,y4):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    c.create_line(xn/2+x3*step, yn/2-y3*step, xn/2+x4*step, yn/2-y4*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    c.create_line(xn/2+x4*step, yn/2-y4*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    
def vector_mult(x1,y1,x2,y2,n):
    c.create_line(xn/2+x1*step, yn/2-y1*step, xn/2+x2*step, yn/2-y2*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    c.create_line(xn/2+x1*n*step, yn/2-y1*n*step, xn/2+x2*n*step, yn/2-y2*n*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
def cos_fi(x3,y3,x4,y4,x5,y5,x6,y6):
    c.create_line(xn/2+x3*step, yn/2-y3*step, xn/2+x4*step, yn/2-y4*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    c.create_line(xn/2+x5*step, yn/2-y5*step, xn/2+x6*step, yn/2-y6*step, fill='black',
                width=5, arrow=LAST,
                activefill='blue',
                arrowshape="10 20 10")
    c.create_rectangle(xn-700, yn-50, xn, yn,outline="#fb0",fill="#ddd")
    x1 = x4-x3
    y1 = y4-y3
    x2 = x6-x5
    y2 = y6-y5
    # Робимо обрахунки
    sd = x1*x2+y1*y2
    d = ((x4-x3)**2+(y4-y3)**2)**0.5
    cos_fi = (x1*x2 + y1*y2)/(((x1**2+y1**2))**0.5*((x2**2+y2**2)**0.5))
    fi = math.acos (cos_fi)
    fi_g = fi *(180/math.pi)
    # Виводимо текст на прямокутник-підкладку
    c.create_text(xn-350, yn, text=f"сд = {sd}, Відстань = {format(d, '.3f')}, cos_fi = {format(cos_fi, '.3f')}, fi = {format(fi, '.3f')} рад, fi = {format(fi_g, '.3f')} град", font="Verdana 8")
    