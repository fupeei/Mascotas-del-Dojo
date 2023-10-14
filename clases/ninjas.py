from mascotas import Mascota
class Ninja:
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascota = comida_mascota

    def caminar(self):
        print(f"El ninja {self.nombre} pasea a {self.mascotas.name}")
        self.mascotas.jugar()

    def alimentar(self):
        print(f"El ninja {self.nombre} esta alimentando a {self.mascotas.name}...")
        self.mascotas.comer()
    
    def bañar(self):
        print(f"El ninja {self.nombre} esta bañando a {self.mascotas.name} ...")
        self.mascotas.ruido()

mascota1 = Mascota("Martina", "Perro", "Galletitas de perro", 10, 50)
ninja1 = Ninja("Chris", "Aguilera", mascota1, "CARNE", "champeon dog")

ninja1.caminar()
print("-----------")
ninja1.alimentar()
print("-----------")
ninja1.bañar()









