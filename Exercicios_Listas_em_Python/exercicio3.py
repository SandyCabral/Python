def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite zero para encerrar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite zero para encerrar: '))


def elementopertence(lista, x):
    achei = True
    for i in range(len(lista)):
        if lista[i] == x:
            achei = False
    return achei


def criarlistacomum(listax, listay, listacomum):
    for i in range(len(listax)):
        if not elementopertence(listay, listax[i]):
            listacomum.append(listax[i])


# Programa Principal
lista1 = []
lista2 = []
listacom = []
fazerlista(lista1)
fazerlista(lista2)
criarlistacomum(lista1, lista2, listacom)
print('A lista diferença é =', listacom)
