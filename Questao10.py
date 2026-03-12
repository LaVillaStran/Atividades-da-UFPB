def calculo(a):
    if a > 0:
        return "P"
    return "N"

def main():
    valor = int(input("Digite um valor "))
    print(calculo(valor))

if __name__ == "__main__":
    main()