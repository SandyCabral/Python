# Ler duas listas U e Y que representam vetores
# Somar U e Y e gerar um novo vetor que represente essa soma
# Imprimir os 3 vetores


def fazerlista(listanova):
    numero = int(input('Digite um número - 0 para terminar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Digite um número - 0 para terminar: '))
    return listanova


def somadevetores(lista1, lista2):
    listasoma = []
    for i in range(len(lista1)):
        soma = lista1[i] + lista2[i]
        listasoma.append(soma)
    return listasoma


# Programa Principal
listaU = []
listaY = []
listaU = fazerlista(listaU)
listaY = fazerlista(listaY)
somadosvetores = somadevetores(listaY, listaU)
print(listaU)
print(listaY)
print(somadosvetores)
