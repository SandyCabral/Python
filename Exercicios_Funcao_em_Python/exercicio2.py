# função para achar a posição do valor fornecido ou retornar -1, caso não tenha esse valor
def acharvalor(lis, val):
    pos = -1
    for i in range(len(lis)):
        if lis[i] == val:
            pos = i
    return pos


# programa principal
lista = [1, 2, 10, 5, 20]
valor = int(input('Digite um valor para achar sua posição: '))
posicao = acharvalor(lista, valor)
print('A posição de', valor,'na lista é:', posicao)
