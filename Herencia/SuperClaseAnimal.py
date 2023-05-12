# Crea una clase Animal con los atributos nombre y edad. 
# Luego, crea subclases como Perro, Gato y Pajaro que hereden de Animal. 
# Agrega métodos adicionales a las subclases para mostrar el sonido característico de cada animal.

class Animal:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Perro(Animal):

    def sonido_perro(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("¡Guau! ¡Guau!\n")

class Gato(Animal):

    def sonido_gato(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Miau Miau\n")

class Pajaro(Animal):

    def sonido_pajaro(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Pio Pio\n")

perro = Perro("Max", 4)
gato = Gato("Luna" , 3)
pajaro = Pajaro("Kiwi", 2)

perro.sonido_perro()
gato.sonido_gato()
pajaro.sonido_pajaro()
