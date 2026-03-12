import random as rd

def repetidor(frase,usados):
    frase_oculta = ""
    for i in range(len(frase)):
        if frase[i] in usados:
            frase_oculta += f"{frase[i]}"
        else:
            frase_oculta += "_ "
    return frase_oculta
    
def entrada(lista):
    tent = input("\nDigite uma letra: ")
    if tent in lista:
        print(f"Tente novamente, você já usou essa palavra!")
        return entrada(lista)
    return tent

def jogo(lista:list):
    randomico = rd.randrange(len(lista))
    tentativa = 0
    frase = [lista[randomico][i] for i in range(len(lista[randomico]))]
    usados = []

    while tentativa < 6:
        frase_oculta = ""
        attempt = entrada(usados)
        usados.append(attempt)

        if attempt in frase:
            frase_oculta = repetidor(frase,usados)
            print(f"A palavra é: {frase_oculta}")

        else:
            tentativa += 1
            if tentativa == 6:
                return f"-> Você errou pela {tentativa}ª vez\n\nVocê perdeu o jogo!"
                
            else: print(f"-> Você errou pela {tentativa}ª vez")

        if frase_oculta == lista[randomico]:
            return f"\nVocê ganhou o jogo!"

def main():
    tamanho = int(input("Digite números de palavras você quer usar na forca: "))
    lista_jogo = [input("Digite a palavra: ") for i in range(tamanho)]
    print(jogo(lista_jogo))

if __name__ == "__main__":
    main()