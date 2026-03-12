print("Digite '-1' para sair.")
frase = input("Digite uma frase: ")

Alfabeto_Auxiliar = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i",
            "J":"j","K":"k","L":"l","M":"m","N":"n","O":"o","P":"p","Q":"q","R":"r",
            "S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}

while frase != '-1':

    lista_freq = []

    for i in range(len(frase)):
        count = 0
        fraseI = frase[i]
        if frase[i] in Alfabeto_Auxiliar:
            fraseI = Alfabeto_Auxiliar[frase[i]]
        for j in range(len(frase)):
            fraseJ = frase[j]
            if frase[j] in Alfabeto_Auxiliar:
                 fraseJ = Alfabeto_Auxiliar[frase[j]]
            if fraseI == fraseJ:
                count += 1
        lista_freq.append((frase[i],count))

    dicionario = {letra:freq for letra,freq in lista_freq}

    print(dicionario)


    print("Digite '-1' para sair.")
    frase = input("Digite uma frase: ")
