"""
Escreva um programa em Python que receba uma string e a imprima
na vertical e em formato de escada. Por exemplo, se o usuário digitar a
string FULANO, o programa deve exibir a seguinte saída:
F
FU
FUL
FULA
FULAN
FULANO
"""

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