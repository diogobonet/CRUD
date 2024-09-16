import time
import menu
from crudCustomer import saveDb, loadDb
from crudCustomer import validarInt, verifyName
fileProducts = 'database/productsData.json'

dicProdutos = {}
dicProdutos = loadDb(dicProdutos, fileProducts)

#Procurar jogo no sistema
def procurar(dic):
    while True:
        procurar = input('Digite o nome do jogo a ser procurado no estoque:\n\033[0;32m->\033[0;0m ')
        if dic == {}:
            print('Processando...')
            time.sleep(1.2)
            return print('Não há produtos no estoque!')
        try:
            if dic[procurar]["NomeProd"] == procurar:
                print('\033[0;93mProcurando produto...')
                time.sleep(1.2)
                print(f'\033[1;92mO produto {dic[procurar]["NomeProd"]} foi encontrado no estoque!')
                break
        except:
            print('\033[0;93mProcurando produto...')
            time.sleep(1.2)
            print('\033[0;31mProduto não encontrado! Tente novamente!\033[0;0m')

def excluirProd():
    print('\033[0;97m=' * 55)
    print('\033[0;32m                   Exclusão de Produtos')
    print('\033[0;97m=' * 55)
    print('\033[0;36mLista de produtos: \033[0m')
    print('\n')
    for keyProdutos in dicProdutos:
        print(f'\033[1;91m[{keyProdutos}]\033[0m')
        print(f'Nome: {dicProdutos[keyProdutos]["NomeProd"]}')
        print(f'Descrição produto: {dicProdutos[keyProdutos]["DescProduto"]}')
        print(f'Preço: {dicProdutos[keyProdutos]["Preço"]}')
        print(f'Desenvolvedor: {dicProdutos[keyProdutos]["Desenvolvedor"]}')
        print(f'Categoria: {dicProdutos[keyProdutos]["Categoria"]}')
        print(f'Quantidade no estoque: {dicProdutos[keyProdutos]["quant"]}')
        print('\n')
    dicPraRemover = input('Digite o nome do produto a ser excluido: ')
    print(f'\n\033[0;33mNome: {dicProdutos[dicPraRemover]["NomeProd"]}')
    print(f'Descrição produto: {dicProdutos[dicPraRemover]["DescProduto"]}')
    print(f'Preço: {dicProdutos[dicPraRemover]["Preço"]}')
    print(f'Desenvolvedor: {dicProdutos[dicPraRemover]["Desenvolvedor"]}')
    print(f'Categoria: {dicProdutos[dicPraRemover]["Categoria"]}')
    print(f'Quantidade no estoque:{dicProdutos[dicPraRemover]["quant"]}')
    print('\n')
    opcaoExcluir = input('\033[0;91mVocê tem certeza que quer apagar este cadastro? (S/N)\n• ')
    if opcaoExcluir == 's' or opcaoExcluir == 'S':
        del dicProdutos[dicPraRemover]
        print('\033[0;92mCadastro removido com sucesso!')
        saveDb(dicProdutos, fileProducts)
    elif opcaoExcluir == 'n' or opcaoExcluir == 'N':
        print('\033[0;91mOperação de excluir cancelada!')
    else:
        print(f'[{opcaoExcluir}] é uma opção inválida! Tente novamente...')

# Cadastrar um Jogo/Produto
def cadProd():
    print("\033[0;97m="*55)
    print("\033[0;32m                Cadastro de Produtos")
    print("\033[0;97m=\033[0;0m" * 55)
    try:
        nomeProduto = str(input("Digite o nome do Jogo:\n\033[0;32m->\033[0;0m "))
        descProduto = input("Digite a descrição do produto:\n\033[0;32m->\033[0;0m ")
        categoria = input("Selecione a categoria do jogo:\n\033[0;32m->\033[0;0m ")
        valor = float(input("Digite o preço do jogo - R$:\n\033[0;32m->\033[0;0m "))
        empresa = input(f"Digite o nome da empresa que desenvolveu o jogo ({nomeProduto}):\n\033[0;32m->\033[0;0m ")
        quant = int(input('Digite a quantidade do produto:\n\033[0;32m->\033[0;0m '))
        cadastroJogo = {"NomeProd": nomeProduto, "DescProduto": descProduto, "Preço": valor, "Desenvolvedor": empresa,
                        "Categoria": categoria, "quant": quant}
        dicProdutos[nomeProduto] = cadastroJogo
        print(cadastroJogo)
        print("\033[0;33mCadastrando produto...")
        time.sleep(1.2)
        print("\033[0;32mProduto cadastrado!\033[0;0m")
        saveDb(dicProdutos, fileProducts)
        return dicProdutos


    except:
        print("\033[1;31mError -> Valor inválido! Tente novamente!\033[0m")

