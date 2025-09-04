def fazerlista(lista1):
    numero = int(input('Digite um número - zero para encerrar: '))
    while numero != 0:
        lista1.append(numero)
        numero = int(input('Digite um número - zero para encerrar: '))
    return lista1


def somatorio(lista2):
    soma1 = 0
    for i in range(1, len(lista2), 1):
        soma1 += i / lista2[i]
    return soma1


def numeradormenor(lista3):
    numerador_menor = 0
    for i in range(1, len(lista3), 1):
        numerador = i
        denominador = lista3[i]
        if numerador < denominador:
            numerador_menor += 1
    return numerador_menor


# Programa principal
listaPrincipal = []
lista = fazerlista(listaPrincipal)
soma = somatorio(listaPrincipal)
numeradormenor = numeradormenor(listaPrincipal)
print(numeradormenor)
print(listaPrincipal)
print(soma)
