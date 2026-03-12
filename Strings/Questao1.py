"""
Escreva um programa para construir uma string a partir da eliminção
de espaços em branco de uma string inicial.
"""

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