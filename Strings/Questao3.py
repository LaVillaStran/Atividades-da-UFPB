def numero_telefone(frase):
    if len(frase) == 8:
        frase_nova ="9"

    else:
        frase_nova =""

    for i in range(len(frase)):
        frase_nova += frase[i]
        if len(frase_nova) == 5:
            frase_nova += "-"

    return frase_nova

def main():
    entrada = input("Digite número de celular sem o ddd: ")
    print(numero_telefone(entrada))

if __name__ == "__main__":
    main()