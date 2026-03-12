Matriz = [[None,None,None],[None,None,None],[None,None,None]]
for i in range(3):
    for j in range(3):
        Matriz[i][j] = int(input("Digite um valor para adicionar na matriz: "))
        
listaL = []
listaC = []

for i in range(3):
    listaL.append(Matriz[1][i])
    listaC.append(Matriz[i][1])

for j in range(3):
    Matriz[j][1] = listaL[j]
    Matriz[1][j] = listaC[j]

print(Matriz)