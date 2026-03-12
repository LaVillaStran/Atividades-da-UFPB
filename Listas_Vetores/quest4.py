import random as rd

n = int(input("Digite a quantidade de vezes que o dado será lançado: "))
while n != 0:
    lista = []
    lista_presenca = []

    for i in range(n):
        dado = rd.randint(1,6)
        lista.append(dado)

    print(lista)

    for i in range(1,7):
        presenca = 0
        for e in range(len(lista)):
            if i == lista[e]:
                presenca += 1
        if presenca > 0:
            lista_presenca.append((i,presenca))
    print(lista_presenca)
    for i in lista_presenca:
        print(f"O número {i[0]} apareceu: {(i[1] / len(lista))*100:.2f}%")
    n = int(input("Digite a quantidade de vezes que o dado será lançado: "))