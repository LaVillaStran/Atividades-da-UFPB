"""
Faça um programa em Python que leia um número de telefone e
corrija o número no caso deste conter somente 8 dígitos,
acrescentando o '9' na frente. O usuário pode informar o número com
ou sem o traço separador. Corrija caso ele informe o número sem o
traço separador.
Exemplo:
Informe seu número de telefone: 88715498
Telefone corrigido: 98871-5498
"""

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