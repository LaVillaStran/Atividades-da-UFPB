def resenha(frase):
    frase = frase.split()
    frase = "".join(frase)

    return frase
def main():
    entrada = input("Digite uma frase e veja como ela fica sem os espaços vazios: ")
    print(resenha(entrada))

if __name__ == "__main__":
    main()