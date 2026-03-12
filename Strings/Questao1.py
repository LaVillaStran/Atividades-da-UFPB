def resenha(frase):
    frase_refeita = ""
    for i in frase:
        if i != " ":
            frase_refeita += i
    return frase_refeita

def main():
    entrada = input("Digite uma frase e veja como ela fica sem os espaços vazios: ")
    print(resenha(entrada))

if __name__ == "__main__":
    main()