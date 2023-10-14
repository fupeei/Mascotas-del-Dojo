
class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energía):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energía

    def dormir(self):
        self.energia += 25
        print(f"La energia de {self.name} a aumentado a {self.energia}")
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f"La salud de {self.name} a aumentado a {self.salud}")
        print(f"La energia de {self.name} a aumentado a {self.energia}")
    
    def jugar(self):
        self.salud += 5
        self.energia -= 5
        print(f"La salud de {self.name} a aumentado a {self.salud}")
        print(f"La energia de {self.name} a bajado a {self.energia}")
    
    def ruido(self):
        print(f"{self.name}: Guau! Guau! Guau!")


