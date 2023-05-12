# Crea una clase Persona con los atributos nombre y edad. 
# Luego, crea una subclase llamada Estudiante que herede de Persona y tenga un atributo adicional llamado curso. 
# Agrega métodos a ambas clases para imprimir la información de cada persona.

class Persona:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

class Estudiante(Persona):

    def informacion(self):
        print("Estudiante: ", self.nombre)
        print("Edad: ", self.edad)
        print("Curso: ", self.curso)

persona = Estudiante("Jonatan", 19, "Preparatoria")
persona.informacion()