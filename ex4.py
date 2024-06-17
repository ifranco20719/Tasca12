class Jugador():
    def __init__(self, atribut, edat, equip, nombre):
        self.atribut = atribut
        self.edat = edat
        self.equip = equip
        self.nombre = nombre

    def xerrar(self):
        pass

    def quisoc(self):
        print(f"Sóc un jugador de futbol de'l equip {self.equip} i porto el nombre {self.nombre}")


class Jugadorfutbol(Jugador):
    def __init__(self, nom, atribut, edat, equip, nombre, age, number):
        super().__init__(atribut, edat, equip, nombre)  # Call the parent constructor
        self.nom = nom
        self.age = age
        self.number = number

    def xerrar(self):
        print(f"{self.nom} diu: Hola!")

    def quisoc(self):
        print(f"{self.nom} diu: Sóc un jugador de futbol de'l equip {self.equip} i porto el nombre {self.number}")


class Equip():
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


class Miami(Equip):
    def __init__(self):
        super().__init__("Miami")


class RealMadrid(Equip):
    def __init__(self):
        super().__init__("Real Madrid")


class Betis(Equip):
    def __init__(self):
        super().__init__("Betis")

def pex4():
    players = [Jugadorfutbol("Messi","Lionel","36","Miami","10",36,10), Jugadorfutbol("Bellingham","Jude","20","RealMadrid","5",20,5), Jugadorfutbol("Isco","Alarcon","32","Betis","22",32,22)]
    for Jugador in players:
        Jugador.xerrar()
        Jugador.quisoc()
