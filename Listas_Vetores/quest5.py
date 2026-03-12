i = 0
lista_mista = []
while i <  10:
    altura = float(input("Digite uma altura: "))
    print("Masculino = (M)\nFeminino = (F)")
    sexo = input("Digite o sexo: ")
    lista_mista.append((altura,sexo))
    i += 1

lista_alturas = []
lista_sexo = []

for i in lista_mista:
    lista_alturas.append(i[0])
    lista_sexo.append(i[1])

maior = menor = lista_alturas[0]

for i in range(len(lista_alturas)):
    
    if maior < lista_alturas[i]:
        maior = lista_alturas[i]
    if menor > lista_alturas[i]:
        menor = lista_alturas[i]

for i in range(len(lista_alturas)):
    if maior == lista_alturas[i]:
        print(f"\nA maior altura é de: {maior} metros\ne essa pessoa é do pessoa é sexo: {lista_sexo[i]}.")
    if menor == lista_alturas[i]:
        print(f"\nA menor altura é de: {menor} metros\ne essa pessoa é do pessoa é sexo: {lista_sexo[i]}.")

media_M = 0
media_F = 0

quant_M = 0
quant_F = 0

for e in range(len(lista_alturas)):
    if lista_sexo[e] == "M":
        media_M += lista_alturas[e]
        quant_M += 1
       
    if lista_sexo[e] == "F":
        media_F += lista_alturas[e]
        quant_F += 1

if quant_M > 0:
    print(f"\nA média de homens é: {(media_M/quant_M):.2f} metros.")
else:
    print("\nNão há homens no grupo.")

if quant_F > 0:
    print(f"A média de mulheres é: {(media_F/quant_F):.2f} metros.")
else:
    print("Não há mulheres no grupo.")

print(f"\nTem {quant_M} homens e {quant_F} mulheres.")