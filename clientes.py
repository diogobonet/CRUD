import verifycpf
import menu
import json

file = 'cadastrosClientes.json'

def loadDb(variavel, filename):
    with open(filename, 'r') as r:
        variavel = json.load(r)
    return variavel


dicClientes = {}
dicClientes = loadDb(dicClientes, file)

CorVerm = '\033[0;31m'
CorVerde = "\033[0;32m"
CorAzul = "\u001b[34;1m"
CorAmarelo = "\033[1;33m"
CorVoltar = '\u001b[0m'


def saveDb(data, filename):
    with open(filename, 'w') as w:
        json.dump(data, w)


def print_cor(msg, cor):
    print(cor, msg, CorVoltar)


def validar(msg, controlvariable, funcao):
    whileV = False
    while whileV == False:
        if controlvariable == '':
            print('\033[0;31mERRO, digite uma opção válida\033[m')
            controlvariable = input(msg)
        else:
            whileV == True
            return funcao(controlvariable)


def validarInt(msg):
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


def verifyAge(idade):
    while True:
        try:
            if idade < 18 or idade > 122:
                print(f'\n[{idade}] é inválido, apenas maiores de 18 e menores que 122')
                idade = int(input('Idade: '))
            if idade >= 18 and idade <= 122:
                return idade
        except ValueError:
            print(f'\n[{idade}] é inválido, apenas podem se registrar maiores de 18 anos e menores que 122 anos.')


def verifyName(name):
    letras = 'abcdefghijklmnopqrstuvwxyzãáéíóúçABCDEFGHIJKLMNOPQRSTUVWXYZÃÁÉÍÓÚÇ'
    for l in name:
        if l in letras:
            pass
        else:
            print(f'[{l}] é uma letra inválida!')
            name = input('• Nome: ')
            return verifyName(name)
    return name


def verifyEndereco(endereco):
    letrasNums = '.,0123456789abcdefghijklmnopqrstuvwxyzãáéíóúçABCDEFGHIJKLMNOPQRSTUVWXYZÃÁÉÍÓÚÇ '
    for l in endereco:
        if l in letrasNums:
            pass
        else:
            print(f'[{l}] é uma letra/número inválida(o)!')
            endereco = input('• Endereço: ')
            return verifyEndereco(endereco)
    return endereco


def cad():
    print('\n')
    name = input('• Nome: ')
    name = validar('• Nome: ', name, verifyName)
    age = int(input('• Idade: '))
    age = validar('• Idade: ', age, verifyAge)
    cpf = input('• Cpf: ')
    while True:
        cpfSave = cpf
        cpf = verifycpf.cpf_valido(cpf)
        if cpf == True:
            cpf = cpfSave
            break
        else:
            print_cor('CPF Inválido!', CorVerm)
            cpf = input('• Cpf: ')
    adress = input('• Endereço: ')
    adress = validar('• Endereço: ', adress, verifyEndereco)
    cdoc = {"nome": name, "idade": age, "endereco":adress, "cpf": cpf}
    dicClientes[cpf] = cdoc
    print_cor("\033[0;32mCadastro concluido!", CorVerde)
    saveDb(dicClientes, file)
    return dicClientes


def editarDic():
    print('\033[0;97m='*55)
    print('\033[0;32m                        Edição')
    print('\033[0;97m='*55)
    print('\n')
    print('Lista de Cadastros: ')
    for keyCpf in dicClientes:
        print(f'\033[1;31m[{keyCpf}]\033[0;0m')
        print(f'Nome: {dicClientes[keyCpf]["nome"]}')
        print(f'Idade: {dicClientes[keyCpf]["idade"]}')
        print(f'Endereço: {dicClientes[keyCpf]["endereco"]}')
        print(f'Cpf: {dicClientes[keyCpf]["cpf"]}')
        print('\n')
    dicPraEdit = input('Digite o CPF do cadastro a ser editado: ')
    print(f'\n[1] Nome: {dicClientes[dicPraEdit]["nome"]}')
    print(f'[2] Idade: {dicClientes[dicPraEdit]["idade"]}')
    print(f'[3] Endereço: {dicClientes[dicPraEdit]["endereco"]}')
    opEdit = validarInt('Qual das informações você gostaria de editar?: ')
    if opEdit == 1:
        novoNome = input('Novo nome: ')
        novoNome = validar('Novo nome: ', novoNome, verifyName)
        dicClientes[dicPraEdit]['nome'] = novoNome
        print_cor('\nEdição de nome concluída!', CorVerde)
        saveDb(dicClientes, file)
    elif opEdit == 2:
        novaIdade = int(input('Nova idade: '))
        novaIdade = validar('Novo idade: ', novaIdade, verifyAge)
        dicClientes[dicPraEdit]['idade'] = novaIdade
        print_cor('\nEdição de idade concluída!', CorVerde)
        saveDb(dicClientes, file)
    elif opEdit == 3:
        novoEndereco = input('Novo endereço: ')
        novoEndereco = validar('Novo endereço: ', novoEndereco, verifyEndereco)
        dicClientes[dicPraEdit]['endereco'] = novoEndereco
        print_cor('\nEdição de endereço concluída!', CorVerde)
        saveDb(dicClientes, file)
    else:
        print(f'[{opEdit}] é uma opção inválida! Tente novamente...')



