def recursiva(vector, buscado):
    if len(vector) == 0:
        return 0
    elif vector[0] == buscado:
        return 1 + recursiva(vector[1:], buscado)
    else:
        return 0 + recursiva(vector[1:], buscado)


print(recursiva(["pato", "naranja", "pato"], "naranja"))
