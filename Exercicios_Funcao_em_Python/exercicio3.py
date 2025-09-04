# excluir elemento em determinada posição
def excluirelemento(lis, pos):
    temp = []
    elementoretirado = 0
    for i in range(len(lis)):
        if i != pos:
            temp.append(lis[i])
        else:
            elementoretirado = lis[i]
    return temp, elementoretirado


# Programa principal
lista = [1, 2, 3, 4]
posicao = int(input('Digite a posição do valor a ser removido: '))
lista, elemento_retirado = excluirelemento(lista, posicao)
print(lista)
print(elemento_retirado)
