def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite zero para encerrar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite zero para encerrar: '))


def fatorial(x):
    fat = 1
    for i in range(2, x+1, 1):
        fat = fat * i
    return fat


def listafatorial(listax, listay):
    for i in range(len(listax)):
        fat = fatorial(listax[i])
        listay.append(fat)


# Programa Principal
lista1 = []
lista2 = []
fazerlista(lista1)
listafatorial(lista1, lista2)
print(lista1)
print(lista2)
