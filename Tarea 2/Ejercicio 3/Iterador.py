# CI-3641 Lenguajes de Programación
# Alumno: Jesus Gutierrez
# Carnet: 20-10332
# Pregunta 3, Inciso c. Iterador que ordena una lista de enteros de menor a mayor. 

def misterio(p):
    if p == []:
        return
    else:
        menor = min(p)
        p.remove(menor)
        yield menor
        for x in misterio(p):
            yield x

for x in misterio([1,3,3,2,1]):
    print(x, end=' ')