def excluirDic():
    print('\n')
    print('\033[0;97m='*55)
    print('\033[0;32m                              Exclusão de cadastros')
    print('\033[0;97m='*55)
    print('\n')
    print('Lista de Cadastros: ')
    for keyCpf in dicClientes:
        print(f'\033[1;31m[{keyCpf}]\033[0;0m')
        print(f'Nome: {dicClientes[keyCpf]["nome"]}')
        print(f'Idade: {dicClientes[keyCpf]["idade"]}')
        print(f'Endereço: {dicClientes[keyCpf]["endereco"]}')
        print(f'Cpf: {dicClientes[keyCpf]["cpf"]}')
        print('\n')
    dicPraRemover = input('Digite o CPF do cadastro a ser removido: ')
    print(f'\nNome: {dicClientes[dicPraRemover]["nome"]}')
    print(f'Idade: {dicClientes[dicPraRemover]["idade"]}')
    print(f'Endereço: {dicClientes[dicPraRemover]["endereco"]}')
    print(f'Cpf: {dicClientes[dicPraRemover]["cpf"]}')
    print('\n')
    opcaoExcluir = input('\033[0;91mVocê tem certeza que quer apagar este cadastro? (S/N)\n• ')
    if opcaoExcluir == 's' or opcaoExcluir == 'S':
        del dicClientes[dicPraRemover]
        print('\033[0;31mCadastro removido com sucesso!\033[0;0m')
        saveDb(dicClientes, file)
    elif opcaoExcluir == 'n' or opcaoExcluir == 'N':
        print('Operação de excluir cancelada!')
    else:
        print(f'[{opcaoExcluir}] é uma opção inválida! Tente novamente...')


def listarDic():
    print('\n')
    print('\033[0;97m='*55)
    print('\033[0;32m                   Lista de cadastros')
    print('\033[0;97m='*55)
    print('\n')
    if len(dicClientes) > 0:
        for keyCpf in dicClientes:
            print(f'\033[1;31m[{keyCpf}]\033[0;0m')
            print(f'Nome: {dicClientes[keyCpf]["nome"]}')
            print(f'Idade: {dicClientes[keyCpf]["idade"]}')
            print(f'Endereço: {dicClientes[keyCpf]["endereco"]}')
            print(f'Cpf: {dicClientes[keyCpf]["cpf"]}')
            print('\n')
    else:
        print_cor('** Lista está vazia! **\n', CorVerm)
    input('[ENTER] para voltar...')


def menuClientes():
    while True:
        print('\n')
        print("\033[0;97m=" * 55)
        print("\033[0;32m                Cadastro de clientes")
        print("\033[0;97m=" * 55)
        print("\033[0;33m[ 1 ] Cadastrar Clientes")
        print("[ 2 ] Listar Clientes")
        print("[ 3 ] Editar Cadastros")
        print("[ 4 ] Excluir Cadastros")
        print("\033[0;31m[ 5 ] Voltar para o menu principal\033[m")
        op = validarInt('Escolha a operação a ser realizada:\n-> ')
        if op == 1:
            cad()
        elif op == 2:
            listarDic()
        elif op == 3:
            editarDic()
        elif op == 4:
            excluirDic()
        elif op == 5:
            menu.menuPrincipal()
            break
        else:
            print('\033[0;31mNúmero inválido, Tente novamente...\033[m')