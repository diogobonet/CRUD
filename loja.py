import time
from clientes import dicClientes, saveDb, loadDb, print_cor, CorAmarelo, CorVerm, CorVoltar
from cadastroprodutos import dicProdutos


fileProducts = 'cadastrosProdutos.json'
file_listanotas = 'listaDeNotas.json'


pedidos = []
dicCarrinho = {}
pedidos = loadDb(pedidos, file_listanotas)




def procurarCliente(dicClientes):

    cpf = input('Digite o cpf do cliente:')
    if dicClientes == {}:
        print('Processando ...')
        time.sleep(1)
        return print('Não há clientes registrados no sistema!')


    try:


        if dicClientes[cpf]["cpf"] == cpf:
            print_cor('Processando ...', CorAmarelo)
            time.sleep(1)
            print(f'\nO cliente [{dicClientes[cpf]["nome"]}] foi encontrado!')
            print(f'Idade do cliente [{dicClientes[cpf]["idade"]}] ')
            print(f'Endereço do cliente: [{dicClientes[cpf]["endereco"]}] ')
            print(f'CPF do cliente: [{dicClientes[cpf]["cpf"]}] \n')
            continuar = input((f'O cliente [{dicClientes[cpf]["nome"]}] gostaria de continuar a compra?\n[S/N]: • '))
            if continuar == 'S':
                print_cor('Processando ...', CorAmarelo)
                time.sleep(1)
                print(f'Continuando com a compra de {dicClientes[cpf]["nome"]} ')
                return cpf, continuar


            elif continuar == 'N':
                print_cor('Processando ...', CorAmarelo)
                time.sleep(1)
                print('Compra cancelada );')
                from menu import menuPrincipal
                return menuPrincipal()




    except:
        print_cor('Procurando cliente ...', CorAmarelo)
        time.sleep(1)
        print_cor('Cliente não encontrado', CorVerm)
        return menuLoja(pedidos)

def listarProdutos(dicProdutos):
    print("=" * 55)
    print("                   Lista de jogos")
    print("=" * 55)
    cont = 0
    for i in dicProdutos:
        cont += 1
        print(f"{cont}-> {i}")





def procurarCompra(dicProdutos):
    listarProdutos(dicProdutos)
    procurar = input('Digite o nome do jogo que você gostaria de comprar ?\n-> ')
    if dicProdutos == {}:
        print_cor('Processando ...', CorAmarelo)
        time.sleep(1)
        return print('Não há produtos disponiveis no estoque!')
    try:
        if dicProdutos[procurar]["NomeProd"] == procurar:

            print_cor('Processando ...', CorAmarelo)
            time.sleep(1)

            print(f'O produto {dicProdutos[procurar]["NomeProd"]} foi encontrado!')
            print(f'Nome do Jogo: {dicProdutos[procurar]["NomeProd"]}')
            print(f'Descrição do Jogo: {dicProdutos[procurar]["DescProduto"]}')
            print(f'Categoria do Jogo: {dicProdutos[procurar]["Categoria"]}')
            print(f'Preço do Jogo: {dicProdutos[procurar]["Preço"]}')
            print(f'Quantidade do jogo: {dicProdutos[procurar]["quant"]}')
            quantidadeUsuario = int(input('Qual a quantidade desse jogo que gostaria de comprar?\n->'))

            if dicProdutos[procurar]["quant"] > 0:
                num = dicProdutos[procurar]["quant"]
                novoEstoque = num - quantidadeUsuario
                if novoEstoque >= 0:
                    dicProdutos[procurar]["quant"] = novoEstoque
                    saveDb(dicProdutos, fileProducts)
                    return procurar,quantidadeUsuario
                else:
                    print('Nao foi possivel atualizar o estoque pois o pedido foi maior que o estoque registrado')
            if dicProdutos[procurar]["quant"] == 0:
                print('Não há estoque desse produto!!!!\nContate com a fornecedora para atualizar o estoque')
    except:
        print_cor('Procurando produto ...', CorAmarelo)
        time.sleep(1.2)
        print(f'{CorVerm}produto não encontrado! Tente novamente!', CorVerm)



def comprar(dicProdutos,dicClientes):
    if dicProdutos == {}:
        print('Processando ...')
        time.sleep(1)
        print('Não há produtos no estoque!! Contate com a fornecedora!')
        return


    try:
        cpf,continuar = procurarCliente(dicClientes)
        nome = dicClientes[cpf]['nome']


        nomeJogo,quant = procurarCompra(dicProdutos)

        preco = dicProdutos[nomeJogo]['Preço']


        precoTotalV = quant*preco


        notaFiscal = {'Cliente':nome,
                      'CPF':cpf,
                      'Jogo':nomeJogo,
                      'Preco': preco,
                      'Quantidade': quant,
                      'PrecoTotal': precoTotalV,
                      }

        print('\nPedido realizado com a seguinte nota fiscal:')
        print(f'Nome do cliente: [{notaFiscal["Cliente"]}]')
        print(f'CPF: [{notaFiscal["CPF"]}]')
        print(f'Jogo: [{notaFiscal["Jogo"]}]')
        print(f'Preço: [{notaFiscal["Preco"]}]')
        print(f'Preço total: [{notaFiscal["PrecoTotal"]}]')
        print(f'Quantidade do jogo: [{notaFiscal["Quantidade"]}]')
        input('\n[ENTER] para continuar...')
        return notaFiscal,continuar

    except:

        time.sleep(1.2)
        print('Voltando ao menu principal ...', CorVerm)

