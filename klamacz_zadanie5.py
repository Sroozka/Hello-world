#!/usr/bin/env python3
"""
https://www.kodolamacz.pl/blog/wyzwanie-python-5-zaawansowane-aspekty-programowania-obiektowego/
Stwórz hierarchię klas reprezentujących figury geometryczne. Każda figura powinna umieć wypisać informacje o sobie,
a także obliczyć swój obwód i pole. W grę niech wchodzą koła, prostokąty, kwadraty oraz trójkąty.
Czy prostokąt i kwadrat mogą być połączone relacją dziedziczenia?
"""
#stworzyc klasy prywatne,
class Figure:
    def __init__(self):
       pass
    v_side = 10
    
    def Circumference(self):
        return 2*3.14*self.ray

    def Area(self):
        return 3.14*self.ray**2

class Circle(Figure):
    def __init__(self, ray=10):
        self.ray = ray
        print("Circle ray 0<R<=100")
        if self.ray <= 0 or self.ray>100 : self.ray = 10

class Triangle(Figure):
    def __init__(self, a=5, b=5, c=5):
        self.a = a
        self.b = b
        self.c = c
        if self.a <= 0: self.a = 10
        if self.b <= 0: self.a = 10
        if self.c <= 0: self.a = 10
    O = super().a

class Rectangle(Figure):
    pass

class Square(Rectangle):
    pass

def Area_Figures(figures):
    for figure in figures:
        print(figure.Area)
        print(figure.O)

def main():
    circle = Circle(10)
    triangle = Triangle()
    rectangle = Rectangle()
    square = Square()
    figures = [circle, triangle, rectangle, square]
    Area_Figures(figures)

if __name__ == "__main__":
    main()
