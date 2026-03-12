"""
Escreva um programa que solicite ao usuário que digite um número de 1 a 99 e imprima-o
na tela por extenso. 
"""


def extenso(n1):
    dicionário_importatne = {1:"um",2:"dois",3:"três",4:"quatro",5:"cinco",6:"seis",7:"sete",8:"oito",9:"nove",10:"dez",
                             11:"onze",12:"doze",13:"treze",14:"quatorze",15:"quinze",16:"dezesseis",17:"dezessete",18:"dezoito",
                             19:"dezenove",20:"vinte",30:"trinta",40:"quarenta",50:"cinquenta",60:"sessenta",70:"setenta",80:"oitenta",
                             90:"noventa"}
    
    if n1 <= 20:
        return dicionário_importatne[n1]
    if n1 > 20:
        frase = ""
        inter = (n1 // 10)#### 41 - - - - > 41//10 --> 4
        if inter < 10:
            frase += dicionário_importatne[ (inter)*10 ] ### 4*10 --> 40
            if (n1 - (inter * 10)) <= 9 and (n1 - (inter * 10)) != 0: ### 41 - 40 <= 9 e diferente de 0
                frase += f" e {dicionário_importatne[n1 - (inter * 10)]}"
        return frase
    
def main():
    valor = int(input("Digite um número de 1 a 99 para ver sua versão em extenso: "))
    print(extenso(valor))

if __name__ == "__main__":
    main()