# Separar a lista V em duas
# Lista A com os elementos positivos da lista V
# Lista B com os elementos negativos da lista V
# Variável para guardar os 0's

# Função 1
def fazerlista(listanova):
    numero = int(input('Crie uma lista - digite 100 para encerrar: '))
    while numero != 100:
        listanova.append(numero)
        numero = int(input('Crie uma lista - digite 100 para encerrar: '))


# Função 2
def acharpositivo(listav, listaa2):
    for i in range(len(listav)):
        if listav[i] > 0:
            listaa2.append(listav[i])


# Função 3
def acharnegativo(listav, listab2):
    for i in range(len(listav)):
        if listav[i] < 0:
            listab2.append(listav[i])


# Função 4
def acharnulo(listav, total0):
    for i in range(len(listav)):
        if listav[i] == 0:
            total0 += 1
    return total0


# Programa Principal
x = []
fazerlista(x)
totalzeros = 0
qtdzeros = acharnulo(x, totalzeros)
listaa = []
acharpositivo(x, listaa)
listab = []
acharnegativo(x, listab)
print(x)
print(listaa)
print(listab)
print(qtdzeros)
