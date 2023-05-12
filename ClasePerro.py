# Crea una clase llamada "Perro" con atributos como nombre, raza y edad. 
# Añade un método para ladrar, que imprima "¡Guau!" por pantalla. 
# Luego, instancia varios objetos de la clase y llama al método de ladrido para cada uno de ellos.

class Perro():

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def pantalla(self):
        print("Nombre: " + self.nombre)
        print("Raza: " + self.raza)
        print("Edad: " + self.edad)
    
    def ladrar(self):
        print("¡Guau! \n")

perro1 = Perro("Max", "Labrador", "4 años")
perro2 = Perro("Luna", "Bulldog", "2 años")
perro3 = Perro("Rocky", "Pastor Aleman", "6 años")

perro1.pantalla()
perro1.ladrar()

perro2.pantalla()
perro2.ladrar()

perro3.pantalla()
perro3.ladrar()