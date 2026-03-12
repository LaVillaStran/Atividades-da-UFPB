"""
Faça um programa para imprimir: 

1
2 2
3 3 3
...
n n n n n n ... n 

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e
imprima até a n-ésima linha. 
"""

def enesimo(n):
    frase = ""
    
    for i in range(1,n+1):
        frase += f"{i}  " * i
        frase += f"\n"
    return frase

def main():
    numero = int(input("Digite o valor de um número: "))
    print(enesimo(numero))

if __name__ == "__main__":
    main()