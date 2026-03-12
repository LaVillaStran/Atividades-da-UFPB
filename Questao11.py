def tamanho(n):
    quantidade_caracteres = 0
    while n != 0:
        quantidade_caracteres += 1
        n //= 10

    return quantidade_caracteres

def main():
    numero = int(input("Digite um número e veja a quantidade de caracteres: "))
    print(f"O número {numero} tem {tamanho(numero)} dígitos.")

if __name__ == "__main__":
    main()