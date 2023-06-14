from Lista import Lista
from Cola import Cola


class Personajes():
    def __init__(self, pj, nombre, grupo, anio):
        self.pj = pj
        self.nombre = nombre
        self.grupo = grupo
        self.anio = anio

    def get_pj(self):
        return self.pj

    def get_nombre(self):
        return self.nombre

    def get_grupo(self):
        return self.grupo

    def get_anio(self):
        return self.anio

    def __str__(
        self): return f'{self.pj}-{self.nombre}-{self.grupo}-{self.anio}'


listaAvengers = Lista()
personajes = [
    Personajes("Black Widow", "Natasha Romanoff", "Avengers", "1964"),
    Personajes("Black Panther", "Black Panther", "Black Panther", "1966"),
    Personajes("Capitana Marvel", "Carol Danvers", "Avengers", "1968"),
    Personajes("Doctor Strange", "Stephen Strange",
               "Masters of the Mystic Arts", "1963"),
    Personajes("Falcon", "Sam Wilson", "Avengers", "1969"),
    Personajes("Loki", "Loki Laufeyson", " Villains/Revengers ", "1962"),
    Personajes("Scarlet Witch", "Wanda Maximoff", "Avengers", "1964"),
    Personajes("Winter Soldier", "Bucky Barnes", "Avengers", "1941"),
    Personajes("Hulk", "Bruce Banner", "Avengers", "1962"),
    Personajes("Ant-Man", "Scott Lang", "Avengers", "1979"),
    Personajes("Doctor Doom", "Victor von Doom", "Masters of Evil", "1962"),
    Personajes("Wolverine", "Logan/James Howlett", "X-Men", "1974"),
    Personajes("Ghost Rider", "Johnny Blaze",
               "Champions of Los Angeles", "1972"),
    Personajes("Spider-Woman", "Jessica Drew", "Avengers ", "1977"),
    Personajes("Gamora ", "Gamora Zen Whoberi Ben Titan",
               "Guardianes de la Galaxia", "1975"),
    Personajes("Iron Man", "Tony Stark", "Avengers", "1963"),
    Personajes("Deadpool", "Wade Wilson", "X-Men/Thunderbolts", "1991"),
    Personajes("Vision", "Vision", "Avengers", " 1968"),
    Personajes("Spider-Man", "Peter Parker", " Avengers", "1962"),
    Personajes("Thor", "Thor Odinson", "Avengers", "1962"),
]

for personaje in personajes:
    listaAvengers.insert(personaje, "pj")

"""Punto 2 Ejercicio a"""

listaAvengers.order_by("nombre")
index = listaAvengers.search("Capitana Marvel", "nombre")
if index != None:
    print(f'El nombre de personaje de Capitana Marvel es {personaje.get_pj}')

"""ejercicio b"""
colaPersonajes = Cola()
for index in range(0, listaAvengers.size()):
    personaje = listaAvengers.get_element_by_index(index)
    if personaje.get_grupo() == "Guardianes de la galaxia":
        colaPersonajes.arrive(personaje)
print(
    f'Los personajes que pertenecenm al grupo Guardianes de la Galaxia son: {colaPersonajes.size()}')

"""ejercicio d"""
for index in range(0, listaAvengers.size()):
    personaje = listaAvengers.get_element_by_index(index)
    if personaje.get_anio() > "1960" and personaje.get_pj() != None:
        print(personaje)

"""ejercicio g"""
for index in range(0, listaAvengers.size()):
    personaje = listaAvengers.get_element_by_index(index)
    if personaje.get_pj()[0] == "C" or personaje.get_pj()[0] == "P" or personaje.get_pj()[0] == "S":
        print(personaje)

"""ejercicio e"""
listaAvengers.order_by('pj')
index = listaAvengers.search("Vlanck Widow", "pj")
if index != None:
    listaAvengers.set_value("Vlanck Widow", "Black Widow", "pj")

"""ejercicio f """
listaAux = Lista()
pj_aux = [
    Personajes("Black Cat", "Juan Gonzalez", "Avengers", "1978"),
    Personajes("Hulk", "Brian Riquelme", "Avengers", "1967"),
    Personajes("Rocket Racoon", "Ricardo Funes",
               "Guardianes de la Galaxia", "1930"),
    Personajes("Loki", "Loki Laufeyson", "Avengers", "1954"),
]
for personaje in pj_aux:
    listaAux.insert(personaje, "pj")

listaAvengers.order_by('pj')

for index in range(0, listaAux.size()):
    personaje = listaAux.get_element_by_index(index)
    index = listaAvengers.search(personaje.get_pj(), "pj")
    if index == None:
        listaAvengers.insert(personaje, "pj")
