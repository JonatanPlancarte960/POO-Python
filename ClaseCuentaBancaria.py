# Crea una clase llamada "CuentaBancaria" con atributos para almacenar el número de cuenta y el saldo. 
# Añade métodos para depositar dinero, retirar dinero y mostrar el saldo actual. 
# Prueba diferentes operaciones utilizando objetos de la clase.

import os

class CuentaBancaria():
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def deposito(self):
        os.system('cls')
        print("-----------------Cajero X-----------------")
        deposito = float((input("¿Cuanto dinero desea depositar? ")))
        print("Saldo Actual: ", self.saldo + deposito)

    def retirar(self):
        os.system('cls')
        print("-----------------Cajero X-----------------")
        retiro = float((input("¿Cuanto dinero desea retirar? ")))
        if retiro <= self.saldo:
            print("Saldo Actual: ", float(self.saldo - retiro))
        else:
            print("Fondos insuficientes")
    
    def saldo_actual(self):
        os.system('cls')
        print("-----------------Cajero X-----------------")
        print("Saldo Actual: ", float(self.saldo))

print("-----------------Cajero X-----------------")
num_cuenta = int(input("Ingrese su numero de cuenta: "))
nip = int(input("Ingrese su NIP: "))
print("Exito")
input("Enter para continuar... ")
os.system('cls')

cuenta = CuentaBancaria(num_cuenta, 5000)

print("-----------------Cajero X-----------------")
usuario = int(input("1) Deposito \n" + "2) Retiro \n" + "3) Saldo \n" + "Ingrese el numero de opcion que desea: "))
if usuario == 1:
    cuenta.deposito()
elif usuario == 2:
    cuenta.retirar()
elif usuario == 3:
    cuenta.saldo_actual()