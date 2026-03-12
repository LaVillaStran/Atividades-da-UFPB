coordenadas = int(input("Digite a quantidade de pontos: "))

lista_coordenadas = []

for i in range(coordenadas):
    eixo_x = float(input("\nDigite o valor do eixo X: "))
    eixo_y = float(input("Digite o valor do eixo Y: "))
    lista_coordenadas.append((eixo_x,eixo_y))

distancia = []

for i in range(coordenadas - 1):
    for j in range(i + 1, coordenadas):
        x1, y1 = lista_coordenadas[i]
        x2, y2 = lista_coordenadas[j]

        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        distancia.append(d)

maior = menor = distancia[0]
media = 0

for i in range(len(distancia)):
    media += distancia[i]
    if maior < distancia[i]:
        maior = distancia[i]
    if menor > distancia[i]:
        menor = distancia[i]


print(f"A distância mínima foi de: {menor:.2f}")
print(f"A distância máxima foi de: {maior:.2f}")
print(f"A média de distância foi de: {media/ len(distancia):.2f}")