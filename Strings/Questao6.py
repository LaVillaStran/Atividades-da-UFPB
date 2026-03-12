"""
Refaça o Exercício 1 usando as funções para manipulação de strings de
Python
"""

def resenha(frase):
    frase = frase.split()
    frase = "".join(frase)

    return frase
def main():
    entrada = input("Digite uma frase e veja como ela fica sem os espaços vazios: ")
    print(resenha(entrada))

if __name__ == "__main__":
    main()