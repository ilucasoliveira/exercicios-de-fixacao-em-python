def validar_senha(senha):
    especiais = "!@#$%^&*"
    score = 0
    resultado = {
        "score": score,
        "feedback": []
    }
    if len(senha) >= 8:
        score += 1
    else:
        resultado["feedback"].append("Mínimo de 8 caracteres")
    if any(i.isupper() for i in senha):
        score += 1
    else:
        resultado["feedback"].append("Digite pelo menos uma letra MAIÚSCULA")
    if any(i.islower() for i in senha):
        score += 1
    else:
        resultado["feedback"].append("Digite pelo menos uma letra minuscula")
    if any(i.isdigit() for i in senha):
        score += 1
    else:
        resultado["feedback"].append("Digite pelo menos um número")
    if any(i in especiais for i in senha):
        score += 1
    else:
        resultado["feedback"].append("Digite pelo menos um caracter especial, como: '!@#$%^&*'")
    
    resultado["score"] = score
    
    if score == 5:
        resultado["feedback"].append("Senha forte! ✅")
    return resultado

def classificar_senha(score):
    if score == 0 or score == 1:
        return "Muito fraca"
    elif score == 2:
        return "Fraca"
    elif score == 3:
        return "Média"
    elif score == 4:
        return "Forte"
    elif score == 5:
        return "Muito forte"

def input_strip(messagem):
    while True:
        valor = input(messagem).strip()
        if valor == "":
            print("Senha inválida. Tente Novamente!")
            continue
        else:
            return valor

def show_main():
    print("\n +======================+\n",
    "| 1- Validar senha     |\n",
    "| 2- Sair              |\n"
    " +======================+\n")


def main():
    senha = input_strip("Crie sua senha: ")
    while True:
        show_main()
        
        opcao = input("Digite a opção: ")
        while opcao not in ["1", "2"]:
            opcao = input("Opção Inválida! Tente Novamente: ")
        
        if opcao == "1":
            resultado = validar_senha(senha)
            print(f"Score: {resultado['score']}/5")
            print(f"Classificação: {classificar_senha(resultado['score'])}")
            print("Feedback:")
            for mensagem in resultado["feedback"]:
                print(f"  • {mensagem}")
        elif opcao == "2":
            break

main()