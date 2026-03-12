###Atividade 4
print("'M' para matutino; 'V' para vespetino; 'N' para Noturno")

turno = input("Digite o turno que você estuda: ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")