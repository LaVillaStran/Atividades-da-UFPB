def verificator(p1,p2) -> int|str:
    print(f"{p1}: {len(p1)}\n{p2}: {len(p2)}")
    if p1 == p2:
        return "Eles possuem o mesmo conteúdo e tamanho."
    else:
        if len(p1) != len(p2):
            return "Eles possuem conteúdos e tamanhos diferentes."
        else:
            return "Eles possuem conteúdos diferentes e tamanhos iguais."

def main():
    frase_1 = input("Digite a primeira frase: ")
    frase_2 = input("Digite a segunda frase: ")
    print(verificator(frase_1,frase_2))

if __name__ == "__main__":
    main()