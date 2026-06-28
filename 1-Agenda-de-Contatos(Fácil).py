
def add_contact(agenda, nome, telefone, email):
    if nome in agenda:
        print("Esse nome já existe em sua agenda. Tente Novamente!")
    else:
        agenda[nome] = {
            "telefone": telefone,
            "email": email
        }
        print(f"O nome {nome} foi adicionado a lista de contatos!")

def list_contacts(agenda):
    resultado = ""
    if not agenda:
        print("A lista de contatos está vazia. Adicione um contato!")
    else:
        for chave, valor in sorted(agenda.items(), key=lambda item:item[0]):
            resultado += f"{chave} - Telefone: {valor['telefone']}.\n"
        print(resultado)

def seek_name(agenda, nome):
    encontrados = []
    for chave, valor in agenda.items():
        if nome.lower() in chave.lower():
            encontrados.append(chave)
    
    if not encontrados:
        print("Nenhum contato encontrado.")
    else:
        for contato in encontrados:
            print(contato)

def delete_name(agenda, nome):
    if nome not in agenda:
        print("O nome inserido não foi encontrado!")
    else:
        del agenda[nome]
        print(f"{nome} foi removido da agenda de contatos!")

def export_agend(agenda):
    resultado = ""
    if agenda == {}:
        print("A lista de contatos está vazia. Adicione um contato!")
    else:
        for chave, valor in sorted(agenda.items(), key=lambda item:item[0]):
            resultado += f"\n+============================+\nNome:     {chave}\nTelefone: {valor['telefone']}\nEmail:    {valor['email']}\n+============================+\n"
        print(resultado)


def input_strip(mensagem):
    while True:
            valor = input(mensagem).strip()
            if valor == "":
                print("O espaço está vazio. Tente Novamente!")
                continue
            return valor

def show_menu():
    print(
        "\n +====== AGENDA DE CONTATOS ======+\n",
        "| 1- Adicionar contato           |\n",
        "| 2- Listar contatos             |\n",
        "| 3- Busca parcial por nome      |\n",
        "| 4- Remover contato             |\n",
        "| 5- Exportar agenda             |\n",
        "| 6- Sair                        |\n",
        "+================================+\n")


def main():
    agenda = {}
    
    while True:
        
        show_menu()
        
        opcao = input_strip("Qual operação você deseja realizar: ")
        while opcao not in ["1","2","3","4","5","6"]:
            opcao = input_strip("Valor inválido. Tente Novamente: ")
        
        if opcao == "1":
            nome = input_strip("Nome do Contato: ").title()
            telefone = input_strip("Telefone: ")
            email = input_strip("E-mail: ")
            add_contact(agenda, nome, telefone, email)
        elif opcao == "2":
            list_contacts(agenda)
        elif opcao == "3":
            nome = input_strip("Buscar por: ")
            seek_name(agenda, nome)
        elif opcao == "4":
            nome = input_strip("Qual nome você deseja remover: ").title()
            delete_name(agenda, nome)
        elif opcao == "5":
            export_agend(agenda)
        elif opcao == "6":
            print("Saindo...")
            break

main()