def add_student(turma, nome, nota):
    if any(i["nome"] == nome for i in turma):
        return f"O aluno {nome} já foi adicionado à turma!"
    else:
        aluno = {
            "nome": nome,
            "nota": nota
        }
        turma.append(aluno)
        return f"O aluno {nome} foi adicionado à turma com sucesso!"

def list_classroom(turma):
    resultado = []
    if not turma:
        print("A turma está vazia. Adiciona um aluno para continuar!")
    else:
        for i in sorted(turma, key=lambda item:item["nota"], reverse=True):
            if i["nota"] >= 7:
                resultado.append(f"{i["nome"]}: Aprovado ✅")
            elif 5 <= i["nota"] < 7:
                resultado.append(f"{i["nome"]}: Recuperação ⚠️")
            elif i["nota"] < 5:
                resultado.append(f"{i["nome"]}: Reprovado ❌")
        for i in resultado:
            print(i)

def statistics_report(turma):
    total_notas = 0
    aprovados = 0
    recuperacao = 0
    reprovado = 0
    
    if not turma:
        print("Nenhum dado foi encontrado!")
    else:
        for i in turma:
            total_notas += i["nota"]
        media_class = total_notas / len(turma)
        
        for i in turma:
            if i["nota"] >= 7:
                aprovados += 1
            elif 5 <= i["nota"] < 7: 
                recuperacao += 1
            elif i["nota"] < 5:
                reprovado += 1
        
        maior = max(turma, key=lambda i:i["nota"])
        menor = min(turma, key=lambda i:i["nota"])
        
        print(f"\nMédia da Turma: {media_class} \nMaior nota: {maior["nota"]} \nMenor nota: {menor["nota"]} \nAprovados: {aprovados} \nRecuperação: {recuperacao} \nReprovado: {reprovado}")

def seek_student(turma, nome):
    encontrados = []
    for i in turma:
        if nome.lower() in i["nome"].lower():
            encontrados.append(i["nome"])
    
    if not encontrados:
        print("Nenhum aluno foi encontrado!")
    else:
        for aluno in encontrados:
            print(aluno)

def input_str(messagem):
    while True:
        valor = input(messagem).strip().capitalize()
        if valor == "":
            print("O espaço está vazio. Tente Novamente!")
            continue
        return valor

def input_int(menssagem):
    while True:
        try:
            valor = float(input(menssagem))
            if valor < 0 or valor > 10:
                print("O valor deve ser entre 0 a 10!")
                continue
        except ValueError:
            print("Valor inválido. Tente Novamente!")
            continue
        return valor

def show_menu():
    print("\n +==== ANALISADOR DE NOTAS =====+\n",
        "| 1- Adicionar aluno           |\n",
        "| 2- Listar turma              |\n",
        "| 3- Relatório estatístico     |\n",
        "| 4- Buscar aluno              |\n",
        "| 5- Sair                      |\n",
        "+==============================+\n")

def main():
    turma = []
    while True:
        show_menu()
        
        opcao = input("Selecione a opção: ")
        while opcao not in ["1","2","3","4","5"]:
            opcao = input("Opção Inválida. Tente Novamente:")
        
        if opcao == "1":
            nome = input_str("Digite o nome do aluno: ")
            nota = input_int("Digite a nota do aluno: ")
            print(add_student(turma, nome, nota))
        elif opcao == "2":
            list_classroom(turma)
        elif opcao == "3":
            statistics_report(turma)
        elif opcao == "4":
            nome = input_str("Buscar por: ")
            seek_student(turma, nome)
        elif opcao == "5":
            print("Saindo do sistema...")
            break

main()