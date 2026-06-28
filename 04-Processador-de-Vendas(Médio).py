def total_vendas(vendas):
    total = [ v["valor"] for v in vendas]
    return sum(total)

def vendas_por_vendedor(vendas, nome_vendedor):
    vendas_vendedor = [v for v in vendas if v["vendedor"] == nome_vendedor]
    return vendas_vendedor

def ranking(vendas):
    ranking_vendedor = {}
    
    for i in vendas:
        if i['vendedor'] not in ranking_vendedor:
            ranking_vendedor[i['vendedor']] = 0
        ranking_vendedor[i['vendedor']] += i['valor']
    
    return sorted(ranking_vendedor.items(), key=lambda item:item[1], reverse=True)

def vendas_acima(vendas):
    total = total_vendas(vendas)
    divisor = len(vendas)
    resultado = total / divisor
    valor_maior = [i for i in vendas if i["valor"] > resultado]
    return valor_maior

def produtos_unicos(vendas):
    produtos = [i["produto"] for i in vendas]
    unicos = set(produtos)
    return unicos

def cadastrar_nova_venda(vendas, nome, produto, valor, data):
    nova_venda = {
        "vendedor": nome,
        "produto": produto,
        "valor": valor,
        "data": data
    }
    vendas.append(nova_venda)
    return vendas

def show_menu():
    print("\n +===== PROCESSADOR DE VENDAS =====+\n",
        "| 1- Total de Vendas              |\n",
        "| 2- Vendas por vendedor          |\n",
        "| 3- Ranking de vendedores        |\n",
        "| 4- Vendas acima da média        |\n",
        "| 5- Produtos únicos vendidos     |\n",
        "| 6- Cadastrar nova venda         |\n",
        "| 7- Sair                         |\n",
        "+=================================+")

def input_str(messagem):
    while True:
        valor = input(messagem).capitalize().strip()
        if valor == "":
            print("O campo está vazio. Tente Novamente: ")
            continue
        return valor

def input_int(messagem):
    while True:
        try:
            valor = input(messagem)
            if "," in valor:
                valor = valor.replace(",",".")
            return float(valor)
        except ValueError:
            print("Valor inválido! Tente Novamente:")
            continue

def main():
    vendas = []
    while True:
        show_menu()
        
        opcao = input("Qual opção você deseja selecionar: ")
        while opcao not in ["1","2","3","4","5","6","7"]:
            opcao = input("Opção Inválida! Tente Novamente: ")
        
        if opcao == "1":
            print(f"Valor total de vendas: {total_vendas(vendas):.2f}")
        
        elif opcao == "2":
            nome_vendedor = input_str("Digite o nome do vendedor: ")
            resultado = vendas_por_vendedor(vendas, nome_vendedor)
            if not resultado:
                print("Nenhuma venda encontrada para esse vendedor!")
            else:
                for i in resultado:
                    print(f"\n vendedor: {i['vendedor']}\n produto: {i['produto']}\n valor: {i['valor']:.2f}\n data: {i['data']}\n")
            
        elif opcao == "3":
            rank = ranking(vendas)
            resultado = []
            for chave, valor in rank:
                resultado.append(f"Colocado - Nome: {chave}, Valor: {valor:.2f}")
            for indice, item in enumerate(resultado):
                print(f"{indice+1}° {item}")
            
        elif opcao == "4":
            resultado = vendas_acima(vendas)
            if not resultado:
                print("Nenhum valor encontrado!")
            else:
                for i in resultado:
                    print(f"\n vendedor: {i['vendedor']}\n produto: {i['produto']}\n valor: {i['valor']:.2f}\n data: {i['data']}\n")
            
        elif opcao == "5":
            unicos = produtos_unicos(vendas)
            if not unicos:
                print("Produtos não encotrados!")
            else:
                for indice, valor in enumerate(unicos):
                    print(f"{indice+1} - {valor}")
            
        elif opcao == "6":
            nome = input_str("Digite o nome do vendedor: ")
            produto = input_str("Produto vendido: ")
            valor = input_int("Valor do produto: ")
            data = input_str("Data da venda: ")
            cadastrar_nova_venda(vendas, nome, produto, valor, data)
        elif opcao == "7":
            print("saindo do sistema...")
            break

main()