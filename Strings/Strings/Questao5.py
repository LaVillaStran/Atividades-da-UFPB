"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e
imprima com o nome do mês por extenso.
Ex.:
Informe uma data: 25/10/2018
Data por extenso: 25 de outubro de 2018.
"""

def data(datas):
    dicionario_datas = {"1":"janeiro","2":"fevereiro","3":"março","4":"abril","5":"maio","6":"junho","7":"julho","8":"agosto",
    "9":"setembro","10":"outubro","11":"novembro","12":"dezembro"}
    lista = []
    frase_datas = ""

    for i in datas:
        if i != "/":
            frase_datas += i
        else:
            lista.append(frase_datas)
            frase_datas = ""
    lista.append(frase_datas)

    return lista[0],dicionario_datas[lista[1]],lista[2]

def main():
    entrada = input("Digite uma data com '/': ")
    dia,mes,ano = data(entrada)
    print(f"A data por extenso: \n{dia} de {mes} de {ano}")

if __name__ == "__main__":
    main()