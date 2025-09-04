# Fazer lista e rotacionar os elementos
# Imprimir antes e depois da rotação

def fazerlista(listanova):
    numero = int(input('Digite um número - 0 para terminar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Digite um número - 0 para terminar: '))
    return listanova


def rotacionarlista(listarot):
    metade = int(len(listarot)/2)
    for i in range(0, metade, 1):
        aux = listarot[i]
        listarot[i] = listarot[len(listarot)-i-1]
        listarot[len(listarot)-i-1] = aux
    return listarot


# Programa Principal
lista = []
lista = fazerlista(lista)
print(lista)
listarotacionada = rotacionarlista(lista)
print(listarotacionada)
