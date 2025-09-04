# função para remover o primeiro elemento do valor especificado
def removervalor(lis, val):
    removeu = False
    temp = []
    for i in range(len(lis)):
        if lis[i] != val or removeu:
            temp.append(lis[i])
        else:
            removeu = True
    return temp


# programa principal
lista = [1, 4, 5, 6, 4, 7, 7]
valor = int(input('Digite um valor a ser removido: '))
# excluir o valor especificado em sua primeira aparição
lista = removervalor(lista, valor)
print(lista)
