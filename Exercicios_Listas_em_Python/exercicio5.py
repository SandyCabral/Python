def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite zero para encerrar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite zero para encerrar: '))


def somarnumerospares(listapar):
    somapar = 0
    for i in range(len(listapar)):
        if listapar[i] % 2 == 0:
            somapar += listapar[i]
    return somapar


def somarnumerosimpares(listaimpar):
    somaimpar = 0
    for i in range(len(listaimpar)):
        if listaimpar[i] % 2 != 0:
            somaimpar += listaimpar[i]
    return somaimpar


def somasiguais(somaimpar, somapar):
    igual = False
    if somaimpar == somapar:
        igual = True
    return igual


# Programa Principal
lista1 = []
fazerlista(lista1)
pares = somarnumerospares(lista1)
impares = somarnumerosimpares(lista1)
somasiguais = somasiguais(impares, pares)
print('Soma ', somasiguais)
