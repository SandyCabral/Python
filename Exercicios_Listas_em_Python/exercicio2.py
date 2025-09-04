def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite zero para encerrar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite zero para encerrar: '))


def elementopertence(lista, x):
    achei = False
    for i in range(len(lista)):
        if lista[i] == x:
            achei = True
    return achei


def criarlistadiferenca(listax, listay, listadif):
    for i in range(len(listax)):
        if not elementopertence(listay, listax[i]):
            listadif.append(listax[i])


# Programa Principal
lista1 = []
lista2 = []
listadiferenca = []
fazerlista(lista1)
fazerlista(lista2)
criarlistadiferenca(lista1, lista2, listadiferenca)
print('A lista diferença é =', listadiferenca)
