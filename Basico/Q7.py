###Atividade 7
valor = int(input("Valor: "))

print("Só é aceito 'Cheque' ou 'Dinheiro'!")

forma = input("Forma Pagamento: ")

if forma == "Dinheiro" and valor >= 100:
    valor *= 0.9
    print(f"R$ {valor:.2f}")
else:
    print(f"R$ {valor:.2f}")