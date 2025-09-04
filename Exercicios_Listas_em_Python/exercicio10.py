# Ler um arquivo txt com valores reais (float) que represente saques
# Armazená-los em uma lista chamada movimento
# Apresentar um menu de acordo com o exercício
# Ao escolher a opção 1, inserir valor positivo e inseri-lo em movimento
# Ao escolher opção 2, inserir valor negativo e inseri-lo em movimento
# Ao escolher opção 3, imprimir o somatório dos valores
# Ao escolher opção 4, finalizar programa

def menu():
    print('********** MENU **********')
    print('1 - Efetuar depósito;\n2 - Efetuar saque;\n3 - Consultar saldos;\n4 - Finalizar programa.')
    print('**************************')


movimento = []
arquivo = open('arquivoexercicio10', 'r', encoding='utf-8')
extrato = arquivo.read()
valor = extrato.split(';')
for i in range(len(valor)):
    valorreal = float(valor[i])
    movimento.append(valorreal)
# print(extrato)
# print(valor)
# print(movimento)
menu()
opcao = input('Escolha a opção desejada: ')
if opcao not in '1234':
    print('Selecionar opção de 1 a 4!')
elif opcao == '4':
    print('Fim')
else:
    while opcao in '123':
        if opcao == '1':
            deposito = float(input('Digite o valor do depósito: '))
            if deposito < 0:
                print('O valor deve ser positivo.')
            else:
                movimento.append(deposito)
        elif opcao == '2':
            saque = float(input('Digite o valor do saque: '))
            if saque > 0:
                print('O valor do saque deve ser negativo.')
            else:
                movimento.append(saque)
        elif opcao == '3':
            soma = 0
            for i in range(len(movimento)):
                soma += movimento[i]
            print('O saldo é de: ', soma, 'reais')
        menu()
        opcao = input('Escolha a opção desejada: ')
