def frase_completa(frase):
    variavel = ""
    for i in range(len(frase)):
        variavel += frase[i]
        print(variavel)

def main():
    frase = input("Digite uma frase: ")
    frase_completa(frase)

if __name__ == "__main__":
    main()