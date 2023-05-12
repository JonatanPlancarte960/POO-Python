# Crea una clase llamada "Persona" con atributos como nombre, edad y ocupación. 
# Luego, instancia varios objetos de la clase y muestra su información por pantalla.

class Persona():

    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    
    def pantalla(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("Ocupacion: " + self.ocupacion + "\n")

persona1 = Persona("Maria", 32, "Ingeniera")
persona2 = Persona("Alejandro", 45, "Medico")
persona3 = Persona("Sofia", 28, "Diseñadora")

persona1.pantalla()
persona2.pantalla()
persona3.pantalla()