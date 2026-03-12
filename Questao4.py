def branco(d1):
    d1_refeito = ""
    for i in d1:
        if i == " ":
            continue
        else:
            d1_refeito += i
    return d1_refeito

def main():
    frase = input("Digite uma frase com 'brancos'/'espaços': ")
    print(branco(frase))

if __name__ == "__main__":
    main()