# Crea una clase llamada "Rectángulo" con atributos para almacenar la longitud y el ancho del rectángulo. 
# Añade métodos para calcular el área y el perímetro del rectángulo. 
# Luego, instancia un objeto de la clase y muestra su área y perímetro por pantalla.

class Rectangulo():

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        print("Area: ", str(self.longitud * self.ancho))
    
    def perimetro(self):
        print("Perimetro: ", str(self.longitud * 2 + self.ancho * 2))

rectangulo = Rectangulo(5, 4)

rectangulo.area()
rectangulo.perimetro()