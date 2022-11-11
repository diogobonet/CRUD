import cadastroprodutos
import clientes
import loja
from clientes import CorVerde, print_cor


def LerInt(msg):
    ok = False
    valor = 0
    while True:
        op = str(input(msg))
        if op.isnumeric():
            valor = int(op)
            ok = True
        else:
            print('\033[0;31mERRO, digite uma opção válida\033[m')
        if ok:
            break
    return valor 


def menuPrincipal():
    print('\n\033[0;33m[ 1 ] Menu | Clientes')
    print('[ 2 ] Menu | Cadastro de jogos')
    print('[ 3 ] Menu | Compra de jogos')
    print('\033[31m[ 4 ] Sair')
    while True:
        op = LerInt('\033[0;32m-> ')
        if op == 1:
            clientes.menuClientes()
        if op == 2:
            cadastroprodutos.menuProd()
        if op == 3:
            loja.menuLoja()
        if op == 4:
            break
        if op < 1 or op > 4:
            print('\033[0;31mAs opções do menu são apenas de 1 à 4!\033[m')
        else:
            print('\nValor inválido! Tente novamente:')
    print('Saindo...')


def menutopo():
    print('\033[0;97m='*75)
    print_cor('                         [Nós Somos do Rock 🤟]\n', CorVerde)
    print("                   \033[0;36m          [🦇 Osbourne 🦇]\n  ")
    print('\033[0;35mAndré Akim; \033[0;97mDiogo Bonet; \033[0;35mEduardo Mussi; \033[0;97mGabriel Mocellin; \033[0;35mVictor Portelinha\033[0;97m')
    print('PUCPR BES 2022-1')
    print('\033[0;97m='*75)
