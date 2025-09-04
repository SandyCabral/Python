# Ler uma lista V que representa um vetor
# Gerar um novo vetor que represente a multiplicação por um escalar
# Imprimir os vetores e o valor escalar


def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite 0 para encerrar: '))
    while numero != 0:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite 0 para encerrar: '))
    return listanova


def multiplicarvetorporescalar(vetor, escalar):
    resultado = []
    for i in range(len(vetor)):
        produto = vetor[i] * escalar
        resultado.append(produto)
    return resultado


# Programa Principal
lista = []
lista = fazerlista(lista)
print(lista)
fator = int(input('Digite o valor do escalar: '))
produtovetorescalar = multiplicarvetorporescalar(lista, fator)
print(fator)
print(produtovetorescalar)
