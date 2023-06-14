from Pila import Pila


class Mision():
    def __init__(self, planeta, captura, costo):
        self.planeta = planeta
        self.captura = captura
        self.costo = costo

    def __str__(self):
        return f'Mision: {self.planeta}.{self.captura}.{self.costo}'

    def get_(self):
        return self.planeta

    def get_captura(self):
        return self.captura

    def get_costo(self):
        return self.costo


pilaMisiones = Pila()

pilaAux = Pila()

for index in range(0, pilaMisiones.size()):
    mision = pilaMisiones.pop()
    pilaAux.push(mision)
for index in range(0, pilaAux.size()):
    misionAux = pilaAux.pop()
    print(
        f'El orden de los planetas en el que hizo las misiones es {misionAux.get_planeta}')

ac_costo = 0
for index in range(0, pilaMisiones.size()):
    mision = pilaMisiones.pop()
    ac_costo = ac_costo + mision.get_costo()

for index in range(0, pilaAux.size()):
    mision = pilaAux.pop()
    if mision.get_captura() == "Han Solo":
        print(
            f'El numero de la mision es {index + 1} en el planeta {mision.get_planeta()}')
