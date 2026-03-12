def soma(p1,p2,p3):
    if p1 + p2 == p3:
        return f"A soma {p1} + {p2} = {p3}, está correta."
    else:
        return f"A soma {p1} + {p2} = {p3}, está errada."
def tester():
    entrada1 = int(input("Digite uma valor para ser somado: "))
    entrada2 = int(input("Digite outro valor para ser somado: "))
    entrada3 = int(input("Digite uma valor que seria a soma: "))
    return soma(entrada1,entrada2,entrada3)

def main():
    print(tester())

if __name__ == "__main__":
    main()