def comprarSemProcurarCliente(dicProdutos,notaFiscal):
    nome = notaFiscal["Cliente"]
    cpf = notaFiscal["CPF"]

    nomeJogo,quant = procurarCompra(dicProdutos)
    preco = dicProdutos[nomeJogo]["Preço"]
    precoTotalV = quant * preco
    notaFiscal = {'Cliente': nome,
                  'CPF': cpf,
                  'Jogo': nomeJogo,
                  'Preco': preco,
                  'Quantidade': quant,
                  'PrecoTotal': precoTotalV,}

    print('\nPedido adcionado ao carrinho com a seguinte nota fiscal:')
    print(f'Nome do cliente: [{notaFiscal["Cliente"]}]')
    print(f'CPF: [{notaFiscal["CPF"]}]')
    print(f'Jogo: [{notaFiscal["Jogo"]}]')
    print(f'Preço: [{notaFiscal["Preco"]}]')
    print(f'Preço total: [{notaFiscal["PrecoTotal"]}]')
    print(f'Quantidade do jogo: [{notaFiscal["Quantidade"]}]')
    input('\n[ENTER] para continuar...')
    return notaFiscal















def adcionarAoCarrinho(notaFiscal,dicProdutos):
    listaCompras = []
    listaCompras.append(notaFiscal)



    while True:

        continuar = input('Deseja continuar adcionando compras ao carrinho?\nS/N ->')
        letters = str('abcdefghijklmopqrtuvwxyzABCDEFGHIJKLMOPQRTUVWXYZ123456789.,;')
        for i in letters:
            if continuar == i:
                print('As únicas opções disponíveis são S ou N, digite um valor válido' )
        if continuar == 'S':
            print('Adcionando pedido ao carrinho ...')





            notaFiscal1=comprarSemProcurarCliente(dicProdutos,notaFiscal)
            listaCompras.append(notaFiscal1)


        if continuar == 'N':
            cpf = notaFiscal["CPF"]
            dicCarrinho[cpf] = listaCompras
            listaCompras.clear()


            return dicCarrinho







def listarPedidos(pedidos):
    cont = 0
    for i in pedidos:
        cont +=1
        print(f"{cont} -> {i}")













def menuLoja(pedidos):
    while True:
        print("=" * 55)
        print("                        Loja")
        print("=" * 55)
        print("[ 1 ] Comprar jogos")
        print("[ 2 ] Lista de jogos")
        print("[ 3 ] Metodos de pagamentos", )
        print("[ 4 ] Listar pedidos ", CorVerm)
        print("[ 5 ] Voltar para Menu", CorVoltar)
        op = input("Escolha uma opção:\n")

        # Procurar Jogos
        if op == "1":
            notaFiscal,continuar = comprar(dicProdutos, dicClientes)
            if continuar == 'S':
                dicCarrinho = adcionarAoCarrinho(notaFiscal,dicProdutos)


                metodopagamento()
                pedidos.append(dicCarrinho)
                saveDb(pedidos,file_listanotas)



        # Jogos Indicados
        if op == "2":
           listarProdutos(dicProdutos)

        # Todos os jogos disponiveis no banco de dados
        if op == "3":
            print("Os métodos de pagamentos da loja são: Boleto, Pix, Cartão de Débito")
            time.sleep(1)

        if op == "4":
            listarPedidos(pedidos)


        # Voltar para o Menu
        if op == "5":
            from menu import menuPrincipal

            return menuPrincipal()



def metodopagamento():
    print("\nOs métodos de pagamentos da loja são:\n[1] Boleto, [2] Pix, [3] Cartão de Débito")
    opcaoMetodo = input("Escolha a opção do método de pagamento:\n->")
    # Opção de Boleto
    if opcaoMetodo == "1":
        print("Você escolheu a forma de pagamento em Boleto!")
        continuar = input("Deseja continuar? [S/N]\nDigite [0] para voltar\n-> ").upper()

        if continuar == "S" or continuar == "SIM":
            print("Processando compra...")
            time.sleep(1.5)
            print("Compra efetuada!")
            fatorCompra = str('Boleto')
            return fatorCompra

        elif continuar == "N" or continuar == "NAO":
            return menuLoja(pedidos)

        elif continuar == "0":
            return metodopagamento()

        elif continuar != "N" or continuar == "S" or continuar == "0":
            print("Digite apenas [S/N ou 0]! Tente novamente!")
            return metodopagamento()

    # Opção de PIX
    if opcaoMetodo == "2":
        print("Você escolheu a forma de pagamento em PIX!")
        continuar = input("Deseja continuar? [S/N]\n-> ").upper()

        if continuar == "S" or continuar == "SIM":
            print("Processando compra...")
            time.sleep(3)
            print("Compra efetuada!")
            print('O pagamento pode ser realizado no CPF 09163976960')
            fatorCompra = str('Pix')
            return fatorCompra

        elif continuar == "N" or continuar == "NAO":
            return comprar(dicProdutos,dicClientes)

        elif continuar == "0":
            return metodopagamento()

        elif continuar != "N" or continuar == "S" or continuar == "0":
            print("Digite apenas [S/N ou 0]! Tente novamente!")
            return metodopagamento()

    # Opção de Cartão de Crédito
    if opcaoMetodo == "3":
        print("Você escolheu a forma de pagamento em Cartão de Débito!")
        continuar = input("Deseja continuar? [S/N]\n-> ").upper()

        if continuar == "S" or continuar == "SIM":
            print("Processando compra...")
            time.sleep(3)
            print("Compra efetuada!")

        elif continuar == "N" or continuar == "NAO":
            return comprar(dicProdutos,dicClientes)

        elif continuar == "0":
            return metodopagamento()

        elif continuar != "N" or continuar == "S" or continuar == "0":
            print("Digite apenas [S/N ou 0]! Tente novamente!")
            return metodopagamento()

    comprar(dicClientes,dicProdutos)