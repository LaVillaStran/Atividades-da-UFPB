def inverter(frase):
    return frase[::-1]

def main():
    entrada = input("Digite uma frase e veja seu reverso: ")
    print(inverter(entrada))

if __name__ == "__main__":
    main()