# Excluir produto
def editarProd():
    print('\033[0;97m==' * 15)
    print('\033[0;32m            Edição')
    print('\033[0;97m==' * 15)
    print('\033[0;36mLista de produtos: \033[0m')
    for keyProdutos in dicProdutos:
        print(f'\033[1;91m[{keyProdutos}]\033[0;0m')
        print(f'Nome: {dicProdutos[keyProdutos]["NomeProd"]}')
        print(f'Descrição produto: {dicProdutos[keyProdutos]["DescProduto"]}')
        print(f'Preço: {dicProdutos[keyProdutos]["Preço"]}')
        print(f'Desenvolvedor: {dicProdutos[keyProdutos]["Desenvolvedor"]}')
        print(f'Categoria: {dicProdutos[keyProdutos]["Categoria"]}')
        print(f'Quantidade no estoque: {dicProdutos[keyProdutos]["quant"]}')
        print('\n')
    dicPraEdit = input('Digite o nome do produto a ser editado: ')
    print(f'\n\033[1;93m[1] Nome: {dicProdutos[dicPraEdit]["NomeProd"]}')
    print(f'[2] Descrição produto: {dicProdutos[dicPraEdit]["DescProduto"]}')
    print(f'[3] Preço produto: {dicProdutos[dicPraEdit]["Preço"]}')
    print(f'[4] Desenvolvedora: {dicProdutos[dicPraEdit]["Desenvolvedor"]}')
    print(f'[5] Categoria: {dicProdutos[dicPraEdit]["Categoria"]}')
    print(f'[6] Quantidade: {dicProdutos[dicPraEdit]["quant"]}\033[0;0m')

    opEdit = validarInt('Qual das informações você gostaria de editar?: ')
    if opEdit == 1:
        novoNome = input('Novo nome: ')
        novoNome = verifyName(novoNome)
        dicProdutos[dicPraEdit]['NomeProd'] = novoNome
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de nome concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 2:
        novaDesc = input('Nova Descrição:')
        novaDesc = verifyName(novaDesc)
        dicProdutos[dicPraEdit]['DescProduto'] = novaDesc
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de Descrição concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 3:
        novoPreco = float(input('Novo preço: R$'))
        dicProdutos[dicPraEdit]["Preço"] = novoPreco
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de preço concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 4:
        novaDesenvolvedora = input('Nova desenvolvedora: ')
        novaDesenvolvedora = verifyName(novaDesenvolvedora)
        dicProdutos[dicPraEdit]['Desenvolvedor'] = novaDesenvolvedora
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de desenvolvedora concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 5:
        novaCategoria = input('Nova categoria: ')
        novaCategoria = verifyName(novaCategoria)
        dicProdutos[dicPraEdit]['Categgoria'] = novaCategoria
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de categoria concluída!')
        saveDb(dicProdutos, fileProducts)
    elif opEdit == 6:
        novaQuantidade = int(input('Nova quantidade: '))
        dicProdutos[dicPraEdit]['quant'] = novaQuantidade
        print('\033[0;93mProcessando...\n')
        time.sleep(1.2)
        print('\n\033[0;32mEdição de quantidade concluída!')
        saveDb(dicProdutos, fileProducts)

    else:
        print(f'\033[0;31m[{opEdit}] é uma opção inválida! Tente novamente...\033[0;0m')


def menuProd():
    while True:
        print("\033[0;97m="*55)
        print("\033[0;32m                  Setor de Produtos\033[0;0m")
        print("\033[0;97m=\033[0;0m" * 55)
        print("\033[0;33m[ 1 ] Cadastrar Jogo/Produto")
        print("[ 2 ] Procurar Jogo/Produto")
        print("[ 3 ] Editar Jogo/Produto")
        print("[ 4 ] Excluir Jogo/Produto")
        print("\033[0;31m[ 5 ] Voltar para o menu principal\033[0;0m")
        op = input("Escolha uma opção:\n\033[0;32m-> \033[0m")
        try:
            if op == "1":
                cadProd()
            if op == "2":
                procurar(dicProdutos)
            if op == "3":
                editarProd()
            if op == "4":
                excluirProd()
            if op == "5":
                menu.menuPrincipal()
        except:
            print("\033[0;91mValor inválido! Tente novamente!")
