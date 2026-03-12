def contador_caracter(frase):
    Alfabeto_Auxiliar = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i",
            "J":"j","K":"k","L":"l","M":"m","N":"n","O":"o","P":"p","Q":"q","R":"r",
            "S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
    dicionario = {}
    for i in frase:
        if i in Alfabeto_Auxiliar:
            i = Alfabeto_Auxiliar[i]
        count = 0
        if i in dicionario:
            count = dicionario[i]
        count += 1
        dicionario[i] = count

    return dicionario
            
def main():
    frase = input("Digite uma frase e veja a quantidade de repetições: ")
    print(contador_caracter(frase))

if __name__ == "__main__":
    main()