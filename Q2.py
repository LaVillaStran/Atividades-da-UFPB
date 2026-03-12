###Atividade 2
altura = float(input("Digite a altura de uma pessoa para ver seu peso ideal: "))

peso_Masculino = (72.7*altura) - 58
peso_Feminino = (62.1*altura) - 44.7

print(f"O peso ideal masculino seria de: {peso_Masculino:.2f}kg.")
print(f"O peso ideal masculino seria de: {peso_Feminino:.2f}kg.")