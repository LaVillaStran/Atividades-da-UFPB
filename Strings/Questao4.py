def frase_crescente(frase):
    frase_nova = ""
    for i in frase:
        frase_nova += i
        print(frase_nova)

def main():
    entrada = input("Digite uma frase e veja ela sendo compeltada: ")
    frase_crescente(entrada)

if __name__ == "__main__":
    main()