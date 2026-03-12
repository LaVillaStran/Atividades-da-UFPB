def data(f1) -> str:
    meses = {'1':"janeiro",'2':"fevereiro",'3':"março",
             '4':"abril",'5':"maio",'6':"junho",'7':"julho",
             '8':"agosto",'9':"setembro",'10':"outubro",'11':"novembro",
             '12':"dezembro"}
    
    lista = []
    frase = ""
    for i in f1:
        if i != "/":
             frase += i
        elif i == "/": 
            lista.append(frase)
            frase = ""
    lista.append(frase)
    return f"Data por extenso: {lista[0]} de {meses[lista[1]]} de {lista[2]}."

def main():
    frase = input("Informe uma data: ")
    print(data(frase))

if __name__ == "__main__":
    main()