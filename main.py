def soma(numero1, numero2):
    print(f'RESULTADO: {numero1} + {numero2} = ', numero1+numero2)


def subtracao(numero1, numero2):
    print(f'RESULTADO: {numero1} - {numero2} = ', numero1-numero2)


def multiplicacao(numero1, numero2):
    print(f'RESULTADO: {numero1} * {numero2} = ', numero1*numero2)

def divisao(numero1, numero2):
    try:
        print(f'RESULTADO: {numero1} / {numero2} = ', numero1/numero2)
    except ZeroDivisionError:
        print('Não é possivel divisao por zero.')

def imprimir_menu():
    print('==================================================')
    print('                     BEM-VINDO                    ')
    print('==================================================')
    print('[1] - SOMA                 ')
    print('[2] - SUBTRAÇÃO            ')
    print('[3] - MULTIPLICAÇÃO        ')
    print('[4] - DIVISÃO              ')
    print('[0] - FINALIZAR O PROGRAMA ')
    print('==================================================')

while True:
    imprimir_menu()
    print()
    opcao = input('ENTRE COM UMA DAS OPÇÕES : ')
    print()
    if opcao == '1':
        numero1 = float(input('Entre com numero 1: '))
        numero2 = float(input('Entre com numero 2: '))
        soma(numero1, numero2)
    elif opcao == '2':
        numero1 = float(input('Entre com numero 1: '))
        numero2 = float(input('Entre com numero 2: '))
        subtracao(numero1, numero2)
    elif opcao == '3':
        numero1 = float(input('Entre com numero 1: '))
        numero2 = float(input('Entre com numero 2: '))
        multiplicacao(numero1, numero2)
    elif opcao == '4':
        numero1 = float(input('Entre com numero 1: '))
        numero2 = float(input('Entre com numero 2: '))
        divisao(numero1, numero2)
    elif opcao == '0':
        print('>>>>> Finalizando Programa.... <<<<<')
        break
    else:
        print('Opção Inválida')
