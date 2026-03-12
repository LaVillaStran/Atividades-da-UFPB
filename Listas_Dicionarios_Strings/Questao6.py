"""
Escreva um programa em Python que receba uma string e a imprima na vertical e em
formato de escada. Por exemplo, se o usuário digitar a string FULANO, o programa deve
exibir a seguinte saída:
F
FU
FUL
FULA
FULAN
FULANO
"""

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