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